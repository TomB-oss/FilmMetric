from streamlit_globe import streamlit_globe
from getData import getMoviesInfos
from getData import getLatLong
import streamlit as st
import pandas as pd
import ast


def MovieStatistics():
    st.title("""
    FilmMetric
    """)

    df = getMoviesInfos.getMoviesInfos()

    pointsData, labelsData = getCountryCounts(df)

    st.header("Movie Statistics")

    st.write("""
    *Data from [Kaggle Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download). This data is not up to date*
    """)

    st.divider()

    st.write("""
    Table of Contents
    -----------------
    * [Number of movies per country](#number-of-movies-per-country)
    * [Number of movies per year](#number-of-movies-per-year)
    * [Number of movies per genre](#number-of-movies-per-genre)
    * [Average rating per genre](#average-rating-per-genre)
    """)
    st.divider()

    st.subheader("Number of movies per country")
    streamlit_globe(pointsData=pointsData, labelsData=labelsData,
                    daytime='day', width=800, height=700)

    st.subheader("Number of movies per year")
    year_counts = df["release_date"].str[:4].value_counts()
    df_year_counts = pd.DataFrame(
        {'year': year_counts.index, 'nbMovies': year_counts.values})
    st.bar_chart(df_year_counts, x="year", y="nbMovies")

    st.subheader("Number of movies per genre")
    all_genres = getMoviePerGenre(df)
    df_genres = pd.DataFrame(all_genres)
    st.bar_chart(df_genres, x="genre", y="nbMovies")

    st.subheader("Average rating per genre")
    average_ratings = getAverageRatingPerGenre(df)
    df_average_ratings = pd.DataFrame(
        {'genre': average_ratings.index, 'averageRating': average_ratings.values})
    df_average_ratings = df_average_ratings.sort_values(
        "averageRating", ascending=False)
    for i, df_average_rating in enumerate(df_average_ratings.values, start=1):
        st.write(f"# {i}")
        st.write(f"### {df_average_rating[0]}")
        st.write(f"⭐  {df_average_rating[1]:.2f} / 10")
        st.divider()

@st.cache_data
def getMoviePerGenre(df):
    genre_counts = df["genres"].value_counts()
    all_genres = []

    for i in range(10):
        genre_list = []
        genre_name = genre_counts.index[i]
        nbMovie = genre_counts.iloc[i]

        if (genre_name == "[]"):
            continue

        genre_name_list = ast.literal_eval(genre_name)
        for genre in genre_name_list:
            genre_name = genre.get("name", "N/A")
            genre_list.append({'genre': genre_name, 'nbMovies': nbMovie})
        all_genres.append(genre_list)

    final_list = []

    for genres in all_genres:
        if len(genres) > 1:
            name = ""
            for genre in genres:
                name += genre['genre']
                if genre != genres[-1]:
                    name += ", "
            final_list.append(
                {'genre': name, 'nbMovies': genres[0]['nbMovies']})
        else:
            final_list.append(genres[0])

    return final_list


@st.cache_data
def getAverageRatingPerGenre(df):
    df = df.dropna(subset=["vote_average"])
    df["genres"] = df["genres"].apply(ast.literal_eval)
    df["genres"] = df["genres"].apply(lambda x: [genre['name'] for genre in x])
    df_exploded = df.explode("genres")
    average_ratings = df_exploded.groupby("genres")["vote_average"].mean()
    return average_ratings


@st.cache_data
def getCountryCounts(df):
    country_counts = df["production_countries"].value_counts()

    pointsData = []
    labelsData = []

    for i in range(10):
        country_name = country_counts.index[i]
        nbMovie = country_counts.iloc[i]

        if (country_name == "[]"):
            continue

        countries_name_list = ast.literal_eval(country_name)
        country_name = countries_name_list[0].get("name", "N/A")

        if country_name == "Germany":
            country_name = "Deutschland"
        coordinates = getLatLong.getLatLong(country_name)

        if coordinates:
            pointsData.append(
                {'lat': coordinates[0], 'lng': coordinates[1], 'size': nbMovie / 10000, 'color': 'red'})
            labelsData.append(
                {'lat': coordinates[0], 'lng': coordinates[1], 'size': 0.3, 'color': 'red', 'text': country_name})
        else:
            print("Failed to retrieve coordinates.")

    return pointsData, labelsData


MovieStatistics()
