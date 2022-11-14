import datetime

from getDataForDay import getDataForDay


""" # alle 30 min abfrage, duplicate am Ende rausfiltern
departureStation = 'Berlin+Hbf'
destinationStation = 'Biberach%28Ri%C3%9F%29'
startTime = '00:00'
age = 'Y' #Y: 15-26,  K: 6-14, E: 27-64, S: ab 65
discount = '3' # 1: 25%, 1.Klasse, 2: 25%, 2.Klasse, 3: 50%, 1.Klasse, 4: 50%, 2.Klasse, 16: 100%, 1.Klasse, 17: 100%, 2.Klasse
tariffClass = '1' or '2'
# optimized price thing? """


# 3 Strecken: 
## Berlin - Biberach
    # Y, 0
    # Y, 1
    ## Y, 2
    ## Y, 3
    ## Y, 4
## Biberach - Berlin
    ## Y, 0
    ## Y, 1
    ## Y, 2
    ## Y, 3
    ## Y, 4
## Berlin - Memmingen
## Memmingen - Berlin
## Berlin - München

# 90 Tage

# 4 Altersklassen
# 4 Preisklassen

# => 58 * 1000

weekdays = {
    0: 'Mo',
    1: 'Di',
    2: 'Mi',
    3: 'Do',
    4: 'Fr',
    5: 'Sa',
    6: 'So'
}



def numToString(number):
    if len(str(number)) < 2:
        return '0'+str(number)
    else:
        return str(number)


def getData(start, end, folderName, departureStation, destinationStation, age, discount, tariffClass):
    for i in range(start, end):
        current_date = datetime.datetime.now() + datetime.timedelta(i)
        weekDayString = f'{weekdays[current_date.weekday()]}'
        dayString = f'{weekDayString}.,{numToString(current_date.day)}.{numToString(current_date.month)}.{current_date.year}'
        print(f'Get All Data For Day: {dayString} current timestamp: {datetime.datetime.now()}')
        getDataForDay(departureStation, destinationStation, dayString, age, discount, tariffClass, 50, folderName)
        print(f'Finish Getting All Data For Day: {dayString} current timestamp: {datetime.datetime.now()}')

""" print(f'TIMESTAMP: {datetime.datetime.now()}')
getData(67, 90, 'data_Y_3', 'Berlin+Hbf', 'Biberach%28Ri%C3%9F%29', 'Y', '4')
print(f'TIMESTAMP: {datetime.datetime.now()}') """
# getData(75, 90, 'data_Y_4', 'Berlin+Hbf',  'Biberach%28Ri%C3%9F%29', 'Y', '4') 
# print(f'TIMESTAMP: {datetime.datetime.now()}')
# getData(1, 90, 'data_E_0', 'Berlin+Hbf',  'Biberach%28Ri%C3%9F%29', 'E', '0', '1')
# getData(1, 90, 'data_E_0', 'Berlin+Hbf',  'Biberach%28Ri%C3%9F%29', 'E', '0', '2')

""" print(f'TIMESTAMP: {datetime.datetime.now()}')
getData(14, 90, 'data_E_1', 'Berlin+Hbf',  'Biberach%28Ri%C3%9F%29', 'E', '1', '1')
print(f'TIMESTAMP: {datetime.datetime.now()}')
getData(1, 90, 'data_E_2', 'Berlin+Hbf',  'Biberach%28Ri%C3%9F%29', 'E', '2', '2') """

""" print(f'TIMESTAMP: {datetime.datetime.now()}')
getData(1, 90, 'data_E_3_1', 'Biberach%28Ri%C3%9F%29', 'Berlin+Hbf', 'E', '3', '1') 

print(f'TIMESTAMP: {datetime.datetime.now()}')
getData(1, 90, 'biberach-berlin/data_E_4_2', 'Biberach%28Ri%C3%9F%29', 'Berlin+Hbf', 'E', '4', '2')
print(f'TIMESTAMP: {datetime.datetime.now()}') """

#############################################
#print(f'TIMESTAMP: {datetime.datetime.now()} data_Y_0_1')
#getData(1, 90, 'data_Y_0_1', 'Biberach%28Ri%C3%9F%29', 'Berlin+Hbf', 'Y', '0', '1')

#print(f'TIMESTAMP: {datetime.datetime.now()} data_E_4_2')
#getData(1, 90, 'data_E_4_2', 'Berlin+Hbf', 'Bahnhof+ZOB%252C+Memmingen', 'E', '4', '2')

print(f'TIMESTAMP: {datetime.datetime.now()} data_Y_1_1')
getData(1, 90, 'data_Y_1_1', 'Bahnhof+ZOB%252C+Memmingen',  'Berlin+Hbf', 'E', '1', '1')

print(f'TIMESTAMP: {datetime.datetime.now()} data_Y_2_2')
getData(1, 90, 'data_Y_2_2', 'Bahnhof+ZOB%252C+Memmingen',  'Berlin+Hbf', 'E', '2', '2')

print(f'TIMESTAMP: {datetime.datetime.now()} data_Y_3_1')
getData(1, 90, 'data_Y_3_1', 'Bahnhof+ZOB%252C+Memmingen',  'Berlin+Hbf', 'E', '3', '1')

print(f'TIMESTAMP: {datetime.datetime.now()} data_Y_4_2')
getData(1, 90, 'data_Y_4_2', 'Bahnhof+ZOB%252C+Memmingen', 'Berlin+Hbf', 'E', '4', '2')



print('All Done!!!')


# camelcase or lowercase?

# continue getting data
# clean data script
# script for getting 90 days in one plot
