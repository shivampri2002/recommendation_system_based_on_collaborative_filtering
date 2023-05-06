#Dataframe manipulation library
import pandas as pd
#Math functions, we'll only need the sqrt function so let's import only that
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def main( ):
    #Storing the movie information into a pandas dataframe
    movies_df = pd.read_csv('movies.csv')
    #Storing the user information into a pandas dataframe
    ratings_df = pd.read_csv('ratings.csv')
    
    #let's remove the year from the title column by using pandas' replace function and store it in a new year column.
    
    #Using regular expressions to find a year stored between parentheses
    #We specify the parantheses so we don't conflict with movies that have years in their titles
    movies_df['year'] = movies_df.title.str.extract('(\(\d\d\d\d\))',expand=False)
    #Removing the parentheses
    movies_df['year'] = movies_df.year.str.extract('(\d\d\d\d)',expand=False)
    #Removing the years from the 'title' column
    movies_df['title'] = movies_df.title.str.replace('(\(\d\d\d\d\))', '', regex=True)
    #Applying the strip function to get rid of any ending whitespace characters that may have appeared
    movies_df['title'] = movies_df['title'].apply(lambda x: x.strip())
    
    #let's also drop the genres column since we won't need it for this particular recommendation system.
    
    #Dropping the genres column
    movies_df = movies_df.drop('genres', axis=1)
    
    #We won't be needing the timestamp column in the rating dataframe, so let's drop it to save on memory.
    
    #Drop removes a specified row or column from a dataframe
    ratings_df = ratings_df.drop('timestamp', axis=1)
    
    
