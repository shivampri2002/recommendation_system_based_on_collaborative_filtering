#Dataframe manipulation library
import pandas as pd
#Math functions, we'll only need the sqrt function so let's import only that
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def userInputFunc( ):
    userInput = [
            {'title':'Breakfast Club, The', 'rating':5},
            {'title':'Toy Story', 'rating':3.5},
            {'title':'Jumanji', 'rating':2},
            {'title':"Pulp Fiction", 'rating':5},
            {'title':'Akira', 'rating':4.5}
         ]
    return userInput

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
    
    #taking user input
    userInput = userInputFunc( )
    inputMovies = pd.DataFrame(userInput)
    
    #let's extract the input movies's ID's from the movies dataframe and add them into it.
    
    #Filtering out the movies by title
    inputId = movies_df[movies_df['title'].isin(inputMovies['title'].tolist())]
    #Then merging it so we can get the movieId. It's implicitly merging it by title.
    inputMovies = pd.merge(inputId, inputMovies)
    #Dropping information we won't use from the input dataframe
    inputMovies = inputMovies.drop('year', 1)
    
    #Filtering out users that have watched movies that the input has watched and storing it
    userSubset = ratings_df[ratings_df['movieId'].isin(inputMovies['movieId'].tolist())]
    
    #let us now group up the rows by user ID.
    
    #Groupby creates several sub dataframes where they all have the same value in the column specified as the parameter
    userSubsetGroup = userSubset.groupby(['userId'])
    
    #let's also sort these groups so the users that share the most movies in common with the input have higher priority. This provides a richer recommendation since we won't go through every single user.
    
    #Sorting it so users with movie most in common with the input will have priority
    userSubsetGroup = sorted(userSubsetGroup,  key=lambda x: len(x[1]), reverse=True)
    
    #let us select a subset of users to iterate through. This limit is imposed because we don't want to waste too much time going through every single user.
    userSubsetGroup = userSubsetGroup[0:100]
    
    #let us calculate the Pearson Correlation between input user and subset group, and store it in a dictionary, where the key is the user Id and the value is the coefficient.

    #Store the Pearson Correlation in a dictionary, where the key is the user Id and the value is the coefficient
    pearsonCorrelationDict = {}

    #For every user group in our subset
    for name, group in userSubsetGroup:
        #Let's start by sorting the input and current user group so the values aren't mixed up later on
        group = group.sort_values(by='movieId')
        inputMovies = inputMovies.sort_values(by='movieId')
        #Get the N for the formula
        nRatings = len(group)
        #Get the review scores for the movies that they both have in common
        temp_df = inputMovies[inputMovies['movieId'].isin(group['movieId'].tolist())]
        #And then store them in a temporary buffer variable in a list format to facilitate future calculations
        tempRatingList = temp_df['rating'].tolist()
        #Let's also put the current user group reviews in a list format
        tempGroupList = group['rating'].tolist()
        #sum variable
        sm_trl = sum(tempRatingList)
        sm_tgl = sum(tempGroupList)
        #Now let's calculate the pearson correlation between two users, so called, x and y
        Sxx = sum([i**2 for i in tempRatingList]) - pow(sm_trl,2)/float(nRatings)
        Syy = sum([i**2 for i in tempGroupList]) - pow(sm_tgl,2)/float(nRatings)
        Sxy = sum( i*j for i, j in zip(tempRatingList, tempGroupList)) - sm_trl*sm_tgl/float(nRatings)

        #If the denominator is different than zero, then divide, else, 0 correlation.
        if Sxx != 0 and Syy != 0:
            pearsonCorrelationDict[name] = Sxy/sqrt(Sxx*Syy)
        else:
            pearsonCorrelationDict[name] = 0
            
    pearsonDF = pd.DataFrame.from_dict(pearsonCorrelationDict, orient='index')
    pearsonDF.columns = ['similarityIndex']
    pearsonDF['userId'] = pearsonDF.index
    pearsonDF.index = range(len(pearsonDF))
    
    #let's get the top 50 users that are most similar to the input.
    topUsers=pearsonDF.sort_values(by='similarityIndex', ascending=False)[0:50]
    
    #let us get the movies watched by the users in our pearsonDF from the ratings dataframe and then store their correlation in a new column called _similarityIndex". This is achieved below by merging of these two tables. 
    topUsersRating=topUsers.merge(ratings_df, left_on='userId', right_on='userId', how='inner')
    
    #let us  multiply the movie rating by its weight (the similarity index), then sum up the new ratings and divide it by the sum of the weights.
    
    #Multiplies the similarity by the user's ratings
    topUsersRating['weightedRating'] = topUsersRating['similarityIndex']*topUsersRating['rating']
    
    #Applies a sum to the topUsers after grouping it up by userId
    tempTopUsersRating = topUsersRating.groupby('movieId').sum()[['similarityIndex','weightedRating']]
    tempTopUsersRating.columns = ['sum_similarityIndex','sum_weightedRating']
    
    #Creates an empty dataframe
    recommendation_df = pd.DataFrame()
    #Now we take the weighted average
    recommendation_df['weighted average recommendation score'] = tempTopUsersRating['sum_weightedRating']/tempTopUsersRating['sum_similarityIndex']
    recommendation_df['movieId'] = tempTopUsersRating.index
    
    #let's sort it and see the top 20 movies that the algorithm recommended.
    recommendation_df = recommendation_df.sort_values(by='weighted average recommendation score', ascending=False)
    
    recommended_10_movies_df = movies_df.loc[movies_df['movieId'].isin(recommendation_df.head(10)['movieId'].tolist())]
    
    print(recommended_10_movies_df)
    
    
    
if __name__ == "__main__":
    main( )
