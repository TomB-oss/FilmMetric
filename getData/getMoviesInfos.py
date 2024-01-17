import streamlit as st
import pandas as pd

@st.cache_data
def getMoviesInfos():
    data = pd.read_csv("MoviesDataset/movies_metadata.csv", low_memory=False)

    columns = ["adult", "belongs_to_collection", "budget", "genres", "homepage", "id", "imdb_id", "original_language", "original_title", "overview", "popularity", "poster_path",
               "production_companies", "production_countries", "release_date", "revenue", "runtime", "spoken_languages", "status", "tagline", "title", "video", "vote_average", "vote_count"]

    df = pd.DataFrame(data, columns=columns)

    return df
