import pandas as pd

#Lets sort only Finnish bands into a data frame
data = pd.read_csv("metal_bands_2017.csv", index_col ="origin")
finn_bands=data.loc["Finland"]
#Indexed bands my origin and pulling only those with Finland
#Which are the first Finnish Bands?
sorted_finn=finn_bands.sort_values(['formed'])
print(sorted_finn[['band_name','formed']].head())

df = pd.read_csv("metal_bands_2017.csv", delimiter =",", index_col=0)
df_clean=df.drop_duplicates()
#How many active bands overall in 2016?
active_bands=df_clean.loc[df_clean['split']=='-']
print(len(active_bands))
#Percentage wise?
all_bands=len(df_clean)
active_bands_number=len(active_bands)
active_bands_per=active_bands_number/all_bands
print(active_bands_per)

#How many Finnish bands were still active in 2016? In the CSV open split date marked with a dash so we want these rows selected.
active_finn_bands=finn_bands.loc[finn_bands['split']=='-']
print(len(active_finn_bands))
#Percentage to compare?
all_finn_bands=len(finn_bands)
active_finn_number=len(active_finn_bands)
active_finn_bands_per=active_finn_number/all_finn_bands
print(active_finn_bands_per)

#And how many and which Finnish bands had broken up by 2016? We want to exclude the rows with a dash in the split column.
split_finn_bands=finn_bands.loc[finn_bands['split']!='-']
print(split_finn_bands[['band_name', 'split']])
print(len(split_finn_bands))
#Some of this data like Nightwish doesn't look correct so one could question the quality of this data?
#Percentage?
split_finn_bands_number=len(split_finn_bands)
split_finn_bands_per=split_finn_bands_number/all_finn_bands
print(split_finn_bands_per)
#60.6% Finnish bands had split so slightly more than average

#How many bands were overall broken up by 2016?
split_bands=df_clean.loc[df_clean['split']!='-']
print(len(split_bands))
#Percentage wise?
all_bands=len(df_clean)
split_bands_number=len(split_bands)
split_bands_per=split_bands_number/all_bands
print(split_bands_per)
#55.7 % of bands have split overall