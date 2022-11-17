
def getMin(freq):
    starts = []
    start = 5
    while start < 60:
        startString = f'{start}'
        if len(startString) < 2:
            startString = f'0{startString}'
        starts.append(startString)
        start += freq
    return starts

def getTimeStrings(freq):
    startMins = getMin(freq)
    hour = 0
    timeStrings = []
    while hour < 24:
        hourString = f'{hour}'
        if len(hourString) < 2:
            hourString = f'0{hourString}'
        for minString in startMins:
            timeStrings.append(f'{hourString}:{minString}')
        hour += 1
    return timeStrings
    #return ['10:05']

""" startTimes = [1,2]
endTimes = [1,2,3]
links = [1,2] 
it = iter([startTimes, endTimes, links])
the_len = len(next(it))
if not all(len(l) == the_len for l in it):
    raise ValueError('not all lists have same length!')
else:
    print('true') """