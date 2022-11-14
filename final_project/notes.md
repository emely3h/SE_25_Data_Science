## Deutsche Bahn

Analyzing ticket prices of the Deutsche Bahn for selected routes with varying conditions.
How to find the optimal ticket and when to book best?

### Questions
- Which is the best (cheap + fast) route to my parents?
- What is the cheapest travel day?
- Chapes time to travale a day
- How much in advance do I have to book/ when do prices start increasing?
- Is it worth to have a bahncard/ which bahncard is the best suited for me/ how much discount do I really get in the end/ does the discount variate/ is there a pattern?
- Are there any irregularities, e.g first klass ticket cheaper than secon class/ regular price with city ticket chaeaper than sparpreis, flexticket cheaper than regular ticket, ....
- (Does the )
- Is it possible to predict the prices?



### Variablen:
Strecken
- Berlin hbf - Biberach an der Riß
- Berlin hbf - Memmingen
- Berlin - München
  => Hin und zurück?

Konditionen:
- 27-64 without Bahncard 2. Klasse
- 27-64 + Bahncard 40 2. Klasse
- 27-64 without Bahncard 1. Klasse
- 27-64 + Bahncard 40 1. Klasse
- 15-26 + Bahncard 50 2. Klasse
- 15-26 + Bahncard 50 1. Klasse

Tageszeitspanne
- Verbindungen mit Abfahrtszeit jeweils von 00:00 bis 23:59 Uhr

Zeitspanne
Jeweils für 90 Tage im Vorraus

### DBEntry
- Abfahrtszeit
- Ankunftszeit
- AbfahrtsBahnhof
- Zielbahnhof
- Umstiege
- Dauer
- Preis
- Tickettyp
- Datum

psycic learn random forest datensatz in 80 % training und 20 % auswertung unterteilen, zufällig, mit random seed
trainTestSplit()titanic challenge kaggle

preisvorhersage, onehotencoding 

'Berlin+Hbf'
    destinationStation = 'Biberach%28Ri%C3%9F%29'


## Getting the data
explain script, explain diffficulties, explain how much data, folder structure
defining vocabulary
double entries at the beginning

## Cleaning data

## Estimate how good data is, how many entries have been missed
claculate mean entries of each day for each option, see how much variety



### Question what time of day are tickets cheapest?

first plot example: 1.12, adult, no discount

matters if you look at sparpresi or flexpreis
you would think that flexpreis ticket is constant in price because once you have the ticket you can take any train you want. 
Flexpreis tickets tend to be cheaper in the middle of the day at 11:30 and 15:30

#### Todo
Just this one day => does it tend to be the same for the other days, other age and discount groups?

#### Takeaways
before buying a flexticket, check if it is cheaper at an other time