import pandas as pd
import numpy as np
df = pd.read_csv("/Users/heliphant/PycharmProjects/pythonProject6/metal_bands_2017.csv", delimiter =",", index_col=0)

#First founded bands - need to get rid of '-' values - also only need to see band name and founded year
df_2=df.sort_values(['formed'])
print (df_2.head(20))

#Number of fans - Most, least, on average
fans=df['fans']
most_fans=max(fans)
print(most_fans)

least_fans=min(fans)
print(least_fans)

print(fans.median())

band_origin_countries=df.origin.unique()
print(band_origin_countries) #Can I make this list alphabetical? Listing same countries multiple times, why? Bands from two different countries!

#How many different nations?
number_origin_countries=df.origin.nunique()
print(number_origin_countries) #How can I filter out multiple country combinations?




#Top 10 countries with metal bands?
bands_per_country=df['origin'].value_counts()
top10 = bands_per_country[:10]
print(top10)

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


