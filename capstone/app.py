import streamlit as st
import pandas as pd
import matplotlib.pyplot as pt


df=pd.read_csv('data\dataset.csv',sep=',')
df = df.drop(['Unnamed: 0','key','mode','tempo','time_signature','loudness','duration_ms','explicit'],axis=1)

grades=df.copy()
#Transformando os valores das colunas em int
grades[['danceability','energy','speechiness','acousticness','instrumentalness','liveness','valence']]=round(grades[['danceability','energy','speechiness','acousticness','instrumentalness','liveness','valence']]*100,ndigits=None).astype(int)

grade_dic={range(0,20):'E',range(20,40):'D',range(40,60):'C',range(60,80):'B',range(80,101):'A'}
#Substituindo os valores por letras, conforme graduação acima
grades[['popularity','danceability','energy','speechiness','acousticness','instrumentalness','liveness','valence']]=grades[['popularity','danceability','energy','speechiness','acousticness','instrumentalness','liveness','valence']].replace(grade_dic)

#gerando coluna com musica e artistas para eliminar repetições
grades['infor']=grades.track_name+", " + grades.artists
grades.drop_duplicates(subset=['infor','track_genre'],inplace=True)

st.set_page_config(page_title='What to play')
header=st.container()
inputs=st.container ()
sugestions=st.container()
caracteristics=st.container()

with header:
    st.title("Spotify's unnoficial next song suggestor")


with inputs:
   col1,col2=st.columns(2)

   with col1:
        genre=st.selectbox(label='Your Favorite Genre',options=grades.track_genre.unique(),)

   with col2:
       
        music=st.selectbox(label='Your Favorite Song',options=grades[grades['track_genre']==genre].infor.unique())

   n_samples=st.slider(label='Samples',min_value=1,max_value=15,value=5,step=1)        

choice=grades[grades['infor']==music].reset_index(drop=True)

print(choice)
pop_sug=grades[(grades['popularity']=='A') & (grades['danceability']==choice['danceability'][0])]
unpop_sug= grades[(grades['popularity']=='E') & (grades['danceability']==choice['danceability'][0])]

with sugestions:
    st.write('Top Picks 4U')
    top_picks=st.table(pop_sug['infor'].head())

    st.write('U may also like')
    low_picks= st.table(unpop_sug['infor'].head())
