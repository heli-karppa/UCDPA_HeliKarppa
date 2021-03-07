import pandas as pd
import numpy as np
df = pd.read_csv("/Users/heliphant/PycharmProjects/pythonProject6/metal_bands_2017.csv", delimiter =",", index_col=0)
print(df.head(20))

fans=df['fans']
most_fans=fans.max()
print(most_fans)

least_fans=fans.min()
print(least_fans)
print(fans.median())

band_origin_countries=df.origin.unique()
print(band_origin_countries) #Can I make this list alphabetical? Listing same countries multiple times, why? Bands from two different countries!

number_origin_countries=df.origin.nunique()
print(number_origin_countries) #How can I filter out multiple country combinations? Some link of conditional loop needed?

df=df.sort_values(['formed'])
print (df.head(20))  #how to get the sort function to work here?

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
