import pandas as pd
df = pd.read_csv("metal_bands_2017.csv", delimiter =",", index_col=0)
df_clean=df.drop_duplicates()

#Just copying the code from 'metal styles' to be able to look at Suomi
df_new = df_clean.rename(columns={'style': 'genre'})

individual_genres=df_new.genre.str.split(',', expand=True)
individual_genres.columns=['genre_1', 'genre_2', 'genre_3', 'genre_4', 'genre_5', 'genre_6']

list_of_genres=individual_genres.values.tolist()

flattened_list=[y for x in list_of_genres for y in x]
list_no_dupes=list(set(flattened_list))
None_filtered=list(filter(None, list_no_dupes))
genres_per_band=list(filter(None, flattened_list))

#The genre 'Suomi' seems interesting. How many bands are there with this genre?
Suomi_number=genres_per_band.count('Suomi')
print(Suomi_number)
#Bands with genre Suomi (Finnish for 'Finland') - are they all from Finland?
#Pull index of rows where "Suomi" is mentioned in the 'genre' column
print(df_new[df_new['genre']=="Suomi"].index.values)
#This only gives 9 indexes while 'Suomi' is mentioned with 16 rows in total as counted earlier...
#The rest must have more than one genre listed. How do I find those rows so I can check the country of origin?

#Need to do the same with each split columns from earlier..
print(individual_genres[individual_genres['genre_1']=="Suomi"].index.values)
print(individual_genres[individual_genres['genre_2']=="Suomi"].index.values)
print(individual_genres[individual_genres['genre_3']=="Suomi"].index.values)
#16 indexes by 3rd column so no need to search further... Now I need to print the 'origin' column of these specific rows
print(df_new.loc[[308,453,476,767,786,854,1194,1517,1546,1742,2042,3382,200,3407,4017,2716],['band_name','origin']])
#All but one are from Finland!

#How popular are bands with 'Suomi' genre? Who is the most popular?
suomi_bands=df_new.loc[[308,453,476,767,786,854,1194,1517,1546,1742,2042,3382,200,3407,4017,2716]]
suomi_bands_sorted=suomi_bands.sort_values(['fans'], ascending=False)
print(suomi_bands_sorted[['band_name','fans']])

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
g=sns.barplot(x='band_name',
            y='fans',
            data=suomi_bands_sorted)
g.set_title("'Suomi' bands")
g.set(ylabel='Number of fans')
plt.xticks(rotation=90)
plt.show()

#What are the other styles/genres of Finnish bands and how does the fan base of 'Suomi' compare with them? Visualise. -!!!!
finnish_bands=df_new[df_new['origin']=="Finland"]
print(finnish_bands)

#Split style/genre column where many rows list multiple values again just for Finnish bands
finn_individual_genres=finnish_bands.genre.str.split(',', expand=True)
finn_individual_genres.columns=['genre_1', 'genre_2', 'genre_3', 'genre_4', 'genre_5', 'genre_6']

list_of_genres_finn=finn_individual_genres.values.tolist()
flattened_list=[y for x in list_of_genres_finn for y in x]

#filter out None also
flattened_list=list(filter(None, flattened_list))
print(flattened_list)

genre_counts_finn=pd.Series(flattened_list).value_counts()
print(genre_counts_finn)

genre_counts_finn_top20=genre_counts_finn[:20]

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
sns.set_palette("BuPu_r") #change colour to darker? (currently not working) - !!!!
g=sns.barplot(x=genre_counts_finn_top20.index,
              y=genre_counts_finn_top20.values)
g.set_title("Top 20 Finnish Metal Genres")
g.set(xlabel="",
     ylabel="# of bands")
plt.xticks(rotation=90)
plt.show()

#Looks like 'Suomi' is the shared 9/10th most popular genre amongst Finnish bands... Any other similarities and differences detected?(For report)