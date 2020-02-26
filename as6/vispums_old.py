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
import matplotlib.pyplot as plt


def main():
    # log the required output header
    print('DATA-51100, Spring 2020')
    print('NAMES: Jenna Lopes, Geoffrey Stewart, Ryan Wade')
    print('PROGRAMMING ASSIGNMENT #6')
    print('')

    df = pd.read_csv('ss13hil.csv')
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    ax1 = fig.add_subplot(2,2,1) 
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)

    hhl = df['HHL'].value_counts()
    hhl.index = ['English only', 'Spanish', 'Other Indo-European languages', 'Asian and Pacific Island languages', 'Other language']
    axes[0, 0].pie(hhl, startangle=242)
    axes[0, 0].legend(bbox_to_anchor=(-0.4, 1), loc="upper left", labels=hhl.index)
    axes[0, 0].set_title('Household Languages')
    axes[0, 0].set_ylabel('HHL')
    plt.show()

def bar_chart(ax):
    grouped = df.groupby('VEH')['WGTP'].sum()/1000
    ax.bar(grouped.index,grouped.values,width=0.9,bottom=None,color='r',align='center')
    ax.set_title('Vehicles Available in Households',fontsize=8)
    ax.set_xlabel('# of Vehicles',fontsize=8)
    ax.set_ylabel('Thousands of Households',fontsize=8)
    ax.set_xticks(grouped.index)
        
    ax3 = fig.add_subplot(2,2,3)
    bar_chart(ax3)
    ax3.tick_params(axis='both', which='major', labelsize=8)
    ax3.tick_params(axis='both', which='minor', labelsize=8)
    plt.show()
    
def scatter_plot ():
    scatter.set_title("Property Taxes vs. Property Values", fontsize = 12)
    plt.xlabel("Property Value ($)", fontsize = 10)
    plt.ylabel("Taxes ($)", fontsize = 10)
    scatter.set_xlim([0, 1200000])
    scatter.set_ylim([0, 10500])
    scatter.tick_params(labelsize = 10)

    taxp_ref = {1: 0, 2: 1}
    counter = 0
    for key in range(3, 23):
        counter += 50
        taxp_ref[key] = counter
    for key in range(23, 63):
        counter += 100
        taxp_ref[key] = counter
    for key in range(63, 65):
        counter += 500
        taxp_ref[key] = counter
    for key in range(65, 69):
        counter += 1000
        taxp_ref[key] = counter

    taxp_convert = []
    for key in data["TAXP"]:
        if taxp_ref.has_key(key):
            taxp_convert.append(taxp_ref[key])
        else:
            taxp_convert.append(np.NaN)

    mappable = scatter.scatter(data["VALP"], taxp_conv, s = data["WGTP"], c = data["MRGP"], cmap = "seismic", alpha = 0.18)
    colorbar = fig.colorbar(mappable, ticks = [1250, 2500, 3750, 5000])
    colorbar.set_label("First Mortgage Payment (Monthly $)", fontsize = 10)
    plt.show()
    
if __name__ == "__main__":
    main()
