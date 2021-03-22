import pandas as pd
#What are the first five founded Finnish bands listed?
data = pd.read_csv("metal_bands_2017.csv", index_col ="origin")
finn_bands=data.loc["Finland"]
#Indexed bands my origin and pulling only those with Finland
#Now need to sort this by founded year...
sorted_finn=finn_bands.sort_values(['formed'])
print(sorted_finn[['band_name','formed']].head())

#How many Finnish bands were still active in 2016? In the CSV open split date marked with a dash so we want these rows selected.
active_finn_bands=finn_bands.loc[finn_bands['split']=='-']
print(len(active_finn_bands))
#And how many and which Finnish bands had broken up by 2016? We want to exclude the rows with a dash in the split column.
split_finn_bands=finn_bands.loc[finn_bands['split']!='-']
print(split_finn_bands[['band_name', 'split']])
print(len(split_finn_bands))
#Some of this data like Nightwish doesn't look correct so one could question the quality of this data?

a = list(sorted_finn['formed'].to_dict().values()) #moving the formed years as values to a dictionary
bands_by_year_counts_split_finn={i:a.count(i) for i in a if '-' not in i} #Counting values in 'a' as long as they are not '-'
year_df_split_finn=pd.DataFrame()
year_df_split_finn['band_counts']=pd.Series(bands_by_year_counts_split_finn)
#Again need to sort this to be in linear order of years
sorted_year_df_split_finn=year_df_split_finn.sort_index()
print(sorted_year_df_split_finn)

import matplotlib.pyplot as plt
import seaborn as sns
g=sns.relplot(x=sorted_year_df_split_finn.index,
            y ='band_counts',
            data=sorted_year_df_split_finn,
            kind="line")
g.fig.suptitle("Finnish Bands Split 1964-2016")
g.set(xlabel='',
      ylabel='Band Count')
plt.xticks(rotation=90)
plt.show()