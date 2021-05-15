#Author : Manideep Paduchuri

'''
About folium
-------------------
Python 3rd party library
Used for Data visualization in Maps
Based on strenghts of leaflet.js library
'''

import folium as fol
import pandas as pd

#Create Map object pointing to India with inital Zoom level as 4
map_obj = fol.Map(
              location = [20.5937,78.9629],
               zoom_start=4,
               min_zoom = 4,
               max_zoom = 7,
               )

#Create Faature group object
feat_grp = fol.FeatureGroup(name="India States")

#Read data from CSV using Pandas and store in data frame
states_data = pd.read_csv("Indian_States.csv")

#Store particular columns from Dataframe as series
names =  states_data['STATE']
lat   =  states_data['LATITUDE']
long  =  states_data['LONGITUDE']

#Add each State / UT to feature group
for name_each, lat_each, long_each in zip(names,lat,long):
    feat_grp.add_child(
        fol.Marker(
            location = [lat_each,long_each], 
            popup    = name_each,
            icon     = fol.Icon(color="green"),
            )
        )

#Add feature group to map
map_obj.add_child(feat_grp)
