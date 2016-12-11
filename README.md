# final_teamAZ
Final project for Team DEET

![alt tag](https://github.com/ksaxberg/final_teamAZ/blob/master/DEET_Logo.png)

This project aimed to predict mosquito abundance using future climate predictions and visualize mosquito 
populations from 1950 to 2099.

There are three components of the project: Data Collection, Data Analysis, and Data Visualization. 
The general workflow is outlined in DEET_Workflow.png.

A grid of 4km x 4km was overlaid on the state of interest and daily climate data for pixels that were considered developed by the The National Land Cover Database 2011 was collected from the Northwest Knowledge Network Multivariate Adaptive Constructed Analog (MACA) Method data (https://www.northwestknowledge.net/data-search).

Climate data for each latitude and longitude coordinate was run through a mosquito abundance model (https://github.com/JocelineLega/MoLS) to predict daily mosquito numbers based on near-surface air temperature, precipitation, and surface relative humidity.

Monthly average mosquito abundance was visualized using QGIS(http://qgis.org/en/site/) time manager plugin.
