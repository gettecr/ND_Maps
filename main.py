'''
This script is the main function for an example of an interpolated contour plot for the 
given lat, long, z station corrdinates and height (data value)
Example data and cities are given for North Dakota. Plots are made of elevation, accumulated GDDs,
and Devaition of GDDs from 5 year average. Other data included in data file are rainfall, min temp and max temp 

Data was retrieved from NDAWN for 2017 May - September

Author Cody R. Gette

'''


import pandas as pd
from make_plot import plot_map


#dates use fmt YYYY-mm-dd
test_date = '2017-09-15'

def main():
    
    data = pd.read_csv("NDCornGDD_data_counties.csv")

    #Make plot of accumulated growing degree days for test_date
    
    plot_map(data, test_date, 'Corn AGDD (F)',
                     cbarlabel='Accumulated Corn GDD '+test_date,
                     title='Corn Growing Season GDDs 2017',
                     zmin=100, zmax=2800, save=True)
    
    #Make plot of deviation of growing degree days from 5 year average
    plot_map(data, test_date, 'Delta GDD (5yr)',
                     cbarlabel='Delta GDD', title='Deviation from 5yr average '+test_date,
                     cmap="coolwarm", zmin=-300, zmax=300, save=True)

    #Plot interpolated elevation for North Dakota (note, date is irrelevant here)
    plot_map(data, test_date, 'Elevation (ft)',
                 cbarlabel='Elevation (ft)', title='Elevation Map',
                 cmap="gist_earth",zmin=0, zmax='max', save=True)

    



if __name__ == "__main__":
   
    main()
