# Larry on Fire

### Project Overview

This was a capstone group-project I did with 3 fellow students. The goal was to develop and application that would give the users the ability to visualize when people tweet about California wildfires. Our application does this by allowing users to analyze the evolution over time while offering several filters to interact with the data. In detail, we produced the following interactive visualization:

1. Map locating the wildfires over time
2. Line chart plotting the number of tweets and acres burned per week
3. Wordcloud with the most frequent words found in the tweets
4. Topic modeling form the tweets

My main task was to implement the line chart (code in ´ui/line_chart.py´) and set up the code for the virtual environment (code in ´install.sh´). However, I also helped my teammates debug whenever needed. Please use the instructions below to interact with the application.

### Installing the Application

1. Run `bash install.sh` in the top-level directory, this will install all required libraries in a virtual environment
2. Enter the virtual environment with `source virtual_larry/bin/activate`
3. Launch the dash server with `ipython3 larry_on_fire.py` and click on the link displayed in the output

*Notes:*
* Please run this application locally for optimal performance.
* When initially loading the application, it can take about a minute.
* When using the filters in the browser, the application takes a few seconds to reload, especially when loading tweets from the entire country.

### Interacting with the Application

Once the three steps above are executed, one can interact with the application on the web browser by toggling three things:

* Year (dropdown menu)
* Season (button)
* Geography (button)

The prior two apply to all 4 visualizations, while the last filter only applies to the wordcloud and LDA. This allows the user to (1) locate the fires, (2) look at the tweet intensity compared to the wildfire intensity, and (3) get an overview of the discussed topics.

### Interacting with the API

1. Run `ipython3 api_interaction.py` in the top-level directory
2. Enter a start and an end date in the command line (format: YYY-MM-DD)
3. View the output of the API in `data/twitter_data/simulation.csv`
