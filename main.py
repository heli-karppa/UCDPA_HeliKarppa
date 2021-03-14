import pandas as pd
df = pd.read_csv("/Users/heliphant/PycharmProjects/pythonProject6/metal_bands_2017.csv", delimiter =",", index_col=0)

#First founded bands - need to get rid of '-' values - also only need to see band name and founded year
df_2=df.sort_values(['formed'])
print (df_2[['band_name', 'formed']].head(20))

#since only 4 bands with '-' in formed could exclude them by subsetting
print(df_2[['band_name', 'formed']][4:].head(20))

#Most recent bands in the data set?
df_3=df.sort_values(['formed'], ascending=False)
print(df_3[['band_name', 'formed']].head(20))

#What is the first founded Finnish band listed here? How to use .loc here conditionally? Not working yet!
finn_bands=df_2.loc[[:-1],['origin']]
print(finn_bands)

#Number of fans - Most, least, on average
fans=df['fans']
most_fans=max(fans)
print(most_fans)

least_fans=min(fans)
print(least_fans)

print(fans.median())

#How about origin countries?
band_origin_countries=df.origin.unique()
print(band_origin_countries) #Can I make this list alphabetical?

mult_origin=df.origin.str.split(',', expand=True)
mult_origin.columns=['country_1', 'country_2']
print(mult_origin)

#Filtering out rows with 'None' values in country_2 to see only multiple origins
mult_countries = mult_origin.dropna(axis=0, subset=['country_2'])
print(mult_countries)

#Number of bands with 2 origin countries
print(len(mult_countries))

#How many different nations? This should exclude the 36 rows with multiple origins at this stage.
number_origin_countries=df.origin.nunique()
print(number_origin_countries)
minus_multiple=number_origin_countries-36
print(minus_multiple)

#Also need to do the same with bands with multiple origins


#Top 10 countries with metal bands? This is excluding the 36 bands with multiple origins.
bands_per_country=df['origin'].value_counts()
top10 = bands_per_country[:10]
print(top10)

#How do I include data of multi origins? Or should I ignore this?

#Visualisation of Top 10
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette("BuPu_r") #change colour to darker? (currently not working)
g=sns.barplot(x=top10.index, y=top10.values)
g.set_title("Top 10 Number of Bands Per Country")
g.set(xlabel="",
     ylabel="")
plt.xticks(rotation=90)
plt.show()

#Histogram of origin countries
import seaborn as sns
import matplotlib.pyplot as plt

g=sns.countplot(x="origin",
               data=df)
g.set_title("Number of Bands Per Country")
g.set(xlabel="",
     ylabel="") #Axis labels are self explanatory so no need to show them
plt.xticks(rotation=90)
plt.show() #would a scatterplot with dots work better here?


#From Top10, how many Heavy metal bands are there in the Nordics (FI, NO, SE) vs in North America (US, CA)?

#How do Top10 excluded countries in same regions compare with their number of bands? - DK, MX

#In proportion to population of these regions, which has more bands per capita?