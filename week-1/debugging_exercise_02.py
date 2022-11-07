#!/usr/bin/env python
# coding: utf-8

# Debugging Exercise: Population Growth

# We want to plot the population growth of a few selected countries.
# 
# The CSV file contains the population in millions.
# 
# Fix five bugs in the analysis.

import pandas as pd


df = pd.read_csv('population.csv')
df.head()

# drop empty column
del df[1949]

# drop rows with missing data
df.dropna(inplace=True)

df = df.set_index('country', inplace=True)
df.head()

countries = df.loc['Argentina', 'Ukraine', 'Vietnam', 'Zimbabwe']
countries

# tilt the table by 90°
timeline = countries.transpose()
timeline.head()

# why is this a terrible plot?
timeline.plot()
