import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('topMusicJOB.csv', index_col = 0)

df.rename({'Unnamed: 0' : 'id', 'top genre': 'genre'}, axis=1, inplace=True)

header = st.container()
sliders = st.container()
plot = st.container()
setlist = st.container()
counters = st.container()

with header:
    st.title('Setlist Generator')

with sliders:
    st.header('What kind of playlist are you going to create?')

    st.subheader('Mood')
    mood = st.slider("100 is happy mood", 0, 100)

    st.subheader('Danceabilty')
    danceability = st.slider("100 is very danceable", 0, 100)

    st.subheader('Popularity')
    popularity = st.slider("100 is very popular", 0, 100)

    st.subheader('Energy')
    energy = st.slider("100 is very energetic", 0, 100)


params = {'val' : mood, 'dnce' : danceability, 'pop' : popularity, 'nrgy': energy}

with setlist:
    df.display()
