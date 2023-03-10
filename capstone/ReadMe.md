# Next song sugestor

This project was done considering a [previous analisys](https://github.com/IvanLopesGit/VAD_DataVis_Final/blob/main/vad_capstone.ipynb) I made in partnership with [Ivan](https://github.com/IvanLopesGit) on a [Spotify's songs dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset) 

The current [dashboard](https://vitorpg-dashboards-capstoneapp-5ccbtr.streamlit.app/) was made using Streamlit and is hosted on its [shared platform](https://share.streamlit.io/).

## How to

The steps are pretty straightfoward: 

1. Choose a prefered music genre from the 'Favorite Genre' dropdown
2. Then select a song from that genre in the   'Favorite Song' options
3. You can select the amount of samples (or recomendations) that will appear on screen (if it shows less than selected it is because the dataset does not have that many matches)
4. The Top Picks will display songs with similar characteristics and high popularity (Grade A)
5. The 'U may also like' are songs with similar characterisics and low popularity (Grade not A)


On the Second part, below the sugestions, we have some interactive charts to explore the dataset.

The first chart shows the correlation between the song's characteristics and its popularity. 

The second one requires the user to select a characteristic and it displays the concentration of songs (for that selection) in each popularity level, separated by track genre. 


## Now you have everithing you need to create that special playlist. 
## Enjoy!!