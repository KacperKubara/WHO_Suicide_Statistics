import importlib
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
utils = importlib.import_module('utils')

path = '~/Desktop/Machine Learning/Datasets/who_suicide_statistics.csv' 

dataset = utils.get_train_data(path)

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
print(deaths_by_year.head())
deaths_by_year.plot.bar()
# Sort and display the countries with the biggest suicide rate (suicides_no/population)