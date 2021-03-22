import pandas as pd
df = pd.read_csv("metal_bands_2017.csv", delimiter =",", index_col=0)
print(len(df))

#NEED TO DROP DUPLICATE ROWS!!! Original has 5000 rows, now 4950 so there were 50 duplicates
df_clean=df.drop_duplicates()
print(len(df_clean))

#Let's start with origin countries?
band_origin_countries=df_clean.origin.unique()
print(band_origin_countries)

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


#Top 10 countries with metal bands? This is excluding the 36 bands with multiple origins.
bands_per_country=df_clean['origin'].value_counts()
top10=bands_per_country[:10]
print(top10)

import matplotlib.pyplot as plt
import seaborn as sns
g=sns.barplot(x=top10.index,
              y=top10.values)
g.set_title("Top 10 Number of Bands Per Country")
g.set(xlabel="",
     ylabel="")
plt.xticks(rotation=90)
plt.show()
