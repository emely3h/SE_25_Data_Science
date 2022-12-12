import datetime

from getDataForDay import getDataForDay



"""
INPUT VARIABLES:

ROUTES
- Berlin Hbf - Biberach (Riß)
- Berlin Hbf - Memmingen Hbf
- Memmingen Hbf - Berlin Hbf

AGE GROUPS
- Adult: 27 - 64 years old (A)
- Youth: 16 - 26 years old (Y)

TARIFF CLASS
- First class (1)
- Second class (2)

DISCOUNT SUBSCRIPTION
- Bahncard 25, first class (1)
- Bahncard 25, second class (2)
- Bahncard 50, first class (3)
- Bahncard 50, second class (4)
"""

weekdays = {
    0: 'Mo',
    1: 'Di',
    2: 'Mi',
    3: 'Do',
    4: 'Fr',
    5: 'Sa',
    6: 'So'
}

departureStation = 'Berlin+Hbf'
destinationStation = 'Biberach%28Ri%C3%9F%29'
startTime = '00:00'
ages = ['Y', 'A'] 
discounts = ['1', '2', '3', '4'] 
tariffClasses = ['1', '2']

test = 0
print(test)


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

def for_input_variables(start, destination, folder_name):
    for age in ages:
        for discount in discounts:
            for tariffClass in tariffClasses:
                print(f'TIMESTAMP: {datetime.datetime.now()} data_{age}_{discount}_{tariffClass}')
                getData(1, 90, '../data/{folder_name}/data_{age}_{discount}_{tariffClass}', start, destination, age, discount, tariffClass)

def main():
    for_input_variables('Berlin+Hbf', 'Biberach%28Ri%C3%9F%29', 'berlin-biberach')
    for_input_variables('Berlin+Hbf', 'Bahnhof+ZOB%252C+Memmingen', 'berlin-memmingen')
    for_input_variables('Bahnhof+ZOB%252C+Memmingen', 'Berlin+Hbf', 'memmingen-berlin')
    
main()
print('All Done!!!')




