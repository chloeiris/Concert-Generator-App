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
    
    svs.vertical_slider(key=3, 
                    default_value=20, 
                    step=10, 
                    min_value=0, 
                    max_value=100,
                    slider_color= 'green' #optional
                    track_color='lightgray' #optional
                    thumb_color = 'red' #optional
                    )

