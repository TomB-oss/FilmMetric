import streamlit as st
import pandas as pd
import requests

import dotenv
import os


@st.cache_data
def getMoviesRating():
    dotenv.load_dotenv()
    API_KEY = os.getenv("API_KEY")

    pageNb = 1

    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer ' + API_KEY}

    for i in range(5):
        url = 'https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=' + \
            str(pageNb + i)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            movie_data = response.json()
            if i == 0:
                df = pd.DataFrame(movie_data['results'])
            else:
                df = pd.concat([df, pd.DataFrame(
                    movie_data['results'])], ignore_index=True)

        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
    return df


@st.cache_data
def getMoviesPopular():
    dotenv.load_dotenv()
    API_KEY = os.getenv("API_KEY")

    pageNb = 1

    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer ' + API_KEY}

    for i in range(5):
        url = 'https://api.themoviedb.org/3/movie/popular?language=en-US&page=' + \
            str(pageNb + i)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            movie_data = response.json()
            if i == 0:
                df = pd.DataFrame(movie_data['results'])
            else:
                df = pd.concat([df, pd.DataFrame(
                    movie_data['results'])], ignore_index=True)
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
    return df
