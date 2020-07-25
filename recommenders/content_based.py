"""

    Content-based filtering for item recommendation.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: You are required to extend this baseline algorithm to enable more
    efficient and accurate computation of recommendations.

    !! You must not change the name and signature (arguments) of the
    prediction function, `content_model` !!

    You must however change its contents (i.e. add your own content-based
    filtering algorithm), as well as altering/adding any other functions
    as part of your improvement.

    ---------------------------------------------------------------------

    Description: Provided within this file is a baseline content-based
    filtering algorithm for rating predictions on Movie data.

"""

# Script dependencies
import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Importing data
movies = pd.read_csv('resources/data/movies.csv', sep = ',',delimiter=',')
ratings = pd.read_csv('resources/data/ratings.csv')
movies.dropna(inplace=True)
movieId_features_df = pd.read_csv('https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/recommenders/movieId_features_df.csv')

def data_preprocessing(subset_size):
    """Prepare data for use within Content filtering algorithm.

    Parameters
    ----------
    subset_size : int
        Number of movies to use within the algorithm.

    Returns
    -------
    Pandas Dataframe
        Subset of movies selected for content-based filtering.

    """
    # Split genre data into individual words.
    movies['keyWords'] = movies['genres'].str.replace('|', ' ')
    # Subset of the data
    movies_subset = movies[:subset_size]
    return movies_subset

# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.
def content_model(movie_list,top_n=10):
    """Performs Content filtering based upon a list of movies supplied
       by the app user.

    Parameters
    ----------
    movie_list : list (str)
        Favorite movies chosen by the app user.
    top_n : type
        Number of top recommendations to return to the user.

    Returns
    -------
    list (str)
        Titles of the top-n movie recommendations to the user.

    """

    def content_generate_top_N_recommendations(movie_list, N=10):
        """ Docstring"""
        # Convert the string book title to a numeric index for our
        # similarity matrix
        try:
            all_recommendations=[]
            movie_title = movie_list[0]
            movie_id = movies[movies['title']==movie_title]['movieId'].iloc[0]
            movie_index = movieId_features_df[movieId_features_df['movieId']==movie_id].index[0]
            # Extract all similarity values computed with the reference book title
            sim_scores = list(enumerate(cosine_sim_items[movie_index]))
            # Sort the values, keeping a copy of the original index of each value
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            # Select the top-N values for recommendation
            sim_scores = sim_scores[0:4]
            # Collect indexes
            movie_indices = [i[0] for i in sim_scores]
            all_recommendations.append(list(movies.iloc[movie_indices]['title'].reset_index().drop('index',axis=1)['title']))

            movie_title = movie_list[1]
            movie_id = movies[movies['title']==movie_title]['movieId'].iloc[0]
            movie_index = movieId_features_df[movieId_features_df['movieId']==movie_id].index[0]
            # Extract all similarity values computed with the reference book title
            sim_scores = list(enumerate(cosine_sim_items[movie_index]))
            # Sort the values, keeping a copy of the original index of each value
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            # Select the top-N values for recommendation
            sim_scores = sim_scores[0:3]
            # Collect indexes
            movie_indices = [i[0] for i in sim_scores]
            all_recommendations.append(list(movies.iloc[movie_indices]['title'].reset_index().drop('index',axis=1)['title']))

            movie_title = movie_list[2]
            movie_id = movies[movies['title']==movie_title]['movieId'].iloc[0]
            movie_index = movieId_features_df[movieId_features_df['movieId']==movie_id].index[0]
            # Extract all similarity values computed with the reference book title
            sim_scores = list(enumerate(cosine_sim_items[movie_index]))
            # Sort the values, keeping a copy of the original index of each value
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            # Select the top-N values for recommendation
            sim_scores = sim_scores[0:3]
            # Collect indexes
            movie_indices = [i[0] for i in sim_scores]
            all_recommendations.append(list(movies.iloc[movie_indices]['title'].reset_index().drop('index',axis=1)['title']))
            all_recommendations = [item for sublist in all_recommendations for item in sublist]
            #/Convert the indexes back into titles
            return all_recommendations[:10]
        except IndexError:
            return('movie not in database. Sorry not sorry')
    return content_generate_top_N_recommendations(movie_list, top_n)
