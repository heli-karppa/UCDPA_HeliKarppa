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


#Visualise with a scatterplot
import matplotlib.pyplot as plt
import seaborn as sns
g=sns.relplot(x='style',
            y='fans',
            data=fans_top20,
            kind="scatter",
            size="origin",
            hue='origin')
g.fig.suptitle("Popularity, Genre & Origin")
g.set(ylabel='Number of fans')
plt.xticks(rotation=90)
plt.show()
#This is OK but the x-ticks get cut off in the middle. How to fix this???

#What has been the fan base progression of Finnish bands over time? Too difficult?
g=sns.relplot(x=df_clean.index[''],
