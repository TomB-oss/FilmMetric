import streamlit as st
from getData import getAwardedMovies
import numpy as np


def Home():
    st.set_page_config(
        page_title="Movies",
        page_icon="🎬",
    )
    st.title("""
    FilmMetric
    """)

    st.write("""
    Shown are the **movies** and ***awards*** of the movies!
    """)
    df = getAwardedMovies.getAwardedMovies()
    df.index = np.arange(1, len(df)+1)

    ################# Show the data #################
    st.write("""
    _____
    """)
    st.write("""
    ## Movies Awarded or Nominated
    *Data from [Wikipedia](https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films)*
    """)
    st.write(df)


Home()
