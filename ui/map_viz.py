'''
Map Visualization of Wildfires
'''

import pandas as pd
import plotly.graph_objects as go

from resources.utils import filter_coord_data

# Map
def map_wildfires(coord_data, year, fire_season):

    coord_data = filter_coord_data(coord_data, year, fire_season)

    fig = go.Figure(go.Scattermapbox(
        mode = "lines", fill = "toself", fillcolor = "orange",
        lon = coord_data["lon"],
        lat = coord_data["lat"],
        name = "Wildfire",
        marker=go.scattermapbox.Marker(
                color = "red", size = 10),
        text = "<b>" + coord_data["fire_name"] + "</b><br>" +
                "GIS Acres: " + coord_data["gis_acres"].astype(str) + "<br>" +
                "Alarm date: " + coord_data["alarm_date"] + "<br>" +
                "Contingency date: " + coord_data["cont_date"],
        hovertemplate = "%{text}"
        ))

    fig.update_layout(
        mapbox = {'style': "stamen-terrain", 'center': {'lon': -119.4179, 'lat': 36.7783}, 'zoom': 5},
        showlegend = False,
        margin = {'l':0, 'r':0, 'b':0, 't':0})

    return fig


