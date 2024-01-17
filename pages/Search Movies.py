import streamlit as st
from getData import getAwardedMovies
import numpy as np


def searchMovies():

    st.title("""
    FilmMetric
    """)
    st.write("""
    Shown are the **movies** and ***awards*** of the movies!
    """)

    df = getAwardedMovies.getAwardedMovies()
    df.index = np.arange(1, len(df)+1)

    ################ Search for a movie ################
    st.write("""
    _____
    """)
    st.write("""
    ### Search for a movie
    *Data from [Wikipedia](https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films)*

    """)
    search_term = st.text_input('Enter a movie name')
    st.write("""
    ### Movie Details
    """)
    st.write(df[df['Film'].str.contains(search_term, case=False)])

    ################ Search for a movie with awards ################
    st.write("""
    _____
    """)
    st.write("""
    ### Search for movies with awards
    *Data from [Wikipedia](https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films)*
    """)
    search_term = st.text_input('Enter a number of awards')

    st.write("""
    number **max** of awards: 11\n
    number **min** of awards: 1
    """)
    st.write("""
    ### Movie Details
    """)
    if search_term == "":
        search_term = -1
    search_term = int(search_term)
    if search_term > 11:
        st.write("Enter a number between 1 and 11")
    st.write(df[df['Awards'] == search_term])

    ################ Search for a movie with more than X awards ################
    st.write("""
    _____
    """)
    st.write("""
    ### Search for movies with more than X awards
    *Data from [Wikipedia](https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films)*
    """)
    search_term = st.text_input('Enter a number')

    st.write("""
    number **max** of awards: 11\n
    number **min** of awards: 1
    """)
    st.write("""
    ### Movie Details
    """)
    if search_term == "":
        search_term = -1
    search_term = int(search_term)
    if search_term > 11:
        st.write("Enter a number between 1 and 11")

    st.write(df[df['Awards'] >= search_term])


searchMovies()
