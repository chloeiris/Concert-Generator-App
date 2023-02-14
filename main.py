import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df = pd.read_csv('topMusicJOB.csv', index_col = 0)

df.rename({'Unnamed: 0' : 'id', 'top genre': 'genre'}, axis=1, inplace=True)



header = st.container()
plot = st.container()
setlist = st.container()
counters = st.container()



with header:
    st.title('Playlist Generator')


    
with st.sidebar:
    st.title(':red[What kind of playlist are you going to create?]')

    st.subheader('Mood')
    mood = st.slider("100 is happy mood", 0, 100, step = 20)
    show_mood = st.checkbox("Apply mood filter")

    if show_mood:
        val_filter = df['val'].isin(range(mood-20, mood+20))
    else:
        val_filter = df['val'].isin(range(100))


    st.subheader('Danceabilty')
    danceability = st.slider("100 is very danceable", 0, 100, step = 20)
    show_dnce = st.checkbox("Apply danceability filter")

    if show_dnce:
        dnce_filter = df['dnce'].isin(range(danceability-20, danceability+20))
    else:
        dnce_filter = df['dnce'].isin(range(100))
            

    st.subheader('Popularity')
    popularity = st.slider("100 is very popular", 0, 100, step = 20)
    show_pop = st.checkbox("Apply popularity filter")

    if show_pop:
        pop_filter = df['pop'].isin(range(popularity-20, popularity+20))
    else:
        pop_filter = df['pop'].isin(range(100))
    

    st.subheader('Energy')
    energy = st.slider("100 is very energetic", 0, 100, step = 20)
    show_energy = st.checkbox("Apply energy filter")

    if show_energy:   
        nrgy_filter = df['nrgy'].isin(range(energy-20, energy+20))
    else:
        nrgy_filter = df['nrgy'].isin(range(100))



with setlist:
    show_all = st.checkbox("Show all songs in the database")

    if show_all:
        st.dataframe(df)
    else:
        #try:
        df_filter = df[val_filter & dnce_filter & pop_filter & nrgy_filter]
        st.dataframe(df_filter)

        #except:
            #st.write("No filters selected.")
        



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
        #try:
        hours = int(df_filter['dur'].sum() / 3600)
        mod_hour = df_filter['dur'].sum() % 3600
        minutes = int((mod_hour) / 60)
        seconds = mod_hour % 60
        st.write(hours, 'hours', ',', minutes, 'minutes', ',', seconds, 'seconds')
        #except:
            #st.write("No filters selected.")


    st.subheader("Number of Songs")
    if show_all:
        st.write(df.shape[0])
    else:
        #try:
        st.write(df_filter.shape[0])
        #except:
            #st.write("No filters selected.")



st.header("Playlist Traits Viz")

tab1, tab2 = st.tabs(["Main traits", "Playlist Flow"])

check_mood = tab2.checkbox("Show mood")
check_dnce = tab2.checkbox("Show danceability")
check_pop = tab2.checkbox("Show popularity")
check_nrgy = tab2.checkbox("Show energy")

if show_all:

    fig, axes = plt.subplots(figsize=(20, 15))
    axes.boxplot(x=df['val'], widths=0.25, positions=[0.5], patch_artist= True, notch=False, labels=["mood"],
                    boxprops=dict(facecolor='mediumvioletred', color='red', linewidth=1.5),
                    capprops=dict(color="red", linewidth=1.5),
                    whiskerprops=dict(color="red", linewidth=1.5),
                    flierprops=dict(color="red", markeredgecolor="red", linewidth=1.5),
                    medianprops=dict(color="red", linewidth=1.5))
    axes.boxplot(x=df['dnce'], widths=0.25, positions=[1], patch_artist= True, notch=False, labels=["danceability"], 
                    boxprops=dict(facecolor='lightseagreen', color='darkorange', linewidth=1.5),
                    capprops=dict(color="darkorange", linewidth=1.5),
                    whiskerprops=dict(color="darkorange", linewidth=1.5),
                    flierprops=dict(color="darkorange", markeredgecolor="darkorange", linewidth=1.5),
                    medianprops=dict(color="darkorange", linewidth=1.5))
    axes.boxplot(x=df['nrgy'], widths=0.25, positions=[1.5], patch_artist= True, notch=False, labels=["popularity"], 
                    boxprops=dict(facecolor='mediumseagreen', color='orange', linewidth=1.5),
                    capprops=dict(color="orange", linewidth=1.5),
                    whiskerprops=dict(color="orange", linewidth=1.5),
                    flierprops=dict(color="orange", markeredgecolor="orange", linewidth=1.5),
                    medianprops=dict(color="orange", linewidth=1.5))
    axes.boxplot(x=df['nrgy'], widths=0.25, positions=[2], patch_artist= True, notch=False, labels=["energy"], 
                    boxprops=dict(facecolor='orangered', color='lawngreen', linewidth=1.5),
                    capprops=dict(color="lawngreen", linewidth=1.5),
                    whiskerprops=dict(color="lawngreen", linewidth=1.5),
                    flierprops=dict(color="lawngreen", markeredgecolor="lawngreen", linewidth=1.5),
                    medianprops=dict(color="lawngreen", linewidth=1.5))
    tab1.pyplot(fig)

    fig2, axes2 = plt.subplots(figsize=(20, 15))
    if check_mood:
        sns.lineplot(x=np.linspace(0,df['dur'].sum(),num=df.shape[0]), y=df['val'], data=df, ax=axes2, color='mediumvioletred', label='mood')
    if check_dnce:
        sns.lineplot(x=np.linspace(0,df['dur'].sum(),num=df.shape[0]), y=df['dnce'], data=df, ax=axes2, color='lightseagreen', label='danceability')
    if check_pop:
        sns.lineplot(x=np.linspace(0,df['dur'].sum(),num=df.shape[0]), y=df['pop'], data=df, ax=axes2, color='mediumseagreen', label='popularity')
    if check_nrgy:
        sns.lineplot(x=np.linspace(0,df['dur'].sum(),num=df.shape[0]), y=df['nrgy'], data=df, ax=axes2, color='orangered', label='energy')
    axes2.legend(fontsize=15)
    tab2.pyplot(fig2)

