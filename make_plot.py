'''
This script is an example of an interpolated contour plot for the 
given lat, long, z station corrdinates and height (data value)
Example data and cities are given for North Dakota

Author Cody R. Gette

'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from mpl_toolkits.basemap import Basemap, cm
from metpy.gridding.gridding_functions import interpolate, remove_nan_observations
from metpy.units import units
import matplotlib
from geopy.geocoders import Nominatim
import os


def plot_map(df, date, value, cbarlabel='', title='', cmap="Spectral_r", zmin=0,zmax=100, save=False):
    
    cities = ['Williston', 'Minot', 'Grand Forks', 'Fargo', 'Bismarck', 'Devils Lake']
    fig, ax = plt.subplots(figsize=(15,10))

    to_plot = df[df["Date"]==date]
    lon = to_plot['Longitude (deg)'].values
    lat = to_plot['Latitude (deg)'].values

    #make basemap map
    print("Making map...")
    m = Basemap(
        llcrnrlon=min(lon),
        llcrnrlat=min(lat),
        urcrnrlon=max(lon),
        urcrnrlat=max(lat),
        projection='merc',
        resolution='h')
    
    #Convert lon, lat to map coordinates and mask any missing points
    xp, yp = m(lon,lat)
    x_masked, y_masked, z = remove_nan_observations(xp, yp, to_plot[value].values)

    print("Interpolating data...")
    #Uncomment one of the interpolation methods below. rbf is chosen as a default
    
    #linear
    #gridx, gridy, z = interpolate(x_masked, y_masked, z, interp_type='linear', hres=5000)
    
    #rbf
    gridx, gridy, z = interpolate(x_masked, y_masked, z, interp_type='rbf', hres=5000, rbf_func='linear',
                          rbf_smooth=0)
        
    #cressman
    #gridx, gridy, z = interpolate(x_masked, y_masked, z, interp_type='cressman', minimum_neighbors=1, hres=5000,
                          #search_radius=100000)
    
    #barnes
    #gridx, gridy, z = interpolate(x_masked, y_masked, z, interp_type='barnes', hres=5000,
                          #search_radius=100000)
    #Natural neighbor
    #gridx, gridy, z = interpolate(x_masked, y_masked, z, interp_type='natural_neighbor', hres=5000)
    

    z = np.ma.masked_where(np.isnan(z), z)

    #Find max and min of z if not input manually
    if zmax=='max':
        zmax=np.max(z)
    if zmin=='min':
        zmin=np.min(z)

    #normalize colormap
    cmap = plt.get_cmap(cmap)
    norm = Normalize(vmin=zmin, vmax=zmax)

    #Draw map lines
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
   
    #Set contour line parameters. must be integers
    low = int(round(np.min(z)))
    high = int(round(np.max(z)))
    step = int(round((high-low)/10))

    #Set step at least 2 so there are not contour lines set for every increase of 1 (unless that's what you want)
    if step<2:
        step=2

    #plot colormesh
    mmb = m.pcolormesh(gridx, gridy, z, cmap=cmap, norm=norm)
    cbar= m.colorbar(mmb, location='bottom')
    cs = m.contour(gridx, gridy, z, colors='k', levels=list(range(low, high, step)), alpha=0.3)
    plt.clabel(cs, inline=1, fontsize=12, fmt='%i')

    #Plot city markers
    geolocator = Nominatim()
    for city in cities:
        loc = geolocator.geocode(city)
        x, y = m(loc.longitude, loc.latitude)
        m.plot(x,y,marker='o',color='None',markeredgecolor='k', markersize=8)
        plt.text(x+10000, y+5000, city,fontsize=12, alpha = 0.7)


    m.drawcounties()
    cbar.set_label(cbarlabel)
    plt.title(title, fontsize=18)
    
    if save:
        # Make sure a directory exists for the gdd data
        print("Checking for file pathways...")
        if not os.path.isdir("./maps"):
            os.mkdir('maps')
        print("Saving figure...")
        fig.savefig('./maps/'+str(title)+'.png', format='png')

    return m

