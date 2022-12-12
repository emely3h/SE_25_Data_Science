import requests as rq
import re
import csv
from startTimes import getTimeStrings
import time
from dbEntry import DBEntry
from datapoint import DataPoint



def getDataPoints(startTimes, endTimes, links, changes, durations):
    dataPoints = []
    for idx, item in enumerate(startTimes):
        try:
            dataPoints.append(DataPoint(startTimes[idx], endTimes[idx], links[idx], durations[idx], changes[idx]))
        except:
            print('ERROR ERROR: lists do not have same length')
    return dataPoints


def getPricesFrom(text):
    pricesFrom = []
    for match in re.finditer('&nbsp;&#128', text):
            pricesFrom.append(text[match.start()-6]+text[match.start()-5]+text[match.start()-4]+text[match.start()-3]+text[match.start()-2]+text[match.start()-1])
    return pricesFrom

def getLinks(text):
    links = []
    for match in re.finditer('href="https://reiseauskunft.bahn.de/bin/query.exe', text): #<a class="buttonbold" 
        urlStartIndex = match.start()+6 #28
        subUrl = text[urlStartIndex:]
        subUrl = subUrl.split('"', 1)[0]
        subUrl = subUrl.replace('amp;', '')
        if('sTID=' in subUrl):
            links.append(subUrl)
    return links

def getDurationsChanges(text):
    durations = []
    changes = []
    for match in re.finditer('<div class="duration"', text):
        duration = text[match.end():]
        change = duration
        change = change.split('changes')[1][:4]
        change = change[2:][1]
        changes.append(change)
        duration =  duration.split('>', 3)[3]
        duration = duration.split('<',1)[0]
        durations.append(duration)
    return durations, changes

def getStartTimes(text):
    startTimes = []
    for match in re.finditer('"timeDep">', text):
            startTimes.append(text[match.end()+1:match.end()+6])
    return startTimes

def getEndTimes(text):
    endTimes = []
    for match in re.finditer('"timeArr">', text):
        endTimes.append(text[match.end():match.end()+5])
    return endTimes

def getPriceAndTicketNames(dataPoints):
    for dataPoint in dataPoints: 
        subPage = rq.get(dataPoint.link)
        counter = 0
        while(len(subPage.text) < 10000 and counter<10):
            subPage = rq.get(dataPoint.link)
            if counter < 9:
                print(f'ERROR: calling for sublink {counter}')
            else:
                print('ERROR ERROR: missing sublink')
            counter += 1
            time.sleep(3)
        priceOptionsAmount = []
        priceOptionsName = []
        for match in re.finditer('availabilityOfferName availabilityHeight', subPage.text):
            name = subPage.text[match.end()+2:]
            name = name.split('<',1)[0]
            name = name[1:-1]
            name = name.replace('\n', ' ')
            priceOptionsName.append(name)
        for match in re.finditer('fareAmount', subPage.text):
            price = subPage.text[match.end()+2:]
            price = price.split('<',1)[0]
            priceOptionsAmount.append(price)
        
        dataPoint.pricesAmount = priceOptionsAmount
        dataPoint.pricesName = priceOptionsName
    return dataPoints
        
def check_for_blocking_response(url, timeString):
    page = rq.get(url)
    counter = 0
    while(len(page.text) < 10000 and counter<10): # status code still 200 
        page = rq.get(url)
        counter += 1
        if counter < 9:
            print(f'ERROR: calling for link {counter}')
        else:
            print(f'ERROR ERROR: missing timestamp {timeString}')
        time.sleep(3)
    return page

def getAllEntriesForDay(departureStation, destinationStation, date, age, discount, tariffClass, freq):
    timeStrings = getTimeStrings(freq)
    allEntries = []
    uniqueTimeKeys = set()
    for timeString in timeStrings:
        startTime = timeString
        url = f'https://reiseauskunft.bahn.de/bin/query.exe/dn?start=1&existOptimizePrice-deactivated=1&REQ0JourneyStopsS0A=1&S={departureStation}&REQ0JourneyStopsSID=A%3D1%40O%3DBerlin+Hbf%40X%3D13369549%40Y%3D52525589%40U%3D81%40L%3D008011160%40B%3D1%40p%3D1666201716%40&REQ0JourneyStopsZ0A=1&Z={destinationStation}&REQ0JourneyStopsZID=A%3D1%40O%3DBiberach%28Ri%C3%9F%29%40X%3D9793127%40Y%3D48101845%40U%3D81%40L%3D008000943%40B%3D1%40p%3D1666201716%40&date={date}&time={startTime}&timesel=depart&returnDate=&returnTime=&optimize=0&auskunft_travelers_number=1&tariffTravellerType.1={age}&tariffTravellerReductionClass.1={discount}&tariffClass={tariffClass}&externRequest=yes&HWAI=JS%21js%3Dyes%21ajax%3Dyes%21#hfsseq1|dv.03240894.1666477996'
        
        page = check_for_blocking_response(url, timeString)
        links = getLinks(page.text)
        durations, changes = getDurationsChanges(page.text)
        startTimes = getStartTimes(page.text)
        endTimes = getEndTimes(page.text)
        dataPoints = getDataPoints(startTimes, endTimes, links, changes, durations)
        dataPoints = list(filter(lambda dataPoint: f'{dataPoint.start}-{dataPoint.end}' not in uniqueTimeKeys, dataPoints))
        dataPoints = getPriceAndTicketNames(dataPoints)
                

        for dataPoint in dataPoints:
            uniqueTimeKeys.add(f'{dataPoint.start}-{dataPoint.end}')
            for idx, price in enumerate(dataPoint.pricesName):
                dbEntry = DBEntry(dataPoint.pricesAmount[idx], dataPoint.pricesName[idx], age, discount, date, departureStation, destinationStation, dataPoint.duration, dataPoint.start, dataPoint.end, dataPoint.changes, tariffClass)
                allEntries.append(dbEntry)
        print('DONE Day: '+ date + ' | ' + timeString)

    return allEntries

def saveAllEntriesToFile(date, age, discount, allEntries, folderName):
    fileLoc = f'{folderName}/{date[-10:-8]}_{date[-7:-5]}_{date[-4:]}_{age}_{discount}.csv'

    print('FILELOC')
    print(fileLoc)
    with open(fileLoc, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        listToWrite = [['price', 'ticketType', 'age', 'discount', 'date', 'departure', 'destination', 'duration', 'startTime', 'arrivalTime', 'changes', 'searched tariffClass']]

        for entry in allEntries:
            listToWrite.append(entry.toList())
        writer.writerows(listToWrite) 

def getDataForDay(departureStation, destinationStation, date, age, discount, tariffClass, freq, folderName):

    allEntries = getAllEntriesForDay(departureStation, destinationStation, date, age, discount, tariffClass, freq)
    print('Done Scraping, date: '+ date)
    saveAllEntriesToFile(date, age, discount, allEntries, folderName)
    print('Done saving to file, date: '+ date)


