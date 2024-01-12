import streamlit as st
from getData import getAwardedMovies


def Home():
    st.set_page_config(
        page_title="Movies",
        page_icon="🎬",
    )
    st.write("""
    # Simple Cinema App
    Shown are the **movies** and ***awards*** of the movies!
    """)
    df = getAwardedMovies.getAwardedMovies()
    ################# Show the data #################
    st.write("""
    _____
    """)
    st.write("""
    ## Movies Awarded or Nominated
    """)
    st.write(df)
    ################ Search for a movie ################
    st.write("""
    _____
    """)
    st.write("""
    ### Search for a movie
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
    """)
    search_term = st.text_input('Enter a number of awards')

    st.write("""
    **max** number of awards: 11\n
    **min** number of awards: 1
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
    ################ Search for a movie with awards ################
    st.write("""
    _____
    """)
    st.write("""
    ### Search for movies with more than x awards
    """)
    search_term = st.text_input('Enter a number')

    st.write("""
    **max** number of awards: 11\n
    **min** number of awards: 1
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

Home()