else:
    fig, axes = plt.subplots(figsize=(20, 15))
    axes.boxplot(x=df_filter['val'], widths=0.25, positions=[0.5], patch_artist= True, notch=False, labels=["mood"],
                    boxprops=dict(facecolor='mediumvioletred', color='red', linewidth=1.5),
                    capprops=dict(color="red", linewidth=1.5),
                    whiskerprops=dict(color="red", linewidth=1.5),
                    flierprops=dict(color="red", markeredgecolor="red", linewidth=1.5),
                    medianprops=dict(color="red", linewidth=1.5))
    axes.boxplot(x=df_filter['dnce'], widths=0.25, positions=[1], patch_artist= True, notch=False, labels=["danceability"], 
                    boxprops=dict(facecolor='lightseagreen', color='darkorange', linewidth=1.5),
                    capprops=dict(color="darkorange", linewidth=1.5),
                    whiskerprops=dict(color="darkorange", linewidth=1.5),
                    flierprops=dict(color="darkorange", markeredgecolor="darkorange", linewidth=1.5),
                    medianprops=dict(color="darkorange", linewidth=1.5))
    axes.boxplot(x=df_filter['nrgy'], widths=0.25, positions=[1.5], patch_artist= True, notch=False, labels=["popularity"], 
                    boxprops=dict(facecolor='mediumseagreen', color='orange', linewidth=1.5),
                    capprops=dict(color="orange", linewidth=1.5),
                    whiskerprops=dict(color="orange", linewidth=1.5),
                    flierprops=dict(color="orange", markeredgecolor="orange", linewidth=1.5),
                    medianprops=dict(color="orange", linewidth=1.5))
    axes.boxplot(x=df_filter['nrgy'], widths=0.25, positions=[2], patch_artist= True, notch=False, labels=["energy"], 
                    boxprops=dict(facecolor='orangered', color='lawngreen', linewidth=1.5),
                    capprops=dict(color="lawngreen", linewidth=1.5),
                    whiskerprops=dict(color="lawngreen", linewidth=1.5),
                    flierprops=dict(color="lawngreen", markeredgecolor="lawngreen", linewidth=1.5),
                    medianprops=dict(color="lawngreen", linewidth=1.5))
    tab1.pyplot(fig)


    fig2, axes2 = plt.subplots(figsize=(20, 15))
    if check_mood:
        sns.lineplot(x=np.linspace(0,df_filter['dur'].sum(),num=df_filter.shape[0]), y=df_filter['val'], data=df_filter, ax=axes2, color='mediumvioletred', label='mood')
    if check_dnce:
        sns.lineplot(x=np.linspace(0,df_filter['dur'].sum(),num=df_filter.shape[0]), y=df_filter['dnce'], data=df_filter, ax=axes2, color='lightseagreen', label='danceability')
    if check_pop:
        sns.lineplot(x=np.linspace(0,df_filter['dur'].sum(),num=df_filter.shape[0]), y=df_filter['pop'], data=df_filter, ax=axes2, color='mediumseagreen', label='popularity')
    if check_nrgy:
        sns.lineplot(x=np.linspace(0,df_filter['dur'].sum(),num=df_filter.shape[0]), y=df_filter['nrgy'], data=df_filter, ax=axes2, color='orangered', label='energy')
    axes2.legend(fontsize=15)
    tab2.pyplot(fig2)



    
