# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns = {'Total':'Total_Medals'}, inplace=True)
data.head(10)


# --------------
#Code starts here
#conditions = [data['Total_Summer'] > data['Total_Winter'], data['Total_Summer'] < data['Total_Winter'], data['Total_Summer'] == data['Total_Winter'] ]
#choices = [ 'Summer', 'Winter', 'Both' ]

#data['Better_Event'] = np.select(conditions, choices, default=np.nan)
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'], 'Summer', np.where(data['Total_Summer']<data['Total_Winter'], 'Winter', 'Both'))
better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
top_countries = data.filter(['Country_Name','Total_Summer','Total_Winter','Total_Medals'], axis=1)
top_countries = top_countries.iloc[:len(top_countries)-1,:]

def top_ten(df, col):
    country_list = []
    top_10 = df.nlargest(10, col)
    country_list = top_10['Country_Name']
    return country_list

top_10_summer = list(top_ten(top_countries, 'Total_Summer'))
top_10_winter = list(top_ten(top_countries, 'Total_Winter'))
top_10 = list(top_ten(top_countries, 'Total_Medals'))
print(top_10_summer, top_10_winter, top_10)
common = list(set(top_10_summer).intersection(set(top_10_winter),set(top_10)))
print(common)


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'],align='center', alpha=0.5)
plt.ylabel('Total Medal')
plt.xlabel('Country Name')
plt.xticks(rotation=30)
plt.title('Top 10 Summer') 
plt.show()

plt.bar(summer_df['Country_Name'],summer_df['Total_Winter'],align='center', alpha=0.5)
plt.ylabel('Total Medal')
plt.xlabel('Country Name')
plt.xticks(rotation=30)
plt.title('Top 10 Winter') 
plt.show()

plt.bar(summer_df['Country_Name'],summer_df['Total_Medals'],align='center', alpha=0.5)
plt.ylabel('Total Medal')
plt.xlabel('Country Name')
plt.xticks(rotation=30)
plt.title('Top 10 Total') 
plt.show()


# --------------
#Code starts here


summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = list(summer_df[summer_df['Golden_Ratio']==summer_max_ratio]['Country_Name'])[0]
print(summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = list(winter_df[winter_df['Golden_Ratio']==winter_max_ratio]['Country_Name'])[0]
print(winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = list(top_df[top_df['Golden_Ratio']==top_max_ratio]['Country_Name'])[0]
print(top_country_gold)
#y = top_df[top_df['Golden_Ratio']==top_max_ratio]
#top_country_gold = y.index.value
#print(top_country_gold)


# --------------
#Code starts here
#data.tail()
data_1 = data.iloc[:len(data)-1,:]
#data_1.tail()
data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']
most_points = data_1['Total_Points'].max()
best_country = list(data_1[data_1['Total_Points']==most_points]['Country_Name'])[0]
print(most_points, best_country)


# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best.filter(['Gold_Total','Silver_Total','Bronze_Total'],axis=1)
best.plot(kind='bar', stacked=True, figsize=(15,10))
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


