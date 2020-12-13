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
