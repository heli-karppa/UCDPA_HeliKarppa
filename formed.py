import pandas as pd
df = pd.read_csv("metal_bands_2017.csv", delimiter =",", index_col=0)
df_clean=df.drop_duplicates()

#First founded bands - need to get rid of '-' values - also only need to see band name and founded year
df_2=df_clean.sort_values(['formed'])
print (df_2[['band_name', 'formed']].head(20))

#since only 4 bands with '-' in formed could exclude them by subsetting
print(df_2[['band_name', 'formed']][4:].head(20))

#Most recent bands in the data set?
df_3=df_clean.sort_values(['formed'], ascending=False)
print(df_3[['band_name', 'formed']].head(20))

#Does the first formed artist/band Alice Cooper still get mentions? Data from LastFM API
# !!! API OR WEB SCRAPING? Could I pull some Finland related data from the web like what?!
import json
import requests
url="http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=alice_cooper&api_key=YOUR_API_KEY&format=json"



#What are the first five founded Finnish bands listed?
data = pd.read_csv("metal_bands_2017.csv", index_col ="origin")
finn_bands=data.loc["Finland"]
#Indexed bands my origin and pulling only those with Finland
#Now need to sort this by founded year...
sorted_finn=finn_bands.sort_values(['formed'])
print(sorted_finn[['band_name','formed']].head())

#Number of bands - need to count by year formed...
a = list(df_clean['formed'].to_dict().values())
bands_by_year_counts={i:a.count(i) for i in a if '-' not in i}
year_df = pd.DataFrame()
year_df['band_counts']=pd.Series(bands_by_year_counts)
print(year_df)

#Need to give year column a name... - unable to define 'x' below... - !!!!
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
g=sns.relplot(x=year_df.index,
            y ='band_counts',
            data=year_df,
            kind="line")
g.fig.suptitle("Number of Bands Formed Through Time")
g.set(xlabel='Year',
      ylabel='Band Count')
plt.xticks(rotation=30)
plt.show()
#Can I stretch the x-axis?
#Plot works but need to modify? years on x-axis only in 5-year intervals?
#Needs to be in linear time order... now is not. -!!!!