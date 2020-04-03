from mpl_toolkits.basemap import Basemap

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

puzzle = pd.read_csv('puzzle.csv', header=None)
puzzle.columns = ['Lon','Lat']

radiansToDegrees = 180/np.pi
puzzle = puzzle.mul(radiansToDegrees)

m = Basemap(projection='robin',lon_0=0,resolution='c')
m.drawcoastlines()
m.drawparallels(np.arange(-90.,120.,30.))
m.drawmeridians(np.arange(0.,360.,60.))
m.fillcontinents(color='beige',lake_color='lightblue')
m.drawmapboundary(fill_color='lightblue')
puzzle['Lat'], puzzle['Lon'] = m(list(puzzle['Lat']),list(puzzle['Lon']))
plt.plot(puzzle['Lat'],puzzle['Lon'], 'ro', marker='.', markersize=1.2)
plt.title("Flight Locations")
plt.show()