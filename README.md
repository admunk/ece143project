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
Creates a dictionary of link ratios for each personality type
Dependencies: None

##### make_avg_link_chart
Visualizes link data
Dependencies: get_link_ratio

##### make_video_data_files
Creates csvs with output data for links from Youtube's API
** Extremely long runtime/unneeded if all {Type}.csv exists **
Dependencies: get_link_ratio

##### get_avg_view
Creates a dictionary of average views of youtube videos by personality
Dependecies: get_link_ratio, make_video_data_files

##### make_avg_view_chart
Visualizes view data
Dependencies: get_avg_view

#### spotify_search.py

##### make_genre_files
Creates csvs with output data for Youtube music videos from Spotify's API
** Extremely long runtime/unneeded if all spotify-{Type}.csv exists **
Dependencies: make_video_data_files

##### make_genre_charts
Visualizes genre data for each personality
Dependencies: make_genre_files

##### make_youtube_categories_chart
Visualizes the distribution of youtube categoies for all types
Dependencies: make_video_data_files

##### make_genre_charts_per_indicator
Visualizes genre data by indicator
