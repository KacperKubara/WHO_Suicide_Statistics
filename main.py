import importlib
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
utils = importlib.import_module('utils')

# Importing the data
path = '~/Desktop/Machine Learning/Datasets/who_suicide_statistics.csv' 
path1 = '~/Desktop/Machine Learning/Datasets/world_population.csv'
dataset = pd.read_csv(path)
world_population = pd.read_csv(path1, index_col = 0)

# Check the suicides by gender
female = dataset[dataset.sex == 'female'].suicides_no.sum(axis = 0)
male = dataset[dataset.sex == 'male'].suicides_no.sum(axis = 0)
#print('Female: ' + str(female) + ' ,Male: ' + str(male))

# Display the suicides by gender over the years
timespan = list(dataset.year.unique())
timespan.sort(reverse = False)
deaths_by_year_male   = list()
deaths_by_year_female = list()
for year in timespan:
    deaths_by_year_male.append(dataset[(dataset.year == year) & (dataset.sex == 'male')].suicides_no.sum(axis = 0))
    deaths_by_year_female.append(dataset[(dataset.year == year) & (dataset.sex == 'female')].suicides_no.sum(axis = 0))
deaths_by_year = pd.DataFrame({'male': deaths_by_year_male,'female': 
                               deaths_by_year_female }, index = timespan)
#print(deaths_by_year.head())
#plt.plot(timespan, deaths_by_year.male,'k',timespan, female_scaled, 'r')

# Sort and display the countries with the biggest suicide rate (suicides_no/population)
suicide_over_population = deaths_by_year.merge(world_population, left_index=True, right_index=True)
male_scaled = suicide_over_population.male.divide(suicide_over_population.population)
female_scaled = suicide_over_population.female.divide(suicide_over_population.population)
#plt.plot(timespan,male_scaled,'k',timespan, female_scaled, 'r')
#print(suicide_over_population.head())

# See the suicide distribution across age category
age_distribution = dataset.drop(columns = ['year', 'country'])
age_distribution = age_distribution.dropna()
age_distribution = age_distribution.groupby(by = ['sex','age']).sum()
print(age_distribution)