import pandas as pd
df = pd.read_csv("metal_bands_2017.csv", delimiter =",", index_col=0)
df_clean=df.drop_duplicates()

#First founded bands - need to get rid of '-' values - also only need to see band name and founded year
df_2=df_clean.sort_values(['formed'])
print (df_2[['band_name', 'formed']].head(20))

#since only 4 bands with '-' in formed could exclude them by subsetting
print(df_2[['band_name', 'formed']][4:].head(20))

#Most recent bands in the data set?
df_3=df_clean.sort_values(['formed'], ascending=False)
print(df_3[['band_name', 'formed']].head(20))

#How to look at split years?



#What are the first five founded Finnish bands listed? How to use .loc here?
data = pd.read_csv("metal_bands_2017.csv", index_col ="origin")
finn_bands=data.loc["Finland"]
#Indexed bands my origin and pulling only those with Finland
#Now need to sort this by founded year...
sorted_finn=finn_bands.sort_values(['formed'])
print(sorted_finn[['band_name','formed']].head())