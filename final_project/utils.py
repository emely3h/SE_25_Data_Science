import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
import datetime
from datetime import timedelta
import os

def read_data(path):
    headers = ['price', 'ticket type', 'age', 'discount', 'date', 'departure', 'destination', 'duration', 'start time', 'arrival time', 'changes', 'tariffClass']
    return pd.read_csv(path, skiprows=[0], header=None, names=headers)

def check_arr_next_day(dep, arr):
    if dep > arr:
        arr = arr + timedelta(days=1)
    return arr
def clean_data(df_raw):
    """ 
    As there the webpage only returns 3-4 routes with one timestamp I had to coninuously fetch
    data every couple of minutes to get all travel options of the day which led to collecting
    duplicates 
    """
    df_clean = df_raw.drop_duplicates()
    # get rid of irrelevant ticket types
    df_clean.drop(df_clean[df_clean['ticket type'] == 'Normalpreis'].index, inplace = True)

    # parsing data types
    df_clean['price'] = df_clean['price'].str.replace(',','.')
    df_clean['price'] = df_clean['price'].astype(float)

    df_clean['date'] = df_clean['date'].str.slice(start=4)


    df_clean['datetime dep'] = df_clean['start time'] +'-'+ df_clean['date']
    df_clean['datetime arr'] = df_clean['arrival time'] +'-'+ df_clean['date']
    df_clean['datetime dep'] = pd.to_datetime(df_clean['datetime dep'], format="%H:%M-%d.%m.%Y")
    df_clean['datetime arr'] = pd.to_datetime(df_clean['datetime arr'], format="%H:%M-%d.%m.%Y")

    df_clean['datetime arr'] = df_clean.apply(lambda row: check_arr_next_day(row['datetime dep'], row['datetime arr']), axis=1 )

    # calculating travel time
    df_clean['sub [min]'] = (df_clean['datetime arr'] - df_clean['datetime dep']).astype('timedelta64[m]')

    df_clean = df_clean.drop('date', axis=1)
    df_clean = df_clean.drop('duration', axis=1)
    df_clean = df_clean.drop('start time', axis=1)
    df_clean = df_clean.drop('arrival time', axis=1)

    df_clean['departure'] = df_clean['departure'].apply(lambda x: 'Berlin' if x == 'Berlin+Hbf' else x)
    df_clean['destination'] = df_clean['destination'].apply(lambda x: 'Biberach' if x == 'Biberach%28Ri%C3%9F%29' else x)
    df_clean['destination'] = df_clean['destination'].apply(lambda x: 'Memmingen' if x == 'Bahnhof+ZOB%252C+Memmingen' else x)

    df_clean['time'] = pd.to_datetime(df_clean['datetime dep']).dt.strftime('%H:%M')
    return df_clean

def save_plot(plot, filename):
    sb.move_legend(plot, "upper left", bbox_to_anchor=(1, 1))

    fig = plt.get_figure()
    fig.savefig(filename, dpi=200, bbox_inches='tight')

def create_single_plot(day, route, discount, tariffClass, path, age):

    df = get_df_single_day(path)
    
    plt = sb.lineplot(data=df, x='time', y='price', hue='ticket type')
    plt.set_xticklabels(plt.get_xticklabels(),rotation = 40)
    plt.tick_params(labelsize=7)
    title = f'{route} {day} | age: {age}, discount: {discount}, class: {tariffClass}'
    plt.set(title=title)
    sb.move_legend(plt, "upper left", bbox_to_anchor=(1, 1))

    fig = plt.get_figure()
    fig_path = f'plots/{route}/{day}_lineplot.png'
    fig.savefig(fig_path, dpi=200, bbox_inches='tight')

