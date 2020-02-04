# Created by sarathkaul on 04/02/20

# Enter file description here

import folium
import os
import json

# Create map object
map = folium.Map(location=[42.3601, -71.0589],zoom_start=12)

# Global tooltip
tooltip = "Click For More Info"

# Create custom marker icon
logo_icon = folium.features.CustomIcon('logo.jpg',icon_size=(30,30))

# Vega data
vis = os.path.join('data','vis.json')

# Create markers
folium.Marker([42.363600, -71.099500], popup='<strong> Location One </strong>',
              tooltip=tooltip).add_to(map)

folium.Marker([42.333600, -71.199500], popup='<strong> Location Two </strong>',
              tooltip=tooltip, icon = folium.Icon(icon='cloud')).add_to(map)

folium.Marker([42.377120, -71.097500], popup='<strong> Location Three </strong>',
              tooltip=tooltip, icon = folium.Icon(color='purple')).add_to(map)

folium.Marker([42.263600, -71.099500], popup='<strong> Location Four </strong>',
              tooltip=tooltip, icon = folium.Icon(color='green',icon = 'leaf')).add_to(map)

folium.Marker([42.273600, -71.199500], popup='<strong> Location Five </strong>',
              tooltip=tooltip, icon = logo_icon).add_to(map)

folium.Marker([42.334600, -71.099500], popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)),width=450, height=250))).add_to(map)



# Circle marker
folium.CircleMarker(
    location=(42.46670, -70.34567),
    radius = 50,
    popup = "My Birthplace",
    color = "#428bca",
    fill = True,
    fill_color = "#428bca"
).add_to(map)

# Generate map
map.save('map.html')