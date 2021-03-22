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
print(fans_top20[['band_name','origin','fans','style']])

#Scatterplot of Top20 most popular bands and their origin/genre
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid'),
g=sns.relplot(x='band_name',
            y='fans',
            data=fans_top20,
            kind="scatter",
            size="origin",
            hue='origin')
g.fig.suptitle("Top 20 Bands, Fans & Origin")
g.set(ylabel='Number of fans',
      xlabel='')
plt.xticks(rotation=90)
plt.show()
#What can we say about Finnish bands in Top 20? How about others? - For the report.