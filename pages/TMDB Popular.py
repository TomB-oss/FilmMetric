import streamlit as st
from getData import getMoviesRating
import numpy as np


def TmdbPopular():
    st.title("""
    FilmMetric
    """)

    st.write('## TMDB Most Popular Movies')
    st.write("""
    *Data from [TMDB Popular](https://www.themoviedb.org/movie)*
    """)

    df = getMoviesRating.getMoviesPopular()
    df.index = np.arange(1, len(df)+1)

    df['ImagePreview'] = df['backdrop_path'].apply(
        lambda x: f'https://image.tmdb.org/t/p/original{x}')

    st.write(df[['title', 'release_date', 'vote_average', 'vote_count']])

    st.write("""
    _____
    """)

    st.write("""
   ## TMDB Popular
    """)

    for i in range(1, len(df) + 1):
        st.write(f"# {i}")

        st.image(df['ImagePreview'][i],
                 caption='Movie Poster', use_column_width=True)
        st.write("""####""", df['title'][i],
                 " (" + df['release_date'][i] + ")")
        st.write(f"⭐ {df['vote_average'][i]} / 10")
        st.write(f"👍 {'{:,}'.format(df['vote_count'][i])}")
        st.write("""
        _____
        """)


TmdbPopular()
