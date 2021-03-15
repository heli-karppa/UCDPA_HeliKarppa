import pandas as pd
df = pd.read_csv("metal_bands_2017.csv", delimiter =",", index_col=0)
df_clean=df.drop_duplicates()

#Number of fans - Most, least, on average
fans=df_clean['fans']
most_fans=max(fans)
print(most_fans)

least_fans=min(fans)
print(least_fans)

print(fans.median())

#Or where do bands with a lot of fans tend to be from? Say top20 countries with most fans and their country of origin.

fans_descending=df_clean.sort_values(['fans'], ascending=False)
fans_top20=fans_descending[:20]
print(fans_top20[['band_name','origin','fans']])

#How can I pull counts of fans per the country of origin of a band?
fans_country_alphabetical=df_clean.sort_values(['origin'])
print(fans_country_alphabetical[['band_name', 'origin','fans']])

#Still need to calculate by origin....


#Visualise with a scatterplot?
import matplotlib.pyplot as plt
import seaborn as sns
sns.relplot(x='origin', y='fans',
            data=fans_top20,
            kind="scatter",
            size="fans")
plt.show()