# Last updated 8 July, 2020
# Created by David Shuster

'''
This program parses and graphs some simple data on Religiosity (%) vs. GDP per capita (USD) for 148 Countries.
'''

import csv
import matplotlib.pyplot as plt

def main():
    f = open('religion_vs_GDP_per_Capita.csv', 'r')
    GDP = [] #per capita in USD
    reli = [] #religiosity as a %
    for line in f.readlines()[1:]:
        line = line.split(",")
        GDP.append(int(line[3][0:-1]))
        reli.append(int(line[2]))
    f.close()

    plt.scatter(GDP, reli)
    plt.xlabel('Nation\'s GDP per capita (USD)')
    plt.ylabel('Nation\'s Religiosity (%)')
    plt.title('Religiosity (%) vs. GDP per capita (USD) for 148 Countries')
    plt.show()

if __name__ == '__main__':
    main()


'''
SOURCES
Data is taken from https://www.kaggle.com/dimanjung/religions-vs-gdp-per-capita/data. Accessed 8 July, 2020.


ACKNOWLEDGEMENTS
Thanks to https://www.kaggle.com/dimanjung/religions-vs-gdp-per-capita/data for the data!
Thanks to https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/ for the helpful instructions.
'''