import matplotlib.pyplot as plt
import numpy as np
import pafy
import pandas as pd
import seaborn as sns

youtube_links = {}
def get_link_ratio(x):
    '''
    returns a dictionary that holds ratios of links to non-links for each 
    personality type :x: input csv
    '''
    input_file = open(x, 'r')
    input_file.readline()
    #output_file = open('output.txt','w')
    output_dict = {}
    comment_dict = {}
    link_dict = {}
    youtube_link_starter = 'http://www.youtube.com/watch?v='
    youtube_link_code_length = 11
    global youtube_links
    while True:
        line = input_file.readline()
        if not line:
            break
        personality_type, sep, data = line.partition(',')
        data = data[1:len(data) - 1]
        comments = data.split('|||')
        link_count = 0
        for comment in comments:
            if 'http://' in comment:
                while youtube_link_starter in comment:
                    start_index = comment.find(youtube_link_starter)
                    youtube_link = comment[start_index:start_index + len(youtube_link_starter) + youtube_link_code_length]
                    youtube_links.setdefault(personality_type, []).append(youtube_link)
                    #output_file.write('{0}\n'.format(youtube_link))
                    comment = comment[:start_index] + comment[start_index+len(youtube_link_starter) + youtube_link_code_length:]
                link_count += 1
        comment_dict[personality_type] = comment_dict.get(personality_type,0) + len(comments)
        link_dict[personality_type] = link_dict.get(personality_type,0) + link_count
    for key in comment_dict.keys():
        output_dict[key] = 100 * link_dict[key]/comment_dict[key]
    input_file.close()
    #output_file.close
    return output_dict 

def make_video_data_files(x):
    '''
    writes relevent data from youtube http requests to csvs :x: a dictionary 
    where each key is a personality type and value is a list of links
    '''
    for k,v in x.items():
        output_file = open("link_data/{0}.csv".format(k),"w")
        for link in v:
            try: 
                video = pafy.new(link)
                output_file.write("{0},{1},{2}\n".format(video.title.replace(",",""), video.viewcount,video.category))
            except:
                continue
        output_file.close()

def make_one_file(x, name):
    output_file = open("link_data/{0}.csv".format(name), "w")
    for v in x.get(name,[]):
        try: 
            video = pafy.new(v)
            output_file.write("{0},{1},{2}\n".format(video.title.replace(",",""), video.viewcount,video.category))
        except:
            continue

def get_avg_views(x):
    '''
    calculate avg views per video for each personality type :x: dictionary of 
    personality types and links; only keys of dictionary are used
    '''
    output_dictionary = {}
    for k in x.keys():
        file = open('link_data/{0}.csv'.format(k),"r")
        index = 0
        count = 0
        while True:
            line = file.readline()
            if not line:
                break
            comma_count = line.count(',')
            count += int(line.split(',')[comma_count - 1])
            index += 1
        if(index < 30):
            count = 0
        output_dictionary[k] = int(count/index)
        file.close()
    return output_dictionary

def get_link_categories(x):
    '''
    Test fuction to get counts of youtube links' categories. Discovery: most links
    fall under Music. Functionality will be included in make_video_data_files.
    :x: dictionary with personality types and youtube links
    '''
    output_dict = {}
    for link in x.get('link_data/ESTP',[]):
        try:
            video = pafy.new(link)
            output_dict[video.category] = output_dict.get(video.category,0) + 1
        except:
            continue
    return output_dict


#Get link reation, print sorted map
x = get_link_ratio('mbti_1.csv')
x = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
# print(x)
# print({k: v for k, v in sorted(x.items(), key=lambda item: item[1])})
'''
{'ESFJ': 0.013875123885034688, 'ESTJ': 0.016137428422696512, 'ENTP': 0.026983797873285743, 
'ENTJ': 0.02847511753747893, 'ESFP': 0.028893905191873587, 'ESTP': 0.03135808162324187, 
'ENFP': 0.03158472946992585, 'ENFJ': 0.03165374677002584, 'ISFJ': 0.03201576160571358, 
'INFJ': 0.03306289439012551, 'INTJ': 0.036820338853843074, 'ISTJ': 0.03792999092101281, 
'ISTP': 0.03921687477269972, 'INTP': 0.03974178885399075, 'INFP': 0.042340416054167225, 
'ISFP': 0.05169230769230769}
'''

# plt.figure(figsize=(20,10))
# sns.barplot(x=np.array(list(x.values())), y=np.array(list(x.keys())))
# plt.ylabel('Type', fontsize=16)
# plt.xlabel('Number of Links (Per 100 Posts)', fontsize=16)
# plt.xticks(fontsize=16, rotation=0)
# plt.yticks(fontsize=16, rotation=0)
# plt.title('Average Links Per 100 Posts By Personality')
# plt.show()
#create data files WARNING function makes ~11000 http requests, runtime ~ 2 hours
# make_video_data_files(youtube_links)
# make_one_file(youtube_links, "ISTP")

#Find average views per video, sort results
y = (get_avg_views(youtube_links))
y = {k: v for k, v in sorted(y.items(), key=lambda item: item[1])}
'''
{'ESFJ': 0, 'ESFP': 0, 'ESTJ': 0, 'INTJ': 17136182, 'INFP': 18424824, 'INTP': 21762186, 
'ISTJ': 22282518, 'ISTP': 25928740, 'INFJ': 29320080, 'ENFP': 30275269, 'ENFJ': 47571205, 
'ISFJ': 48570312, 'ISFP': 48798584, 'ENTP': 50213236, 'ENTJ': 52580978, 'ESTP': 54378005}
'''
# plt.figure(figsize=(20,10))
# sns.barplot(x=np.array(list(y.values())), y=np.array(list(y.keys())))
# plt.ylabel('Type', fontsize=16)
# plt.xlabel('Average Views', fontsize=16)
# plt.xticks(fontsize=16, rotation=0)
# plt.yticks(fontsize=16, rotation=0)
# plt.title('Average View Per Link By Personality')
# plt.show()
