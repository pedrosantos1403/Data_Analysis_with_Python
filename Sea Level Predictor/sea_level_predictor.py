import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():

    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b')

    # Creating array of years
    future_years = np.arange(2014,2051)
    years = np.concatenate([df['Year'], future_years])
    years_second = np.arange(2000, 2051)

    # Calculating first line of best fit
    best = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Calculating second line of best fit
    best_second = linregress(df.iloc[120:]['Year'], df.iloc[120:]['CSIRO Adjusted Sea Level'])

    # Ploting first line of best fit
    plt.plot(years, best.intercept + best.slope*years, label='best fit (all)', color='r')

    # Ploting second line of best fit (2000 - 2050)
    plt.plot(years_second, best_second.intercept + best_second.slope*years_second,
             label='best fit (2000)', color='g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()