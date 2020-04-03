from mpl_toolkits.basemap import Basemap

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing data into pandas
puzzle = pd.read_csv('puzzle.csv', header=None)
puzzle.columns = ['Lon','Lat']

#value needed to convert radians to degrees
radiansToDegrees = 180/np.pi
puzzle = puzzle.mul(radiansToDegrees)

#splitting the dataframe into two
#assumption here is that the first half of the data is departures
#and the second half is arrivals
#fair assumption since the first half is mostly origins of USA and Europe
#and the second half has more destinations of the Caribbean, South America, etc
departures, arrivals = np.split(puzzle, 2)
arrivals = arrivals.reset_index(drop=True)
#joining the data back together into one dataframe of flights
flightData = departures.join(arrivals,lsuffix='_depart', rsuffix='_arrive')

#Using Basemap to map the point data on to a world map
m = Basemap(projection='robin',lon_0=0,resolution='c')
m.drawcoastlines()
m.drawparallels(np.arange(-90.,120.,30.))
m.drawmeridians(np.arange(0.,360.,60.))
m.fillcontinents(color='beige',lake_color='lightblue')
m.drawmapboundary(fill_color='lightblue')
puzzle['Lat'], puzzle['Lon'] = m(list(puzzle['Lat']),list(puzzle['Lon']))
plt.plot(puzzle['Lat'],puzzle['Lon'], 'ro', marker='.', markersize=1.2)
plt.title('Flight Markers')
plt.show()

plt.clf()

#Reinitializing the map data to a second map that charts out the flight paths
m = Basemap(projection='robin',lon_0=0,resolution='c')
m.drawcoastlines()
m.drawparallels(np.arange(-90.,120.,30.))
m.drawmeridians(np.arange(0.,360.,60.))
m.fillcontinents(color='beige',lake_color='lightblue')
m.drawmapboundary(fill_color='lightblue')
plt.plot(puzzle['Lat'],puzzle['Lon'], 'ro', marker='.', markersize=1.2)
#drawgreatcircle method needs to be 
for index, flight in flightData.iterrows():
    m.drawgreatcircle(flight['Lat_depart'], flight['Lon_depart'], flight['Lat_arrive'], flight['Lon_arrive'], linewidth=0.5, color='g')
plt.title('Flight Paths')
plt.show()