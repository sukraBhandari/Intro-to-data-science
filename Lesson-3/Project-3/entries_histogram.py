import numpy as np
import pandas
import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, lets 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Why don't you plot two histograms on the same axes, showing hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()
    
    Your histograph may look similar to the following graph:
    http://i.imgur.com/9TrkKal.png
    
    You can read a bit about using matplotlib and pandas to plot
    histograms:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
    
    You can look at the information contained within the turnstile weather data at the link below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
    #print turnstile_weather
    plt.figure()
    entry_while_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 1]
    entry_no_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] != 1]
    
    entry_no_rain.hist(bins=180, alpha = 0.8, color='blue')
    entry_while_rain.hist(bins=180,  alpha = 0.8, color='green')
    plt.xlabel('Hourly ENtries')
    plt.ylabel('frequency')
    plt.axis([0,6000, 0,45000])
    return plt
