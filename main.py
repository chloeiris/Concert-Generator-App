import streamlit as st
import pandas as pd
import numpy as np

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
    st.slider('Mood', 0, 100)
    
