
class DataPoint:
    def __init__(self, start, end, link, duration, changes):
        self.start= start
        self.end = end
        self.link = link
        self.duration = duration
        self.changes = changes
        self.pricesAmount = []
        self.pricesName = []

def getDataPoints(startTimes, endTimes, links, changes, durations):
    for d in durations:
        print(f'Duration 1: {type(d)}')
    dataPoints = []
    for idx, item in enumerate(startTimes):
        print(type(durations[idx]))
        dataPoints.append(DataPoint(startTimes[idx], endTimes[idx], links[idx], durations[idx], changes[idx]))
    return dataPoints