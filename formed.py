import pandas as pd
df = pd.read_csv("metal_bands_2017.csv", delimiter =",", index_col=0)
df_clean=df.drop_duplicates()

#First founded bands - need to get rid of '-' values - also only need to see band name and founded year
df_2=df_clean.sort_values(['formed'])
print (df_2[['band_name', 'formed']].head(20))

#since only 4 bands with '-' in formed could exclude them by slicing
print(df_2[['band_name', 'formed']][4:].head(20))

#I want to know who Alice Cooper are...
import requests
url='http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=Alice+Cooper&api_key=aebdf03f0dcc6a8eb89a00bdafcb4bea&format=json'
r=requests.get(url)
json_data=r.json()
for key, value in json_data.items():
    print(key+':', value)
#This is the artist summary from LastFM API. Looks like he was still active in 2017 at least.

#Number of bands - need to count by year formed...
a = list(df_clean['formed'].to_dict().values()) #moving the formed years as values to a dictionary
bands_by_year_counts={i:a.count(i) for i in a if '-' not in i} #Counting values in 'a' as long as they are not '-'
year_df_formed = pd.DataFrame()
year_df_formed['band_counts']=pd.Series(bands_by_year_counts)
#Again need to sort this to be in linear order of years
sorted_year_df_formed=year_df_formed.sort_index()
print(sorted_year_df_formed)

#Visualise...
import matplotlib.pyplot as plt
import seaborn as sns
g=sns.relplot(x=sorted_year_df_formed.index,
            y ='band_counts',
            data=sorted_year_df_formed,
            kind="line")
g.fig.suptitle("Number of Bands Formed 1964-2016")
g.set(xlabel='',
      ylabel='Band Count')
plt.xticks(rotation=90)
plt.show()