import streamlit as st
import  streamlit_vertical_slider  as svs
import pandas as pd

df = pd.read_csv('topMusicJOB.csv', index_col = 0)

df.rename({'Unnamed: 0' : 'id', 'top genre': 'genre'}, axis=1, inplace=True)



header = st.container()
sliders = st.container()
plot = st.container()
setlist = st.container()
counters = st.container()



with header:
    st.title('Setlist Generator')

    svs.vertical_slider("Test", 0, 100)



with sliders:
    #left_col = st.column()
    
    st.header('What kind of playlist are you going to create?')
    
    st.subheader('Mood')
    mood = st.slider("100 is happy mood", 0, 100, step = 20)
    show_mood = st.checkbox("Apply mood filter")

    if show_mood:
        val_filter = df['val'].isin(range(mood-20, mood+20))
    else:
        val_filter = df['val']


    st.subheader('Danceabilty')
    danceability = st.slider("100 is very danceable", 0, 100, step = 20)
    show_dnce = st.checkbox("Apply danceability filter")

    if show_dnce:
        dnce_filter = df['dnce'].isin(range(danceability-20, danceability+20))
    else:
        dnce_filter = df['dnce']
            

    st.subheader('Popularity')
    popularity = st.slider("100 is very popular", 0, 100, step = 20)
    show_pop = st.checkbox("Apply popularity filter")

    if show_pop:
        pop_filter = df['pop'].isin(range(popularity-20, popularity+20))
    else:
       pop_filter = df['pop']
    

    st.subheader('Energy')
    energy = st.slider("100 is very energetic", 0, 100, step = 20)
    show_energy = st.checkbox("Apply energy filter")

    if show_energy:   
        nrgy_filter = df['nrgy'].isin(range(energy-20, energy+20))
    else:
        nrgy_filter = df['nrgy']



with setlist:
    show_all = st.checkbox("Show all songs in the database")

    if show_all:
        st.dataframe(df)
    else:
        try:
            df_filter = df[val_filter & dnce_filter & pop_filter & nrgy_filter]
            st.dataframe(df_filter)

        except:
            st.write("No filters selected.")
        



with counters:
    st.header("Counters")

    st.subheader("Total Duration")
    if show_all:
            hours = int(df['dur'].sum() / 3600)
            mod_hour = df['dur'].sum() % 3600
            minutes = int((mod_hour) / 60)
            seconds = mod_hour % 60
            st.write(hours, 'hours', ',', minutes, 'minutes', ',', seconds, 'seconds')
    else:
        try:
            hours = int(df_filter['dur'].sum() / 3600)
            mod_hour = df_filter['dur'].sum() % 3600
            minutes = int((mod_hour) / 60)
            seconds = mod_hour % 60
            st.write(hours, 'hours', ',', minutes, 'minutes', ',', seconds, 'seconds')
        except:
            st.write("No filters selected.")


    st.subheader("Number of Songs")
    if show_all:
        st.write(df.shape[0])
    else:
        try:
            st.write(df_filter.shape[0])
        except:
            st.write("No filters selected.")
