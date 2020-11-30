import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def find_genre(genre_list):
    if len(genre_list) == 0:
        return 'other'
    for genre in genre_list:
        if 'rock' in genre or 'metal' in genre or 'punk' in genre:
            return 'rock'
        elif 'rap' in genre or 'hop' in genre or 'hip' in genre:
            return 'hip hop'
        elif 'pop' in genre or 'new mellow' in genre:
            return 'pop'
        elif 'electronic' in genre or 'electro' in genre or 'techno' in genre:
            return 'electronic'
        elif 'r&b' in genre or 'reggae' in genre:
            return 'r&b'
        elif 'dance' in genre or 'house' in genre or 'rave' in genre or 'dubstep' in genre:
            return 'dance'
        elif 'folk' in genre:
            return 'folk'
        elif 'jazz' in genre or 'soul' in genre:
            return 'jazz'
        elif 'classic' in genre or 'piano' in genre:
            return 'classic'
        elif 'soundtrack' in genre or 'broadway' in genre:
            return 'soundtrack'
    print(genre_list)
    return 'other'
    

def get_genres(x):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="cfdbf9aecc71457f9421a63b45d888f5",
                                                            client_secret="6e73af200e5e4f9eb67010e6df985cb3"))
    input_file = open('link_data/INFJ.csv', 'r')
    genre_dict = {}
    success_count = 0
    total_count = 0
    while True:
        line = input_file.readline()
        if not line:
            break
        components = line.split(',')   
        if components[2] == 'Music\n':
            total_count += 1
            try:
                results = sp.search(q=components[0], limit=1, type='track')
                artist = results['tracks']['items'][0]['album']['artists'][0]['id'] 
                genres = sp.artist(artist)['genres']
                genre = find_genre(genres)
                genre_dict[genre] = genre_dict.get(genre,0) + 1
                success_count += 1
            except:
                continue
    return genre_dict
print(get_genres('x'))    
'''
{'rock': 63, 'pop': 44, 'electronic': 7, 'jazz': 12, 'hip hop': 13, 'folk': 15, 'other': 33, 'classic': 7, 'soundtrack': 4, 'dance': 13, 'r&b': 3}
'''
