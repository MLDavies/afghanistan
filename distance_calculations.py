# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 14:29:28 2019

@author: Andrew
"""


############### Calculate Distances for Farah and Ghazni 2018 ################
import pandas as pd
import mpu # (lat, long)

df2018 = pd.read_csv('C:/Users/Andrew/Desktop/Projects/Afghanistan/violence/2018.csv',
                     encoding = 'Latin_1')

# exclude uncertain / nonviolent events
filter_term = ((df2018['Event Type'] == 'Military') | 
        (df2018['Event Type'] == 'Hostile Action') | 
        (df2018['Event Type'] == 'Explosive Hazard')) # create a filter term
df2018 = df2018.loc[filter_term] # filter to above categories

# Fix a problematic variable type
df2018['Latitude'] = df2018['Latitude'].astype('float64')

capitals = pd.read_csv('C:/Users/Andrew/Desktop/Projects/Afghanistan/capitals/capitals.csv')

# Recode Farah to remove the space
df2018['Province'] = df2018['Province'].str.replace('Farah ', 'Farah')

# Filter Farah
df2018 = df2018.loc[df2018['Province'] == 'Farah'].reset_index()
capitals = capitals.loc[capitals['Province'] == 'Farah'].reset_index()

# Calculate Distances

container = []
container2 = []
container3 = []

for i in range(capitals.shape[0]):
    for j in range(df2018.shape[0]):
        if capitals['Province'][i] == df2018['Province'][j]:
            container.append(mpu.haversine_distance((capitals['latitude'][i],
                                                     capitals['longitude'][i]),
                                                     (df2018['Latitude'][j],
                                                     df2018['Longitude'][j])))
            container2.append(df2018['Province'][j])
            container3.append(df2018['Month'][j])

# create df from containers
farah_results = pd.DataFrame({'distance': container, 'province': container2,
                              'month':container3})

# calculate the mean
farah_results = farah_results.groupby('month').mean().reset_index()

# set month order
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
               'September', 'October', 'November', 'December']

# apply month order
farah_results['month'] = pd.Categorical(farah_results['month'], ordered=True, categories=month_order)

# sort df
farah_results = farah_results.sort_values(by='month')

# write to csv for dashboard use
farah_results.to_csv('C:/Users/Andrew/Desktop/farah_distances2018.csv')

###################### Repeat for Ghazni 2018 ###############################
df2018 = pd.read_csv('C:/Users/Andrew/Desktop/Projects/Afghanistan/violence/2018.csv',
                     encoding = 'Latin_1')

# exclude uncertain / nonviolent events
filter_term = ((df2018['Event Type'] == 'Military') | 
        (df2018['Event Type'] == 'Hostile Action') | 
        (df2018['Event Type'] == 'Explosive Hazard')) # create a filter term
df2018 = df2018.loc[filter_term] # filter to above categories

# Fix a problematic variable type
df2018['Latitude'] = df2018['Latitude'].astype('float64')

capitals = pd.read_csv('C:/Users/Andrew/Desktop/Projects/Afghanistan/capitals/capitals.csv')

# Filter Ghazni
df2018 = df2018.loc[df2018['Province'] == 'Ghazni'].reset_index()
capitals = capitals.loc[capitals['Province'] == 'Ghazni'].reset_index()

# Recode a month to remove the space
df2018['Month'] = df2018['Month'].str.replace('December ', 'December')

# Calculate Distances
container = []
container2 = []
container3 = []

for i in range(capitals.shape[0]):
    for j in range(df2018.shape[0]):
        if capitals['Province'][i] == df2018['Province'][j]:
            container.append(mpu.haversine_distance((capitals['latitude'][i],
                                                     capitals['longitude'][i]),
                                                     (df2018['Latitude'][j],
                                                     df2018['Longitude'][j])))
            container2.append(df2018['Province'][j])
            container3.append(df2018['Month'][j])

# create df from containers
ghazni_results = pd.DataFrame({'distance': container, 'province': container2,
                              'month':container3})

# calculate the mean
ghazni_results = ghazni_results.groupby('month').mean().reset_index()

# set month order
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
               'September', 'October', 'November', 'December']

# apply month order
ghazni_results['month'] = pd.Categorical(ghazni_results['month'], ordered=True, categories=month_order)

# sort df
ghazni_results = ghazni_results.sort_values(by='month')

# write to csv for dashboard use
ghazni_results.to_csv('C:/Users/Andrew/Desktop/ghazni_distances2018.csv')



############### Calculate Distances for Farah and Ghazni 2017 ################
import pandas as pd
import mpu # (lat, long)

df2017 = pd.read_csv('C:/Users/Andrew/Desktop/Projects/Afghanistan/violence/2017.csv',
                     encoding = 'Latin_1')

# check categories
df2017['Event Type'].unique()
df2017['Month'].unique()
df2017['Province'].unique()

# Recode Farah to remove the space
df2017['Province'] = df2017['Province'].str.replace('Farah ', 'Farah')

# exclude uncertain / nonviolent events
filter_term = ((df2017['Event Type'] == 'Military') | 
        (df2017['Event Type'] == 'Hostile Action') | 
        (df2017['Event Type'] == 'Explosive Hazard')) # create a filter term
df2017 = df2017.loc[filter_term] # filter to above categories

# Fix a problematic variable type
df2017['Latitude'] = df2017['Latitude'].astype('float64')
df2017['Longitude'] = df2017['Longitude'].astype('float64')

capitals = pd.read_csv('C:/Users/Andrew/Desktop/Projects/Afghanistan/capitals/capitals.csv')

# Filter Farah
df2017 = df2017.loc[df2017['Province'] == 'Farah'].reset_index()
capitals = capitals.loc[capitals['Province'] == 'Farah'].reset_index()

# Recode a month to remove the space
df2017['Month'] = df2017['Month'].str.replace('November ', 'November')

# Calculate Distances
container = []
container2 = []
container3 = []

for i in range(capitals.shape[0]):
    for j in range(df2017.shape[0]):
        if capitals['Province'][i] == df2017['Province'][j]:
            container.append(mpu.haversine_distance((capitals['latitude'][i],
                                                     capitals['longitude'][i]),
                                                     (df2017['Latitude'][j],
                                                     df2017['Longitude'][j])))
            container2.append(df2017['Province'][j])
            container3.append(df2017['Month'][j])

# create df from containers
farah_results = pd.DataFrame({'distance': container, 'province': container2,
                              'month':container3})

# calculate the mean
farah_results = farah_results.groupby('month').mean().reset_index()

# set month order
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
               'September', 'October', 'November', 'December']

# apply month order
farah_results['month'] = pd.Categorical(farah_results['month'], ordered=True, categories=month_order)

# sort df
farah_results = farah_results.sort_values(by='month')

# write to csv for dashboard use
farah_results.to_csv('C:/Users/Andrew/Desktop/farah_distances2017.csv')

###################### Repeat for Ghazni 2017 ###############################
df2017 = pd.read_csv('C:/Users/Andrew/Desktop/Projects/Afghanistan/violence/2017.csv',
                     encoding = 'Latin_1')

# exclude uncertain / nonviolent events
filter_term = ((df2017['Event Type'] == 'Military') | 
        (df2017['Event Type'] == 'Hostile Action') | 
        (df2017['Event Type'] == 'Explosive Hazard')) # create a filter term
df2017 = df2017.loc[filter_term] # filter to above categories

# Fix a problematic variable type
df2017['Latitude'] = df2017['Latitude'].astype('float64')
df2017['Longitude'] = df2017['Longitude'].astype('float64')

capitals = pd.read_csv('C:/Users/Andrew/Desktop/Projects/Afghanistan/capitals/capitals.csv')

# check months
df2017['Month'].unique()

# Recode a month to remove the space
df2017['Month'] = df2017['Month'].str.replace('December ', 'December')
df2017['Month'] = df2017['Month'].str.replace('November ', 'November')

# Filter Ghazni
df2017 = df2017.loc[df2017['Province'] == 'Ghazni'].reset_index()
capitals = capitals.loc[capitals['Province'] == 'Ghazni'].reset_index()

# Calculate Distances
container = []
container2 = []
container3 = []

for i in range(capitals.shape[0]):
    for j in range(df2017.shape[0]):
        if capitals['Province'][i] == df2017['Province'][j]:
            container.append(mpu.haversine_distance((capitals['latitude'][i],
                                                     capitals['longitude'][i]),
                                                     (df2017['Latitude'][j],
                                                     df2017['Longitude'][j])))
            container2.append(df2017['Province'][j])
            container3.append(df2017['Month'][j])

# create df from containers
ghazni_results = pd.DataFrame({'distance': container, 'province': container2,
                              'month':container3})

# calculate the mean
ghazni_results = ghazni_results.groupby('month').mean().reset_index()

# set month order
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
               'September', 'October', 'November', 'December']

# apply month order
ghazni_results['month'] = pd.Categorical(ghazni_results['month'], ordered=True, categories=month_order)

# sort df
ghazni_results = ghazni_results.sort_values(by='month')

# write to csv for dashboard use
ghazni_results.to_csv('C:/Users/Andrew/Desktop/ghazni_distances2017.csv')




############### Calculate Avg. Location for Farah and Ghazni 2018 ################
import pandas as pd

df2018 = pd.read_csv('C:/Users/Andrew/Desktop/Projects/Afghanistan/violence/2018.csv',
                     encoding = 'Latin_1')

# exclude uncertain / nonviolent events
filter_term = ((df2018['Event Type'] == 'Military') | 
        (df2018['Event Type'] == 'Hostile Action') | 
        (df2018['Event Type'] == 'Explosive Hazard')) # create a filter term
df2018 = df2018.loc[filter_term] # filter to above categories

# Fix a problematic variable type
df2018['Latitude'] = df2018['Latitude'].astype('float64')

# Recode Farah to remove the space
df2018['Province'] = df2018['Province'].str.replace('Farah ', 'Farah')

# Filter Farah
df2018 = df2018.loc[df2018['Province'] == 'Farah'].reset_index()


# Calculate Average Location
farah_event_results = df2018.groupby('Month').mean().reset_index()
farah_event_results = farah_event_results[['Month','Latitude', 'Longitude']]

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
               'September', 'October', 'November', 'December']

# apply month order
farah_event_results['Month'] = pd.Categorical(farah_event_results['Month'], ordered=True, categories=month_order)

# sort df
farah_event_results = farah_event_results.sort_values(by='Month')

# write to csv for dashboard use
farah_event_results.to_csv('C:/Users/Andrew/Desktop/farah_event_distances2018.csv')

############ Repeat for Ghazni 2018 #####################
import pandas as pd

df2018 = pd.read_csv('C:/Users/Andrew/Desktop/Projects/Afghanistan/violence/2018.csv',
                     encoding = 'Latin_1')

# exclude uncertain / nonviolent events
filter_term = ((df2018['Event Type'] == 'Military') | 
        (df2018['Event Type'] == 'Hostile Action') | 
        (df2018['Event Type'] == 'Explosive Hazard')) # create a filter term
df2018 = df2018.loc[filter_term] # filter to above categories

# Fix a problematic variable type
df2018['Latitude'] = df2018['Latitude'].astype('float64')

# Filter Ghazni
df2018 = df2018.loc[df2018['Province'] == 'Ghazni'].reset_index()

# Recode a month to remove the space
df2018['Month'] = df2018['Month'].str.replace('December ', 'December')

# Calculate Average Location
ghazni_event_results = df2018.groupby('Month').mean().reset_index()
ghazni_event_results = ghazni_event_results[['Month','Latitude', 'Longitude']]

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
               'September', 'October', 'November', 'December']

# apply month order
ghazni_event_results['Month'] = pd.Categorical(ghazni_event_results['Month'], ordered=True, categories=month_order)

# sort df
ghazni_event_results = ghazni_event_results.sort_values(by='Month')

# write to csv for dashboard use
ghazni_event_results.to_csv('C:/Users/Andrew/Desktop/ghazni_event_distances2018.csv')


############ Repeat for Farah 2017 #####################
df2017 = pd.read_csv('C:/Users/Andrew/Desktop/Projects/Afghanistan/violence/2017.csv',
                     encoding = 'Latin_1')

# exclude uncertain / nonviolent events
filter_term = ((df2017['Event Type'] == 'Military') | 
        (df2017['Event Type'] == 'Hostile Action') | 
        (df2017['Event Type'] == 'Explosive Hazard')) # create a filter term
df2017 = df2017.loc[filter_term] # filter to above categories

# Fix a problematic variable type
df2017['Latitude'] = df2017['Latitude'].astype('float64')
df2017['Longitude'] = df2017['Longitude'].astype('float64')

# Recode Farah to remove the space
df2017['Province'] = df2017['Province'].str.replace('Farah ', 'Farah')

# Recode a month to remove the space
df2017['Month'] = df2017['Month'].str.replace('November ', 'November')

# Filter Farah
df2017 = df2017.loc[df2017['Province'] == 'Farah'].reset_index()


# Calculate Average Location
farah_event_results = df2017.groupby('Month').mean().reset_index()
farah_event_results = farah_event_results[['Month','Latitude', 'Longitude']]

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
               'September', 'October', 'November', 'December']

# apply month order
farah_event_results['Month'] = pd.Categorical(farah_event_results['Month'], ordered=True, categories=month_order)

# sort df
farah_event_results = farah_event_results.sort_values(by='Month')

# write to csv for dashboard use
farah_event_results.to_csv('C:/Users/Andrew/Desktop/farah_event_distances2017.csv')


############ Repeat for Ghazni 2017 #####################
df2017 = pd.read_csv('C:/Users/Andrew/Desktop/Projects/Afghanistan/violence/2017.csv',
                     encoding = 'Latin_1')

# exclude uncertain / nonviolent events
filter_term = ((df2017['Event Type'] == 'Military') | 
        (df2017['Event Type'] == 'Hostile Action') | 
        (df2017['Event Type'] == 'Explosive Hazard')) # create a filter term
df2017 = df2017.loc[filter_term] # filter to above categories

# Fix a problematic variable type
df2017['Latitude'] = df2017['Latitude'].astype('float64')
df2017['Longitude'] = df2017['Longitude'].astype('float64')

# Recode a month to remove the space
df2017['Month'] = df2017['Month'].str.replace('December ', 'December')
df2017['Month'] = df2017['Month'].str.replace('November ', 'November')

# Filter Ghazni
df2017 = df2017.loc[df2017['Province'] == 'Ghazni'].reset_index()


# Calculate Average Location
ghazni_event_results = df2017.groupby('Month').mean().reset_index()
ghazni_event_results = ghazni_event_results[['Month','Latitude', 'Longitude']]

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
               'September', 'October', 'November', 'December']

# apply month order
ghazni_event_results['Month'] = pd.Categorical(ghazni_event_results['Month'], ordered=True, categories=month_order)

# sort df
ghazni_event_results = ghazni_event_results.sort_values(by='Month')

# write to csv for dashboard use
ghazni_event_results.to_csv('C:/Users/Andrew/Desktop/ghazni_event_distances2017.csv')
