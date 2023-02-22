import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

@st.cache_data
def load_data(path):
    df = pd.read_csv(path, index_col = 0)
    df.rename({'Unnamed: 0' : 'id', 'top genre': 'genre'}, axis=1, inplace=True)
    return df

df0 = load_data('topMusicJOB.csv')



header = st.container()
setlist = st.container()
counters = st.container()
plots = st.container()



with header:
    st.title('Playlist Generator')


    
with st.sidebar:
    st.title(':red[What kind of playlist are you going to create?]')

    @st.cache_data
    def gen_sliders(name, colname, message, start=0, stop=100, step=20):
        st.subheader(name)
        slider = st.slider(message, start, stop, step)
        show_filter = st.checkbox(f"Apply {name.lower()} filter")

        if show_filter:
            filter = df0[colname].isin(range(slider-step, slider+step))
        else:
            filter = df0[colname].isin(range(stop))

        return filter

    mood_filter = gen_sliders('Mood', 'val', '100 is happy mood')
    dnce_filter = gen_sliders('Danceabilty', 'dnce', '100 is very danceable')
    pop_filter = gen_sliders('Popularity', 'pop', '100 is very popular')
    nrgy_filter = gen_sliders('Energy', 'nrgy', '100 is very energetic')



with setlist:
    show_all = st.checkbox("Show all songs in the database")

    if show_all:
        data = st.dataframe(df0)
        data2 = pd.DataFrame(data)
    else:
        df_filter = df0[mood_filter & dnce_filter & pop_filter & nrgy_filter]
        data = st.dataframe(df_filter)
        data2 = pd.DataFrame(data)



with counters:
    st.header("Counters")

    st.subheader("Total Duration")
    def counter(dataf):
        hours = int(dataf['dur'].sum() / 3600)
        mod_hour = dataf['dur'].sum() % 3600
        minutes = int((mod_hour) / 60)
        seconds = mod_hour % 60
        return st.write(hours, 'hours', ',', minutes, 'minutes', ',', seconds, 'seconds')

    if show_all:
        counter(df0)
    else:
        counter(df_filter)


    st.subheader("Number of Songs")
    if show_all:
        st.write(df0.shape[0])
    else:
        st.write(df_filter.shape[0])
        


with plots:
    st.header("Playlist Visualizaton")

    tab1, tab2 = st.tabs(["Main traits", "Playlist Flow"])

    @st.cache_data
    def check_char(name):
        check_box = tab2.checkbox(f"Show {name.lower()}")
        return check_box
    
    check_mood = check_char("mood")
    check_dnce = check_char("danceability")
    check_pop = check_char("popularity")
    check_nrgy = check_char("energy")

    def boxplots_chars(dataf, colnames, labels, facecolors, colors):
        fig, axes = plt.subplots(figsize=(20, 15))
        axes.boxplot(x=dataf[colnames[0]], widths=0.25, positions=[0.5], patch_artist= True, notch=False, labels=[labels[0]],
                        boxprops=dict(facecolor=facecolors[0], color=colors[0], linewidth=1.5),
                        capprops=dict(color=colors[0], linewidth=1.5),
                        whiskerprops=dict(color=colors[0], linewidth=1.5),
                        flierprops=dict(color=colors[0], markeredgecolor=colors[0], linewidth=1.5),
                        medianprops=dict(color=colors[0], linewidth=1.5))
        axes.boxplot(x=dataf[colnames[1]], widths=0.25, positions=[0.5], patch_artist= True, notch=False, labels=[labels[1]],
                        boxprops=dict(facecolor=facecolors[1], color=colors[1], linewidth=1.5),
                        capprops=dict(color=colors[1], linewidth=1.5),
                        whiskerprops=dict(color=colors[1], linewidth=1.5),
                        flierprops=dict(color=colors[1], markeredgecolor=colors[1], linewidth=1.5),
                        medianprops=dict(color=colors[1], linewidth=1.5))
        axes.boxplot(x=dataf[colnames[2]], widths=0.25, positions=[0.5], patch_artist= True, notch=False, labels=[labels[2]],
                        boxprops=dict(facecolor=facecolors[2], color=colors[2], linewidth=1.5),
                        capprops=dict(color=colors[2], linewidth=1.5),
                        whiskerprops=dict(color=colors[2], linewidth=1.5),
                        flierprops=dict(color=colors[2], markeredgecolor=colors[2], linewidth=1.5),
                        medianprops=dict(color=colors[2], linewidth=1.5))
        axes.boxplot(x=dataf[colnames[3]], widths=0.25, positions=[0.5], patch_artist= True, notch=False, labels=[labels[3]],
                        boxprops=dict(facecolor=facecolors[3], color=colors[3], linewidth=1.5),
                        capprops=dict(color=colors[3], linewidth=1.5),
                        whiskerprops=dict(color=colors[3], linewidth=1.5),
                        flierprops=dict(color=colors[3], markeredgecolor=colors[3], linewidth=1.5),
                        medianprops=dict(color=colors[3], linewidth=1.5))
        return tab1.pyplot(fig)
    

    def line_plots(dfr, colnames, colors, labels):
        fig2, axes2 = plt.subplots(figsize=(20, 15))
        if check_mood:
            sns.lineplot(x=np.linspace(0,dfr['dur'].sum(),num=dfr.shape[0]), y=dfr[colnames[0]], data=dfr, ax=axes2, color=colors[0], label=labels[0])
        if check_dnce:
            sns.lineplot(x=np.linspace(0,dfr['dur'].sum(),num=dfr.shape[0]), y=dfr[colnames[1]], data=dfr, ax=axes2, color=colors[1], label=labels[1])
        if check_pop:
            sns.lineplot(x=np.linspace(0,dfr['dur'].sum(),num=dfr.shape[0]), y=dfr[colnames[2]], data=dfr, ax=axes2, color=colors[2], label=labels[2])
        if check_nrgy:
            sns.lineplot(x=np.linspace(0,dfr['dur'].sum(),num=dfr.shape[0]), y=dfr[colnames[3]], data=dfr, ax=axes2, color=colors[3], label=labels[3])
        axes2.legend(fontsize=15)
        return tab2.pyplot(fig2)

    
    colnames = ['val', 'dnce', 'pop', 'nrgy']
    labels = ['mood', 'danceability', 'popularity', 'energy']
    facecolors = ['mediumvioletred', 'lightseagreen', 'mediumseagreen', 'lawngreen']
    colors = ['red', 'darkorange', 'orange', 'lawngreen']

    boxplots_chars(data2, colnames, labels, facecolors, colors)
    line_plots(data2, colnames, colors, labels)

    



        