def create_multiple_plots():
    
    day = datetime.datetime.strptime('11_11_2022', '%d_%m_%Y').date()
    day_string = day.strftime('%d_%m_%Y')
    route='berlin-memmingen'
    age='E'
    discount='1'
    tariffClass='1'
    path=f'data/{route}/data_{age}_{discount}_{tariffClass}/{day_string}_{age}_{discount}.csv'

    for i in range(1, 12):
        plt.figure()
        create_single_plot(day_string, route, discount, tariffClass, path, age)
        day = datetime.datetime.now() + datetime.timedelta(i)
        day_string = day.strftime('%d_%m_%Y')
        path=f'data/{route}/data_{age}_{discount}_{tariffClass}/{day_string}_{age}_{discount}.csv'

def get_df_single_day(path):
    try:
        df = read_data(path)
        df = clean_data(df)
    except FileNotFoundError:
        return pd.DataFrame()
    return df

day = datetime.datetime.strptime('11_11_2022', '%d_%m_%Y').date()
day_string = day.strftime('%d_%m_%Y')
route='berlin-memmingen'
age='E'
discount='1'
tariffClass='1'
path=f'data/{route}/data_{age}_{discount}_{tariffClass}/{day_string}_{age}_{discount}.csv'


def merge_multiple_tables(path, start, end):
    merge_table = pd.DataFrame()


    for file in os.listdir(path):  
        file_path = path + '/' + file
        table = get_df_single_day(file_path)
        merge_table = pd.concat([merge_table, table], ignore_index=True)
    return merge_table

def merge_multiple_tables_custom(path, start_date, total_days=None, end_date = None):
    day = pd.to_datetime(start_date, format='%d.%m.%Y')
    
    if end_date is None:
        end_date = day + datetime.timedelta(days = total_days)
    else:
        end_date = pd.to_datetime(end_date, format='%d.%m.%Y')
    merge_table = pd.DataFrame()
    while day < end_date:
        day_string = day.strftime('%d_%m_%Y')
        file_path = path + '/' + day_string + '.csv' 
        table = get_df_single_day(file_path)
        if table.empty == False:
            merge_table = pd.concat([merge_table, table], ignore_index=True)
        day = day + datetime.timedelta(1)
    return merge_table

def scatterplot_over_day_multiple_days_all_ticket_types():
    table = merge_multiple_tables()
    plt = sb.scatterplot(data=table, x='time', y='price', hue='ticket type', s=6)
    plt.set_xticklabels(plt.get_xticklabels(),rotation = 40)
    plt.tick_params(labelsize=7)
    title = f'Price development in a single day'
    plt.set(title=title)
    sb.move_legend(plt, "upper left", bbox_to_anchor=(1, 1))

    fig = plt.get_figure()
    fig_path = f'plots/berlin-memmingen/all_days.png'
    fig.savefig(fig_path, dpi=200, bbox_inches='tight')

def filter_price_differences(df, min_max, max_changes, max_duration):

    # Filter out rows that don't fit the constraints
    df.drop(df[df['sub [min]'] > max_duration].index, inplace = True)
    df.drop(df[df['changes'] > max_changes].index, inplace = True)

    df_flexpreis_plus = df.loc[df['ticket type'] == 'Flexpreis Plus']
    df_flexpreis_plus.sort_values('price')
    flexpreis_plus_max = df_flexpreis_plus.iloc[0]
    flexpreis_plus_min = df_flexpreis_plus.iloc[-1]

    df_flexpreis = df.loc[df['ticket type'] == 'Flexpreis']
    df_flexpreis.sort_values('price')
    flexpreis_max = df_flexpreis.iloc[0]
    flexpreis_min = df_flexpreis.iloc[-1]

    if flexpreis_plus_max['price'] != flexpreis_plus_min['price']:
        concat = pd.concat([pd.DataFrame(flexpreis_plus_max), pd.DataFrame(flexpreis_plus_min)],axis=1)
        concat = concat.transpose()
        min_max = pd.concat([min_max, concat])

    if flexpreis_max['price'] != flexpreis_min['price']:
        concat = pd.concat([pd.DataFrame(flexpreis_max), pd.DataFrame(flexpreis_min)], axis=1)
        concat = concat.transpose()
        min_max = pd.concat([min_max, concat])

    return min_max