import pandas as pd
df = pd.read_csv("metal_bands_2017.csv", delimiter =",", index_col=0)

#NEED TO DROP DUPLICATE ROWS!!! Original has 5000 rows, now 4950 so there were 50 duplicates
df_clean=df.drop_duplicates()
print(df_clean)

#Let's start with origin countries?
band_origin_countries=df_clean.origin.unique()
print(band_origin_countries) #Can I make this list alphabetical?

mult_origin=df_clean.origin.str.split(',', expand=True)
mult_origin.columns=['country_1', 'country_2']
print(mult_origin)

#Filtering out rows with 'None' values in country_2 to see only multiple origins
mult_countries = mult_origin.dropna(axis=0, subset=['country_2'])
print(mult_countries)

#Number of bands with 2 origin countries
print(len(mult_countries))

#How many different nations? This should exclude the 36 rows with multiple origins at this stage.
number_origin_countries=df_clean.origin.nunique()
print(number_origin_countries)
minus_multiple=number_origin_countries-36
print(minus_multiple)

#Also need to do the same with bands with multiple origins


#Top 10 countries with metal bands? This is excluding the 36 bands with multiple origins.
bands_per_country=df_clean['origin'].value_counts()
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

#From Top10, how many Heavy metal bands are there in the Nordics (FI, NO, SE) vs in North America (US, CA)?
#Form a dictionary from counted values earlier and count?


#In proportion to population of these regions, which has more bands per capita?


