import pandas as pd
df = pd.read_csv("/Users/heliphant/PycharmProjects/pythonProject6/metal_bands_2017.csv", delimiter =",", index_col=0)

#'Style' column name seems to confuse Python so renaming that here with a dictionary value assignment
df_new = df.rename(columns={'style': 'genre'})
print(df_new)

#Split style column where many rows list multiple values
df_new['']=df.index+1
df_new.set_index('').genre.str.split(',', expand=True).stack().reset_index(1, drop=True).reset_index(name='styles')
print(df_new.head())

#What are the styles/genres?
all_genres=df_new.genre.unique()
print(all_genres)

#How many genres are there?
number_genres=df_new.genre.nunique()
print(number_genres)

#Pick 3-5 metal styles and see how popular they are?

#From Top10, how many Heavy metal bands are there in the Nordics (FI, NO, SE) vs in North America (US, CA)?

#How do Top10 excluded countries in same regions compare with their number of bands? - DK, MX

#In proportion to population of these regions, which has more bands per capita?