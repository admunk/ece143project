import matplotlib.pyplot as plt
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

type_list = ["ENFJ", "ENFP", "ENTJ", "ENTP", "ESFJ", "ESFP", "ESTJ", "ESTP", "INFJ", "INFP", "INTJ", "INTP", "ISFJ", "ISFP", "ISTJ", "ISTP"]
genre_list = ["rock","hip hop","pop","electronic","r&b","dance","folk","jazz","classic","soundtrack","other"]
color_list = ["#fff100","#ff8c00","#e81123","#ec008c","#68217a","#00188f","#bad80a","#00b294","#009e49","#00bcf2","#9f5f80","#fcf8ec"]
indicators = ["E","I","N","S","F","T","P","J"]
def find_genre(genre_list):
    '''
    Returns a main genre from a list of genres :genre_list: a list of genres
    '''
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
    if(len(generator) == 0):
        return 'unlisted'
    return 'other'
    

def make_genre_files(id, secret):
    '''
    Makes a file for each personality type that returns data on a song using
    Spotify's API :id: spotify API ID :secret: spotify API Secret
    '''
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=id,
                                                            client_secret=secret))
    
    for personality in type_list:    
        input_file = open('link_data/{0}.csv'.format(personality), 'r')
        output_file = open('link_data/spotify-{0}.csv'.format(personality), 'w')
        genre_dict = {}
        for genre in genre_list:
            genre_dict[genre] = 0
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
                    name = results['tracks']['items'][0]['album']['artists'][0]['name']
                    genres = sp.artist(artist)['genres']
                    genre = find_genre(genres)
                    output_file.write("{0},{1},{2}\n".format(components[0], name,genre))
                    genre_dict[genre] = genre_dict.get(genre,0) + 1
                    success_count += 1
                except:
                    continue
        input_file.close()
        output_file.write("Genres:\n")
        for k,v in genre_dict.items():
            output_file.write("{0},{1}\n".format(k,v))
        output_file.close()

def make_genre_charts():
    '''
    Creates visualization of genre data by personality
    '''
    total_dict = {}
    for personality in type_list:
        input_file = open("link_data/spotify-{0}.csv".format(personality)) 
        labels = []
        count = []
        colors = []
        genre_count_dict = {}
        color_index = 0
        while True:
            line = input_file.readline()
            if not line:
                break
            if line.count(',') == 1:
                components = line.split(',')
                genre_count_dict[components[0]] = components[1]
                if(int(components[1]) > 0):   
                    total_dict[components[0]] = total_dict.get(components[0], 0) + int(components[1])
                    labels.append(components[0])
                    count.append(components[1])
                    colors.append(color_list[color_index])
                color_index += 1
        input_file.close()
        if len(labels) > 0:
            fig, ax = plt.subplots(figsize=(20, 10), subplot_kw=dict(aspect="equal"))
            wedges, texts, autotexts = ax.pie(count, labels=labels,autopct='%1.1f%%',
                                    textprops=dict(color="w"),pctdistance=0.9,startangle=90,colors = colors)
            ax.legend(wedges, labels, title="Genres", bbox_to_anchor=(1, 0, 0.5, 1))
            plt.setp(autotexts, size=8,weight="bold")
            ax.set_title("{0}'s Genres".format(personality),size=16)
            plt.show()
    fig, ax = plt.subplots(figsize=(20, 10), subplot_kw=dict(aspect="equal"))
    wedges, texts, autotexts = ax.pie(list(total_dict.values()), labels=list(total_dict.keys()),autopct='%1.1f%%',
                                    textprops=dict(color="w"),pctdistance=0.9,startangle=90,colors = color_list)
    ax.legend(wedges, list(total_dict.keys()), title="Genres", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=8,weight="bold")
    ax.set_title("Genres for All Personalities",size=16)
    plt.show()


def autopct(pct):
    return ('%.2f' % pct) if pct > 2 else ''

def label_list(data):
    return_list = []
    index = 0
    for k,v in data.items():
        if index > len(list(data.keys())) -  6: 
           return_list.append(k)
        else:
           return_list.append('')
        index += 1
    return return_list


def make_youtube_categories_chart():
    '''
    Makes visualization of youtube category data
    '''
    category_dict = {}
    for personality in type_list:    
        input_file = open('link_data/{0}.csv'.format(personality), 'r')
        while True:
            line = input_file.readline()
            if not line:
                break
            components = line.split(',')   
            category_dict[components[2]] = category_dict.get(components[2],0) + 1
        input_file.close()
    category_dict = {k: v for k, v in sorted(category_dict.items(), key=lambda item: item[1])}
    fig, ax = plt.subplots(figsize=(20, 10), subplot_kw=dict(aspect="equal"))
    wedges, texts, autotexts = ax.pie(list(category_dict.values()), labels=label_list(category_dict),autopct=autopct,
                                    textprops=dict(color="k"),pctdistance=0.9,startangle=90)
    ax.legend(wedges, list(category_dict.keys()), title="Categories", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=8,weight="bold")
    ax.set_title("Youtube Link Categories",size=16)
    plt.show()

def make_genre_charts_per_indicator():
    '''
    Visualizes data on genres by indicator
    '''
    total_dict = {}
    for indicator in indicators:
        total_dict[indicator] = {}
        for genre in genre_list:
            total_dict[indicator][genre] = 0
    for personality in type_list:
        input_file = open("link_data/spotify-{0}.csv".format(personality)) 
        while True:
            line = input_file.readline()
            if not line:
                break
            if line.count(',') == 1:
                components = line.split(',')
                if(int(components[1]) > 0):   
                    for indicator in indicators:
                        if indicator in personality:
                            total_dict[indicator][components[0]] = total_dict[indicator].get(components[0],0) + int(components[1])
    for k,v in total_dict.items():
        fig, ax = plt.subplots(figsize=(20, 10), subplot_kw=dict(aspect="equal"))
        wedges, texts, autotexts = ax.pie(list(v.values()), labels=v.keys(),autopct='%1.1f%%',
                                    textprops=dict(color="k"),pctdistance=0.9,startangle=90,colors = color_list)
        ax.legend(wedges,v.keys(), title="Genres", bbox_to_anchor=(1, 0, 0.5, 1))
        plt.setp(autotexts, size=8,weight="bold")
        ax.set_title("{0}'s Genres".format(k),size=16)
        plt.show()
    input_file.close()
        
# Makes data files with Spotify information
# make_genre_files()

#Genre charts for each personality type
make_genre_charts()

#Chart of youtube video categories
make_youtube_categories_chart()

#Genre chart by type indicator
make_genre_charts_per_indicator()
