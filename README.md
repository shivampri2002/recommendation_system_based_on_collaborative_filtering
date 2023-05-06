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
                
                
