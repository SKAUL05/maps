# Created by sarathkaul on 04/02/20
# pylint: disable=import-error

"""
Data Driven Maps with Folium and Leaflet.js
"""

import os
import json
import folium

# Create map object
_MAP_OBJECT = folium.Map(location=[32.95, 74.87], zoom_start=12)

# Global tooltip
_TOOLTIP = "Click For More Info"

# Create custom marker icon
_LOGO_ICON = folium.features.CustomIcon("logo.jpg", icon_size=(30, 30))

# Vega data
_VIS = os.path.join("data", "vis.json")

# Geojson data
_OVERLAY = os.path.join("data", "overlay.json")

# Create markers
folium.Marker(
    [32.95277692166277, 74.87466583251953],
    popup="<strong> Location One </strong>",
    tooltip=_TOOLTIP,
).add_to(_MAP_OBJECT)

folium.Marker(
    [32.85277692166277, 74.87466583251953],
    popup="<strong> Location Two </strong>",
    tooltip=_TOOLTIP,
    icon=folium.Icon(icon="cloud"),
).add_to(_MAP_OBJECT)

folium.Marker(
    [32.75289692166277, 74.77486583251953],
    popup="<strong> Location Three </strong>",
    tooltip=_TOOLTIP,
    icon=folium.Icon(color="purple"),
).add_to(_MAP_OBJECT)

folium.Marker(
    [32.7345692166277, 74.76462583251953],
    popup="<strong> Location Four </strong>",
    tooltip=_TOOLTIP,
    icon=folium.Icon(color="green", icon="leaf"),
).add_to(_MAP_OBJECT)

folium.Marker(
    [32.752222692166277, 74.77422283251953],
    popup="<strong> Location Five </strong>",
    tooltip=_TOOLTIP,
    icon=_LOGO_ICON,
).add_to(_MAP_OBJECT)

folium.Marker(
    [32.75677672166277, 74.77466583241953],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open(_VIS)), width=450, height=250)
    ),
).add_to(_MAP_OBJECT)


# Circle marker
folium.CircleMarker(
    location=(32.75277692166277, 74.77466583251953),
    radius=50,
    popup="My Birthplace",
    color="#428bca",
    fill=True,
    fill_color="#428bca",
).add_to(_MAP_OBJECT)

# Geojson overlay
folium.GeoJson(_OVERLAY, name="Jammu Tawi").add_to(_MAP_OBJECT)

# Generate map
_MAP_OBJECT.save("./html/index.html")
