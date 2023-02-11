import streamlit as st
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



#filtered = []

with sliders:
    #left_col = st.column()
    st.header('What kind of playlist are you going to create?')

    st.subheader('Mood')
    mood = st.slider("100 is happy mood", 0, 100)
    show_mood = st.checkbox("Apply mood filter")

    if show_mood:
        val_filter = df['val'].isin(range(mood-20, mood+20))
    else:
        val_filter = df['val']
        #filtered.append(val_filter)
        #df_val = df[val_filter]
        #filtered.append(df_val)

    st.subheader('Danceabilty')
    danceability = st.slider("100 is very danceable", 0, 100)
    show_dnce = st.checkbox("Apply danceability filter")

    if show_dnce:
        dnce_filter = df['dnce'].isin(range(danceability-20, danceability+20))
    else:
        dnce_filter = df['dnce']
        #filtered.append(dnce_filter)
        #df_dnce = df[dnce_filter]
        #filtered.append(df_dnce)

    st.subheader('Popularity')
    popularity = st.slider("100 is very popular", 0, 100)
    show_pop = st.checkbox("Apply popularity filter")

    if show_pop:
        pop_filter = df['pop'].isin(range(popularity-20, popularity+20))
    else:
       pop_filter = df['pop']
        #filtered.append(pop_filter)
        #df_pop = df[pop_filter]
        #filtered.append(df_pop)

    st.subheader('Energy')
    energy = st.slider("100 is very energetic", 0, 100)
    show_energy = st.checkbox("Apply energy filter")

    if show_energy:   
        nrgy_filter = df['nrgy'].isin(range(energy-20, energy+20))
    else:
        nrgy_filter = df['nrgy']
        #filtered.append(nrgy_filter)
        #df_nrgy = df[nrgy_filter]
        #filtered.append(df_nrgy)



#if filtered:

    
    #df_filter = pd.concat(filtered, axis = 0)
    #df_filter.drop_duplicates(inplace=True)



with setlist:
    try:
        df_filter = df[val_filter & dnce_filter & pop_filter & nrgy_filter]

    except:
        st.write("No filters selected.")
        
    show_all = st.checkbox("Show all songs in the database")

    if show_all:
        st.dataframe(df)
    else:
        st.dataframe(df_filter)



with counters:
    st.header("Counters")

    st.subheader("Total Duration")
    if show_all:
        st.write(round(df['dur'].sum() / 60, 2), 'minutes')
    if filtered:
        st.write(round(df_filter['dur'].sum() / 60, 2), 'minutes')

    st.subheader("Number of Songs")
    if show_all:
        st.write(df.shape[0])
    if filtered:
        st.write(df_filter.shape[0])
