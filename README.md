# ECE143 Project Group 21
## Myers-Briggs Personality Analysis in Python
<p align="center">
    Personality Type
</p>

![image](https://github.com/admunk/ece143project/blob/main/Images/MeyersBriggs.jpg)

## File Structure
![image](https://github.com/admunk/ece143project/blob/main/Images/Structure.png)

## Running the Project

### Link Processing

#### link_information_parser.py
##### get_link_ratio
Creates a dictionary of link ratios for each personality type</p>
Dependencies: None</p>

##### make_avg_link_chart
Visualizes link data</p>
Dependencies: get_link_ratio</p>

##### make_video_data_files
Creates csvs with output data for links from Youtube's API</p>
**Extremely long runtime/unneeded if all {Type}.csv exists**</p>
Dependencies: get_link_ratio</p>

##### get_avg_view
Creates a dictionary of average views of youtube videos by personality</p>
Dependecies: get_link_ratio, make_video_data_files</p>

##### make_avg_view_chart
Visualizes view data</p>
Dependencies: get_avg_view</p>

#### spotify_search.py

##### make_genre_files
Creates csvs with output data for Youtube music videos from Spotify's API</p>
**Extremely long runtime/unneeded if all spotify-{Type}.csv exists**</p>
Dependencies: make_video_data_files</p>

##### make_genre_charts
Visualizes genre data for each personality</p>
Dependencies: make_genre_files</p>

##### make_youtube_categories_chart
Visualizes the distribution of youtube categoies for all types</p>
Dependencies: make_video_data_files</p>

##### make_genre_charts_per_indicator
Visualizes genre data by indicator</p>
Dependecies: make_genre_files</p>

### Pronoun Anaylsis

#### pronouns_analysis.py

##### main
Visualizes the usages for pronouns in the 1st/2nd/3rd person</p>
Dependencies: none</p>

### Word and Sentiment Analysis

#### word_cloud.py 

##### pre_process_data
Preprocesses and cleans the text by removing links, punctuation and lower case</p>
Dependencies: none</p>

##### generate_wordcloud_tfidf
Visualizes most commons words across all personality types</p>
Dependencies: pre_process_data</p>

#### sentiment_visualization.py

##### run_vader
Generates a dictionary of sentiment scores</p>
Dependencies: none</p>

##### get_sentiment_of_sentence
Returns sentiment for a particular sentence</p>
Dependencies: run_vader</p>

##### get_sentiments
Creates result_dict that contains number of positive, negative and neutral sentiments for each personality type</p>
Dependencies: get_sentiments_of_sentence

##### dump_result_dict
Dumps the dictionary into a pickle file</p>
Dependencies: get_sentiments</p>

##### load_result_dict
Load the dictionary from a pickle file</p>
Dependencies: dump_result_dict</p>

##### plot_sentiment_pies_charts
Plots pie charts, showing percentage of each sentiment type for each personality type</p>
Dependencies: load_result_dict</p>

### User Count analysis

#### mbti_visual_basic.py

##### Script
Visualizes the number of users per personality type and their average words per comment </p>
Dependencies: none</p>

### Libraries Used
<ul>
<li>numpy</li>
<li>pandas</li>
<li>re</li>
<li>nltk</li>
<li>sklearn</li>
<li>wordcloud</li>
<li>spacy</li>
<li>matplotlib</li>
<li>pickle</li>
<li>seaborn</li>
<li>vader</li>
<li>pafy</li>
<li>spotipy</li>
</ul>