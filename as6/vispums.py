# -*- coding: utf-8 -*-
"""
This program does data visualiations of various attributes from the ACS PUMS dataset
Students:   Ryan Wade, Geoffrey, Jenna
Date:       Feb. 22, 2020
Course:     CPSC-51100
Semester:   Spring 2020
Assignment: PROGRAMMING ASSIGNMENT #6
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def hh1_plot(fig, df):
    hhl = df['HHL'].value_counts()

    # create the pie chart
    ax = fig.add_subplot(2, 2, 1)
    ax.axis('equal')
    pie = ax.pie(hhl, startangle=-117)

    # add the legend
    language = ['English only',
                'Spanish',
                'Other Indo-European languages',
                'Asian and Pacific Island languages',
                'Other language']

    ax.legend(language, loc='upper left',
              bbox_to_anchor=(0.1, 0.93),
              fontsize='small')

    # add the title
    plt.title('Household Languages')

def income_plot(fig, df):
    # filter out missing data
    hincp = df.HINCP[df.HINCP.notna()]

    # create the histogram
    ax = fig.add_subplot(2, 2, 2)
    bins = np.logspace(1, 7, num=100, base=10)

    hist = ax.hist(x=hincp,
                   density=True,
                   bins=bins,
                   histtype='bar',
                   color='g',
                   linewidth=0.6)
    plt.xscale('log', nonposx='clip', subsx=[1, 2, 3, 4, 5, 6, 7])
    hincp.plot.kde(ax=ax, style='--', color = 'black', logx=True)
    ax.grid(linestyle='--')

    # add labels and title
    plt.ylabel('Density')
    plt.xlabel('Household Income ($) - Log Scaled')
    plt.title('Distribution of Household Income')

def vehicle_plot(fig, df):
    # aggregate the data
    veh = df.groupby('VEH').aggregate({'WGTP':'sum'})

    # create the bar chart
    ax = fig.add_subplot(2, 2, 3)
    ax.bar(veh.index,
           veh.WGTP / 1000,
           align='center',
           color='red',
           tick_label=[int(x) for x in veh.index])

    # add labels and title
    plt.ylabel('Thousands of Households')
    plt.xlabel('# of Vehicles')
    plt.title('Vehicles Available in Households')

def taxes_plot(fig, df):
    # create the mapping between the TAXP to $ value
    mapping={1:0,2:1,3:50,63:5500,64:6000,65:7000,66:8000,67:9000,68:10000}
    for i in range(4,63):
        if(i<23):
            mapping[i] = mapping[i-1]+50
        else:
            mapping[i] = mapping[i-1]+100

    #replace the value of TAXP with the mapping value
    df['TAXP'].replace(mapping,inplace=True)

    # create the scatter plot
    ax = fig.add_subplot(2, 2, 4)
    plt.scatter(df['VALP'],df['TAXP'],c=df['MRGP'],s=df['WGTP'],alpha=0.25,cmap='seismic')
    plt.colorbar(ticks=[0,1250,2500,3750,5000]).set_label('First Mortgage Payment (Monthly $)')
    plt.ylim(ymin=0,ymax=11000)
    plt.xlim(xmin=0,xmax=1200000)

    # add labels and title
    plt.xlabel('Property Value ($)')
    plt.ylabel('Taxes ($)')
    plt.title('Property Taxes vs. Property Values')

def main():
    # Create the figure
    fig = plt.figure(figsize=(20, 10))
    plt.subplots_adjust(wspace=.3, hspace=.3)

    # Read the csv file
    df = pd.read_csv("ss13hil.csv")

    # Add the plots to the figures
    hh1_plot(fig, df)
    income_plot(fig, df)
    vehicle_plot(fig, df)
    taxes_plot(fig, df)

    # Export to png file
    plt.savefig('pums.png')

if __name__ == "__main__":
    print("CPSC-51100, Spring 2020")
    print("Name: Ryan Wade, Geoffrey, Jenna")
    print("PROGRAMMING ASSIGNMENT #6 \n")
    main()