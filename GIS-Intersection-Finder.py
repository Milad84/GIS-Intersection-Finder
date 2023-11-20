#-------------------------------------------------------------------------------
# Name:       GIS Intersection Finder
# Purpose:    The code in the "GIS-Intersection-Finder" project serves the purpose of
#             Identifying intersecting streets and calculating the closest intersections for given 
#             spatial data, specifically designed for the context of a GIS analysis in the Austin, Texas, area. 
#             The analysis is conducted using GeoPandas and Shapely libraries in Python, 
#             allowing users to explore and visualize the relationships between road networks and 
#             speed management projects in the region. The provided scripts enable users to interactively
#             select target streets and obtain information about their intersections, facilitating spatial analysis in a geospatial context.
#
# Author:     Milad Korde
#
# Created:     20/11/2023
# Copyright:   (c) MohammadalizadehkorM 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import geopandas as gpd
from shapely.geometry import Point, LineString

# Load your dispersed multiline layer (speed management projects) and the street network layer into GeoDataFrames
speed_projects = gpd.read_file(r'C:\Users\MohammadalizadehkorM\Desktop\Speed Management\Speed Management Study Areas.shp')
street_network = gpd.read_file(r'C:\Users\MohammadalizadehkorM\Desktop\CTN\CTN.shp')

# Set the CRS to EPSG:2277
speed_projects.crs = 'EPSG:2277'
street_network.crs = 'EPSG:2277'

# Function to find intersecting streets for a given row
def find_intersecting_streets(row):
    return street_network[street_network.intersects(row['geometry'])]['FULL_STREE'].tolist()

# Find the intersecting streets for each speed project using the original geometry
speed_projects['intersecting_streets'] = speed_projects.apply(find_intersecting_streets, axis=1)

# Define a buffer distance for finding closest intersections (adjust as needed)
initial_buffer_distance = 300  # You can experiment with different initial buffer distances

# Function to find the closest intersection for a given row and end (start or end)
def find_closest_intersection(row, end):
    # Get the centroid of the polygon
    point = row['geometry'].centroid if row['geometry'].geom_type == 'Polygon' else Point(row['geometry'].coords[0] if end == 'start' else row['geometry'].coords[-1])

    # Set the initial buffer distance
    buffer_distance = initial_buffer_distance

    # Iterate until an intersection or street is found
    while True:
        buffer = point.buffer(buffer_distance)
        if street_network.intersects(buffer).any():
            break
        buffer_distance += 50  # Increase the buffer distance (adjust as needed)

    return street_network[street_network.intersects(buffer)]['FULL_STREE'].tolist()

# Find the closest intersections for each speed project
speed_projects['closest_intersection_start'] = speed_projects.apply(lambda row: find_closest_intersection(row, 'start'), axis=1)
speed_projects['closest_intersection_end'] = speed_projects.apply(lambda row: find_closest_intersection(row, 'end'), axis=1)

# Save the result to a CSV file
speed_projects.to_csv(r'C:\Users\MohammadalizadehkorM\Desktop\Speed Management\SpeedManResWithStreetsAndClosest.csv', index=False)
