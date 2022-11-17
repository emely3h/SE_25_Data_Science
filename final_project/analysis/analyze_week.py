import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
import datetime

from utils import read_data, clean_data, get_df_single_day, merge_multiple_tables




ticket_type = 'Super Sparpreis'

route='memmingen-berlin'


total_days = 14



def create_multiple_plots():
    discount='2'
    tariffClass='2'
    ages = ['E', 'Y']
    discounts = ['0','1','2','3','4']


    for age in ages:
        for discount in discounts:
            tariffClass = '1'
            if discount == '2' or discount == '4':
                tariffClass = '2'
            title = f'Price development over week: 11.11 - 25.11,{ticket_type} {age}, discount: {discount}, {tariffClass} class'
            fig_path = f'plots/analyse_weekdays/super_sparpreis/{route}_{age}_{discount}_{tariffClass}_11.11-25.11.png'
            create_plot(route, age, tariffClass, total_days, discount, title, fig_path )
            if discount =='0':
                tariffClass = '2'
                title = f'Price development over week: 11.11 - 25.11,{ticket_type} {age}, discount: {discount}, {tariffClass} class'
                fig_path = f'plots/analyse_weekdays/super_sparpreis/{route}_{age}_{discount}_{tariffClass}_11.11-25.11.png'
                create_plot(route, age, tariffClass, total_days, discount, title, fig_path )

    

def create_plot(route, age, tariffClass, total_days, discount, title, fig_path):

    df = merge_multiple_tables(route, age, tariffClass, total_days, discount)

    df = df.loc[df['ticket type'] == ticket_type]

    df['weekday'] = df['datetime dep'].dt.day_name()

    df = df.sort_values(by=['time'])

    plt = sb.scatterplot(data=df, x='time', y='price', hue='weekday', s=6)
    plt.set_xticklabels(plt.get_xticklabels(),rotation = 40)
    plt.tick_params(labelsize=5)

    plt.set(title=title)
    sb.move_legend(plt, "upper left", bbox_to_anchor=(1, 1))

    fig = plt.get_figure()
    fig.savefig(fig_path, dpi=200, bbox_inches='tight')


create_multiple_plots()
