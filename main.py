import streamlit as st
import pandas as pd
import numpy as np
import  streamlit_vertical_slider  as svs


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
    st.slider("100 is happy mood", 0, 100)
    st.subheader('Danceabilty')
    st.slider("100 is very danceable", 0, 100)
    st.subheader('Popularity')
    st.slider("100 is very popular", 0, 100)
    st.subheader('Energy')
    st.slider("100 is very energetic", 0, 100)

