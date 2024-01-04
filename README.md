# GIS Intersection Finder

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)
![Geopandas](https://img.shields.io/badge/Geopandas-0.10.2-brightgreen.svg)
![Shapely](https://img.shields.io/badge/Shapely-2.0.0-brightgreen.svg)


A Python script for finding streets that intersect with a target line string along the same street network in a given shapefile using Geopandas.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Search by Street Name](#Search-by-Street-Name)
- [Search by Geometry Coordinates](#Search-by-Geometry-Coordinates)
- [Acknowledgments](#acknowledgments)

## Description

This repository contains Python scripts for a comprehensive Geographic Information System (GIS) analysis of speed management projects in Austin, Texas. The code leverages the GeoPandas library to perform spatial operations on a road network layer and a dispersed multi-line layer representing speed management projects. The analysis includes identifying intersecting streets, finding the closest intersections at the exterior parts of line segments, and dynamically handling variations in buffer distances. The resulting GeoDataFrame is saved and can be used for further exploration and visualization.

## Features

- Intersecting streets identification
- Dynamic buffer-based closest intersection calculation
- GeoDataFrame export for visualization and exploration

## Getting Started

### Prerequisites

Before using this script, you need to have the following prerequisites installed on your system:

- Python 3.11
- Geopandas
- Shapely

### Installation

## Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/YourUsername/GIS-Intersection-Finder.git
Navigate to the project directory:

```shell
    cd GIS-Intersection-Finder
```
Install the required Python packages:
```shell
pip install geopandas shapely
```


## Usage

1. Run the script by executing GIS-Intersection-Finder.py from the command line.

2. Explore the GeoDataFrame for intersecting streets and closest intersections.


## Examples


![image](https://github.com/Milad84/GIS-Intersection-Finder/assets/38597478/f672816f-f305-4a19-b5c3-eddcab64441e)

