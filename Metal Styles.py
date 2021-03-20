import pandas as pd
df = pd.read_csv("metal_bands_2017.csv", delimiter =",", index_col=0)
df_clean=df.drop_duplicates()

#'Style' column name seems to confuse Python so renaming that here with a dictionary value assignment
df_new = df_clean.rename(columns={'style': 'genre'})
print(df_new.head())

#Split style/genre column where many rows list multiple values
individual_genres=df_new.genre.str.split(',', expand=True)
individual_genres.columns=['genre_1', 'genre_2', 'genre_3', 'genre_4', 'genre_5', 'genre_6']
print(individual_genres)
#Now this is listing 5 genres for each even if they don't exist. Why? Can I drop the 'None' values?

#Merge column values into a list?
list_of_genres=individual_genres.values.tolist()
#Now this is a list of lists - I want one flat list of all so easier to drop duplicates and 'None'
flattened_list=[y for x in list_of_genres for y in x]

#Drop duplicates - using this set() function because the index doesn't matter here - we just want unique values
list_no_dupes=list(set(flattened_list))
print(list_no_dupes)
#filter out None also?
None_filtered=list(filter(None, list_no_dupes))
print(None_filtered)

#How many genres are there?
print(len(None_filtered))

#What are the top10 genres?
#First filter out just 'None' from original flat list. We want to keep the duplicates.
genres_per_band=list(filter(None, flattened_list))
#Lets use pandas series to pull the value counts again...
genre_counts=pd.Series(genres_per_band).value_counts()
top10_genres=genre_counts[:10]
print(top10_genres)

#Visualise somehow? Another bar plot probably best.
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette("BuPu_r") #change colour to darker? (currently not working) - !!!!
g=sns.barplot(x=top10_genres.index, y=top10_genres.values)
g.set_title("Top 10 Metal Genres")
g.set(xlabel="",
     ylabel="# of bands")
plt.xticks(rotation=90)
plt.show()

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

#How popular are bands with 'Suomi' genre? Who is the most popular? Visualise. - !!!!
suomi_bands=df_new.loc[[308,453,476,767,786,854,1194,1517,1546,1742,2042,3382,200,3407,4017,2716]]
print(suomi_bands[['band_name','fans']])

#What are the other styles/genres of Finnish bands and how does the fan base of 'Suomi' compare with them? Visualise. -!!!!


