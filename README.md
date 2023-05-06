# Recommendation_System_Based_On_Collaborative_Filtering
A simple recommendation system based on collaborative filtering technique
<br></br>
<br></br>
In modern applications like e-commerce platforms and movie streaming sites, Recommendation Systems play a vital role. These systems utilize previous viewer reviews and user preferences to provide users with enhanced choices and personalized recommendations.

We have built a simple version of Recommendation System based on Collaborative filtering technqiue using Python and Pandas library.

Dataset is acquired from [GroupLens](https://grouplens.org/datasets/movielens/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkML0101ENSkillsNetwork1047-2022-01-01). 
To download the data, we will use `!wget` command.
Downloading and unzipping the dataset:
```
!wget -O moviedataset.zip https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%205/data/moviedataset.zip
print('unziping ...')
!unzip -o -j moviedataset.zip 
```

### Information about the dataset
Zipped dataset folder:  moviedataset.zip    </br>
Files contained in this folder:
1. links.csv 
2. movies.csv
3. ratings.csv
4. README.txt
5. tags.csv

Data were created by 247753 users between January 09, 1995 and January 29, 2016 on the [MovieLens](http://movielens.org) website. All selected users had rated at least 1 movies and  each user is represented by an id.

**Ratings Data File Structure (ratings.csv)**   </br>
The lines within this file are ordered first by userId, then, within user, by movieId.   </br>
Each line of this file after the header row:    </br>
>              userId,movieId,rating,timestamp
              
**Tags Data File Structure (tags.csv)**   </br>
Tags are user-generated metadata about movies.    </br>
>               userId,movieId,tag,timestamp
                
**Movies Data File Structure (movies.csv)**   </br>
Genres are a pipe-separated list.   </br>
>                movieId,title,genres

**Links Data File Structure (links.csv)**     </br>
movieId is an identifier for movies used by <https://movielens.org>. imdbId is an identifier for movies used by <http://www.imdb.com>. tmdbId is an identifier for movies used by <https://www.themoviedb.org>.   </br>
>               movieId,imdbId,tmdbId
                
                

### Packages used in this program:
```
pip install matplotlib pandas numpy
```

## Details about filtering method used in this program:
Collaborative Filtering( also known as User-User Filtering) technique uses other users data to recommend items to the input user. It attempts to find users that have similar preferences and opinions as the input and then recommends items that they have liked to the input. The method one we will be using here is going to be based on the `Pearson Correlation Function`.

![Image of description of filtering method](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%205/images/User_Item.png)

The process for creating a User Based recommendation system is as follows:
1. Select a user with the movies the user has watched
2. Based on his rating of the movies, find the top X neighbours
3. Get the watched movie record of the user for each neighbour
4. Calculate a similarity score using some formula
5. Recommend the items with the highest score
</br>
We are going to compare all users (not really all !!!) to our specified user and find the one that is most similar.
We're going to find out how similar each user is to the input through the Pearson Correlation Coefficient. It is used to measure the strength of a linear association between the two variables. 
</br>
**Pearson correlation** is invariant to scaling, i.e. multiplying all elements by a nonzero constant or adding any constant to all elements. This is a pretty important property in recommendation systems because, for example, two users might rate two series of items totally differently in terms of absolute rates, but they would be similar users (i.e. with similar ideas) with similar rates in various scales. 

![Corrlation coefficinet formaula image](https://editor.analyticsvidhya.com/uploads/39170Formula.JPG)

The values given by the formula vary from r = -1 to r = 1, where 1 forms a direct correlation between the two entities (it means a perfect positive correlation) and -1 forms a perfect negative correlation. In our case, a 1 means that the two users have similar tastes while a -1 means the opposite.
</br>

## Advantages and Disadvantages of Collaborative Filtering
### Advantages
* Takes other user's ratings into consideration
* Doesn't need to study or extract information from the recommended item
* Adapts to the user's interests which might change over time
### Disadvantages
* Approximation function can be slow
* There might be a low amount of users to approximate
* Privacy issues when trying to learn the user's preferences
