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

#Visualise
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
g=sns.barplot(x=top10_genres.index,
              y=top10_genres.values)
g.set_title("Top 10 Metal Genres")
g.set(xlabel="",
     ylabel="# of bands")
plt.xticks(rotation=90)
plt.show()
