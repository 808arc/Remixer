#statistic and research part for defining a right song 
import billboard
from datetime import datetime

# create an empty list to store the chart data

track_name = []
track_artist = []

dates = ['2009-07-07', '2009-09-08', '2009-09-09']

for custom_date in dates:


#custom_date = datetime.today().strftime('%Y-%m-%d')
#custom_date = '2007-07-07'

    chart = billboard.ChartData('hot-100', date=custom_date)

# iterate over the chart data and append each item to the song_list
    for song in chart:
    #    song_list.append(song.title)
    #    song_list.append(song.artist)
        track_name.append(song.title + " by " + song.artist)
    
import pandas as pd
# create a dictionary with data
tracklist = {'name': track_name}

# create a DataFrame from the dictionary
df = pd.DataFrame(tracklist)
df.drop_duplicates()


print(df)
