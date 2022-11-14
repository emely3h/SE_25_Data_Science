recomendation system => predicting missing data, interpolation

### explanatory analysis
- many plots, fast
- one-liners

#### explanatory analysis
- styling, takes time
- matplot lib
- darkboard
- plotly

### fireworks
- 3D
- animations
- fancy colors
- buttons


## Descriptive Statistics

    - Centrality
        mean
        median
        mode
    - Spread
        min 
        max
        turning points
        quartiles
        standard deviation
        varianz
    - Other
        regression lines 
        => correlation coefficient r^2
    describe()
    cor()

look for patterns/ correlation
how to access character of dame in df column => df['name'].str[0]

### Measures of Centrality
- arithmetic mean => Durchschnitt => outliers can falsify result
- median => middle value of a list => does not take occurences into account
- mode = >value that occures the most often => not necessarily median

### Measures of Spread
- range => min + max
- quartiles => useful for box plots, divide list into quaters, from each quater take the median = quartile
  - interquartile range = Q3 - Q1
- variance => how far data set is spread out
  - average of the quared differences from the mean
  - sigma^2 = sum(X - u)^2 / N
  - => u = mean
  - => N = total number of values
  - => X each value
  - prefered for statistical tests
- standard deviation => square root of variance
  - unit easier to understand than variance, same unit than meassured values
  - homoscedasticity/ homogeneity of variances = equal or similar variances in different groups
- percentile
  - In statistics, a k-th percentile (percentile score or centile) is a score below which a given percentage k of scores in its frequency distribution falls (exclusive definition) or a score at or below which a given percentage falls (inclusive definition). 

### Distribution
- monodal, bimodal, multimodal
- if not monodal groupd does not consits of one homegenous groups but of thwo or multiple subgoups
- when examining histogram of a variable check how many max there are => mono, bi or multimodal
- Is there a predominant distribution?
- power law distribution
  - functional relationship between two quantities where a relative change in one quantity results in a proportional relative change in the other quantity, one quantity varies as a power of an other
- long tail distribution
  - 
### Normalize
- generic term that refers to all kinds of mathematical transformations before analyzing, some frequent normalization procedures are:
  - calculating percentages against a mean value
  - scaling the data to values from 0.0 to 10.0
  - scaling the data to a standard normal distrubution
  - taking the binary of decadic logarithm of all values

### Correlation
- To see if two parameters correlate start with
  - inspecting a scatter plot to see if there are any visible sub-groups
  - calculate correlation coefficients

### Multiindexing
In pandas we don't have to think in data models and cardinality
advantage of the library is multiindexing being able to create multidimensional tables.

### Distribution
- normal distribution
- uniform distribution
- triangular distribution
- binominal distribution
- power law distribution/ longtail distribution
- poisson distribution
- Central Limit Theorem => if you sum up many distriubtion the result will always be a normal (gaussian) distribution

### Epistemology
Subfield of psychology, how to determine what we know
"What can we know?" - Kant
hypothetical realism => root assumtion of science
Assumptions => Reality => Observations => Model => explains Reality
Gödel: if you are describing a complex system, your model is either going to be incomplete or contradicting
Popper: A model needs be falsifyable otherwise it is not a scientific model
Kuhn: Science is an evolutionary process, models envolve constantly
Occams Razor: if multiple models fit, the best one is always the simpler one

### Machine Learning Intro
coursera course for basics: andrew ng
- Step 1: Split into training and test sets
- Step 2: Train a model
  - RandomForestClassifier => comes up with the smalles amount of questions to answer the prediction
  - define what to predict from what
- Step 3: Evaluate
Machine learning models to learn about: psychic learn
- linear regression
- logistic regression
- random forests and gradient boosting
- principal component analysis (unsupervised)
- support vector machines
- clustering T-SNE, multidimensional scaling
- neural networks, if and only if you have a lot of complex data (images,text, voice signals,... if less then 1000 datapoints don't even think about it)

### Project Ideas
- Does tourism in thailand have more positive or negative impact?
- something related to bioinformatics
- something related to learning languages => which countries are better than others what do they better, related to watching movies?
- german crime statistics
- analysis of train tickets, when to best buy tickets
  - when to book before prices increase
  - which route to take
  - which combination of discounts is best, how much impact does discount have
  - which time of day is cheapest
  - how to get cheap first class tickets
  - instead of focusing on one route which route is the cheapes/ at which age best prices?/ Which region has least train connections
  - focus on fernverkehr oder auch nahverkehr? Begrenzung auf Europa?
  - compare which screens deliver which results 
  - how would an ideal screen look like to find the best suited ticket at once?
  - why and when are prices changing
  - maybe do the analysis for several routes to compare
  - I can only make all request from the same date and change the travel date but would be interesting to see how results change if travel date is fixed but I make same requests every day until travel date
  - 

see if there already exist similar projects, e.g. for flight price analysis

Other methods not yet discussed

regression
hypothesis testing

### price factors
- age
- bahncard
### types of tickets
- normalpreis
- flexpreis
- flexpreis plus
- sparpreis | sparpreis young | sparpreis senioren | sparpreis gruppe
- supersparpreis | supersparpreis young | supersparpreis senioren | supersparpreis gruppe
- 1. Klasse 2. Klasse


### endpoints
reiseauskunft.bahn.de
normal ticketauskunft bis 90 Tage im vorraus, aktuell nur bis 9.12?? ab 12.10 preisauskunft für tickets ab 11.12
über stadata api auskunft über bahnhöfe: https://developers.deutschebahn.com/db-api-marketplace/apis/product/stada


### Questions
- how to collect data
  - would need to scrape
  - 2 requests to find out about different ticket types + only 3 results at once 
- which methods to apply
- how to deal with holidays => falsify results

Fahrplansukunft in die Vergangenheit möglich aber ohne preisauskunft

Wenn zu kompliziert besser recherche über zuglinienabdeckung? Region mit schlechtester Anbindung?

Look into: https://github.com/juliuste/db-prices


Wenn dem so ist, ergibt sich daraus ein wichtiges Kriterium bei der Preissuche: Wenn du ein günstiges Flex-Preis-Ticket zu einer “verrückten” Tageszeit findest, z.B. 0:12 Uhr in der Nacht, das nur eine ICE-Verbindung enthält, kannst du damit den ganzen Tag auf dieser Strecke reisen. Idealerweise auch auf einer Direktverbindung, nur mit dem ICE. In dem Fall ist erst Recht wichtig, Preise immer in einem großzügigen Zeitfenster zu vergleichen.

https://www.kaggle.com/datasets/thegurusteam/spanish-high-speed-rail-system-ticket-pricing/discussion


as alternative , looking at fahrplanauskunft api and see which regions has worst train accessability?
https://data.deutschebahn.com/dataset/api-fahrplan.html
