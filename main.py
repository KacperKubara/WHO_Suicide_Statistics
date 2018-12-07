import importlib
import pandas as pd 
import numpy as np 
import seaborn as sns
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

# Suicides by gender over the years
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
fig1, ax1 = plt.subplots()
ax1.set_title("Suicides over time")
ax1.set_ylabel("No. Suicides")
ax1.set_xlabel("")
ax1.plot(timespan, deaths_by_year.male,'k',timespan, deaths_by_year.female,'r')


# Suicide distribution across age category
age_distribution = dataset.drop(columns = ['year', 'country', 'population'])
age_distribution = age_distribution.dropna()
age_distribution = age_distribution.groupby(by = ['sex','age'], as_index = False).sum()
age_distribution.reset_index()
age_distribution = age_distribution.reindex(labels = [3,0,1,2,4,5,9,6,7,8,10,11],axis = 0)
# print(age_distribution)
fig2, ax2 = plt.subplots()
ax2.set_title("Suicides over age")
sns.barplot(x = 'age', y = 'suicides_no',hue = 'sex', data = age_distribution, ax = ax2)
ax2.set_ylabel("No. Suicides")
ax2.set_xlabel("")

# Relative Suicide distribution across countries (no. suicides/population)
country_distribution = dataset.drop(columns = ['year','population'])
country_distribution = country_distribution.groupby(by = ['country'], as_index = False).sum().sort_values(by = ['suicides_no'], ascending = False)
fig3, ax3 = plt.subplots()
ax3.set_title("Suicides in countries")
sns.barplot(x = 'country', y = 'suicides_no', data = country_distribution.head(12), ax = ax3)
ax3.set_ylabel("No. Suicides")
ax3.set_xlabel("")