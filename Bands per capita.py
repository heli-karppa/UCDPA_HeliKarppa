#Just copying the start/needed code from main
import pandas as pd
df = pd.read_csv("metal_bands_2017.csv", delimiter =",", index_col=0)
print(len(df))

df_clean=df.drop_duplicates()

bands_per_country=df_clean['origin'].value_counts()
top10=bands_per_country[:10]
print(top10)

#Bring in second CSV world populations so we can compare band counts and population in 2015

df_populations=pd.read_csv("world_population_1960_2015.csv", delimiter =",", index_col=0)
df_pop_2015=df_populations['2015']

#Indexing/locating Top 10 countries with most metal bands from before - Noticing that country name is actually the index in this CSV
top10_pop=df_pop_2015.loc[['United States', 'Sweden', 'Germany', 'United Kingdom','Finland','France','Norway','Italy','Canada','Netherlands']]

#Need to rename index values for United States and Netherlands so that they match the main CSV format
top10_pop_new=top10_pop.rename(index={'United States': 'USA', 'Netherlands':'The Netherlands'})
print(top10_pop_new)

#Per capita = measurement/number of people in a population
per_capita=top10/top10_pop_new
print(per_capita)

#Visualise - put two bar plots side by side? -!!!!
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette("BuPu_r") #play with this more?
g=sns.catplot(x=top10.index,
              y=top10.values)
g.set_title("Top 10 Number of Bands Per Country")
g.set(xlabel="",
     ylabel="")
plt.xticks(rotation=90)
plt.show()