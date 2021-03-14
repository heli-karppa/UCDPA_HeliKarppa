import pandas as pd
df = pd.read_csv("/Users/heliphant/PycharmProjects/pythonProject6/metal_bands_2017.csv", delimiter =",", index_col=0)
#NEED to change this reference before I submit the project

#'Style' column name seems to confuse Python so renaming that here with a dictionary value assignment
df_new = df.rename(columns={'style': 'genre'})
print(df_new.head())

#Split style column where many rows list multiple values
individual_genres=df_new.genre.str.split(',', expand=True)
individual_genres.columns=['genre_1', 'genre_2', 'genre_3', 'genre_4', 'genre_5', 'genre_6']
print(individual_genres)
#Now this is listing 5 genres for each even if they don't exist. Why? Can I drop the 'None' values?

#Seems so complicated - workaround to do the same as with origin countries...
mult_genres=individual_genres.dropna(axis=0, subset=['genre_2'])
print(mult_genres)
#Still showing the 'None' values and unable to compile a list of unique genres

#How many rows i.e. bands listed under multiple genres
print(len(mult_genres))


#How many genres are there? -1 since 'None' is not a genre
print(individual_genres.nunique()) #Showing the unique values per column
#How can I compare the values in different columns since there could be duplicates?
import numpy as np
column_values=individual_genres[['genre_1', 'genre_2', 'genre_3', 'genre_4', 'genre_5', 'genre_6']].values.ravel()


#Pick 3-5 metal styles and see how popular they are?


#Visualise somehow?
