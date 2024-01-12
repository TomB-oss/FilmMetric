import streamlit as st
from getData import getDataImdbRating


def ImdbMostRated():
    st.write("""
    # Simple Cinema App
    Shown are the **movies** and ***awards*** of the movies!
    """)
    st.title('IMDb Most People Rating')

    df = getDataImdbRating.getRatingByNumberOfRates()
    df['ImagePreview'] = df['ImageURL'].apply(
        lambda x: f'<img src="{x}" alt="Image" width="100">')

    st.write(df[['Title', 'Year', 'Rating', 'Votes']])

    st.write("""
   ## Movies with their IMDb Most People Rating
    """)

    for i in range(len(df)):
        st.write(df['ImagePreview'][i], unsafe_allow_html=True)
        st.write("""####""", df['Title'][i], " (" + df['Year'][i] + ")")
        st.write("⭐", df['Rating'][i] + "/10")
        st.write("👍", df['Votes'][i])
        st.write("""
        _____
        """)


ImdbMostRated()
