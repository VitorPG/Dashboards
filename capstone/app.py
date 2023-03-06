import streamlit as st
import pandas as pd
import matplotlib.pyplot as pt


df=pd.read_csv('data\dataset.csv',sep=',')
df = df.drop(['Unnamed: 0','key','mode','tempo','time_signature','loudness','duration_ms','explicit'],axis=1)

grades=df.copy()
#Changing columns values to int
grades[['danceability','energy','speechiness','acousticness','instrumentalness','liveness','valence']]=round(grades[['danceability','energy','speechiness','acousticness','instrumentalness','liveness','valence']]*100,ndigits=None).astype(int)

grade_dic={range(0,20):'E',range(20,40):'D',range(40,60):'C',range(60,80):'B',range(80,101):'A'}
#Replacing numbers for letter grades 
grades[['popularity','danceability','energy','speechiness','acousticness','instrumentalness','liveness','valence']]=grades[['popularity','danceability','energy','speechiness','acousticness','instrumentalness','liveness','valence']].replace(grade_dic)

#creating info column to avoid duplicates in same song/artist but keep same song name for diferent artists
grades['infor']=grades.track_name+", " + grades.artists

#drop duplicates from same song in the same genre
grades.drop_duplicates(subset=['infor','track_genre'],inplace=True)

st.set_page_config(page_title='What to play')
header=st.container()
inputs=st.container ()
recomend=st.container()
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

#choose first row from choice options (avoid same song in diferent genders)
match=pd.DataFrame(choice.iloc[:1])

#print(match)

#filter possible sugestions only to same genre
genre_df=grades[grades['track_genre']==genre]

sugestions=[]

for row in range(genre_df.shape[0]):
    
    linha=genre_df.iloc[[row]].reset_index(drop=True)
    
    #compare similarity between to chosen music and all the rows inside genre sample
    diference=match.compare(linha,align_axis=0)

    # since all duplicates from same genre have been dropped already, 
    # this diference of less than 10 will result in matches of at least 4 of the following parameters:
    # danceability energy speechiness acousticness instrumentalness liveness valence
    if diference.shape[1]<=10:
        sugestions.append(linha)

sugestions=pd.concat(sugestions,axis=0)
sugestions.reset_index(drop=True,inplace=True)

pop_sug=sugestions[sugestions['popularity']=='A']
unpop_sug= sugestions[sugestions['popularity']!='A']

with recomend:
    
    st.write('Top Picks 4U')
    top_picks=st.table(pop_sug['infor'].head(n_samples))

    st.write('U may also like')
    low_picks= st.table(unpop_sug['infor'].head(n_samples))
