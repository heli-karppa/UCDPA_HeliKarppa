import pandas as pd
df = pd.read_csv("metal_bands_2017.csv", delimiter =",", index_col=0)
df_clean=df.drop_duplicates()

a = list(df_clean['split'].to_dict().values()) #moving the formed years as values to a dictionary
bands_by_year_counts_split={i:a.count(i) for i in a if '-' not in i} #Counting values in 'a' as long as they are not '-'
year_df_split = pd.DataFrame()
year_df_split['band_counts']=pd.Series(bands_by_year_counts_split)
#Again need to sort this to be in linear order of years
sorted_year_df_split=year_df_split.sort_index()
print(sorted_year_df_split)

import matplotlib.pyplot as plt
import seaborn as sns
g=sns.relplot(x=sorted_year_df_split.index,
            y ='band_counts',
            data=sorted_year_df_split,
            kind="line")
g.fig.suptitle("Number of Bands Split 1964-2016")
g.set(xlabel='',
      ylabel='Band Count')
plt.xticks(rotation=90)
plt.show()

