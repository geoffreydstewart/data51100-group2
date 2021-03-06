# -*- coding: utf-8 -*-
"""
This program computes loads the PUMS dataset and prepares some visualizations based on the data
Students:   Jenna Lopes, Geoffrey Stewart, Ryan Wade
Date:       Feb. 24, 2020
Course:     DATA-51100-002: 	Statistical Programming
Semester:   Spring 2020
Assignment: PROGRAMMING ASSIGNMENT #6
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def hhl_plot(fig, df):
    hhl = df['HHL'].value_counts()

    # define the legend labels
    languages = ['English only',
                 'Spanish',
                 'Other Indo-European languages',
                 'Asian and Pacific Island languages',
                 'Other language']

    # create the pie chart
    ax = fig.add_subplot(2, 2, 1)
    ax.axis('equal')
    ax.pie(hhl, startangle=-117)
    ax.set_ylabel('HHL', fontsize=9)
    # add the legend
    ax.legend(languages, loc='upper left', bbox_to_anchor=(0, 0.95), prop={'size': 8.5})

    # add the title
    plt.title('Household Languages')


def income_plot(fig, df):
    # filter out missing data
    hincp = df.HINCP[df.HINCP.notna()]

    ax = fig.add_subplot(2, 2, 2)
    bins = np.logspace(1, 7, num=100, base=10)

    # create the histogram
    ax.hist(x=hincp, density=True, bins=bins, histtype='bar', color='g', linewidth=0.6, alpha=0.5)
    plt.xscale('log', nonposx='clip', subsx=[1, 2, 3, 4, 5, 6, 7])
    # add the kernel density estimate plot
    hincp.plot(kind='kde', color='k', ls='dashed')
    ax.grid(False)

    # add labels and title
    plt.ylabel('Density')
    plt.xlabel('Household Income ($) - Log Scaled')
    plt.title('Distribution of Household Income')


def vehicle_plot(fig, df):
    # aggregate the data
    veh = df.groupby('VEH').aggregate({'WGTP': 'sum'})

    ax = fig.add_subplot(2, 2, 3)
    # create the bar chart
    ax.bar(veh.index, veh.WGTP / 1000, align='center', color='red', tick_label=[int(x) for x in veh.index])
    ax.margins(0, 0.04)
    # add labels and title
    plt.ylabel('Thousands of Households')
    plt.xlabel('# of Vehicles')
    plt.title('Vehicles Available in Households')


def taxes_plot(fig, df):
    # create the mapping between the TAXP to $ value
    mapping={1: 0, 2: 1, 3: 50, 63: 5500, 64: 6000, 65: 7000, 66: 8000, 67: 9000, 68: 10000}
    for i in range(4, 63):
        if i < 23:
            mapping[i] = mapping[i-1] + 50
        else:
            mapping[i] = mapping[i-1] + 100

    # replace the value of TAXP with the mapping value
    df['TAXP'].replace(mapping, inplace=True)

    ax = fig.add_subplot(2, 2, 4)
    # create the scatter plot
    plt.scatter(df['VALP'], df['TAXP'], c=df['MRGP'], s=df['WGTP'], alpha=0.25, cmap='seismic')
    plt.colorbar(ticks=[0, 1250, 2500, 3750, 5000]).set_label('First Mortgage Payment (Monthly $)')
    plt.ylim(ymin=0, ymax=10400)
    plt.xlim(xmin=0, xmax=1200000)

    # add labels and title
    plt.xlabel('Property Value ($)')
    plt.ylabel('Taxes ($)')
    plt.title('Property Taxes vs. Property Values')


def main():
    # Create the figure
    fig = plt.figure(figsize=(15, 8))
    plt.subplots_adjust(wspace=.2, hspace=.4)

    # Read the csv file
    df = pd.read_csv("ss13hil.csv")

    # Add the plots to the figures
    hhl_plot(fig, df)
    income_plot(fig, df)
    vehicle_plot(fig, df)
    taxes_plot(fig, df)

    # Export to png file
    plt.savefig('pums.png')


if __name__ == "__main__":
    print('DATA-51100, Spring 2020')
    print('NAMES: Jenna Lopes, Geoffrey Stewart, Ryan Wade')
    print('PROGRAMMING ASSIGNMENT #6')
    main()
