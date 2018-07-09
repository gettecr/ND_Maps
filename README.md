ND Maps
==============================

This project plots spacial (lat, long) data with python using Basemap

Data was retrieved from NDAWN stations
NDAWN is limited to North Dakota data only (and a few stations
in northern Minnesota)

Getting Started
--------------------------

Clone the repo and navigate to the `main.py` file.

Example data is given for north dakota and a test date.
Sample data run from 05-15-2017 to 09-30-2017

Running `python main.py` from the terminal window will generate three
plots.

Accumulated GDDs (growing degree days) for `test_date`
Deviation of Accumulated GDDs from 5yr average for `test_date`
and an elevation map 

Project Organization
------------

    ├── LICENSE
    ├─ README.md			   <- The top-level README 
    ├── main.py      	 	   <- Execute this to generate sample plots
	├── make_plot.py		   <- makes Basemap plot and interpolates given data
	├── NDCordGDD_data_counties.csv <- contains data from NDAWN
    ├── maps			   <- contains sample map outputs 
   
  

Visualization
--------
![Accumulated GDDs](./maps/Corn\ Growing\ Season\ GDDs\ 2017.png)

![Delta GDDs](./maps/Deviation\ from\ 5yr\ average\ 2017-09-15.png )

![Elevation](./maps/Elevation\ Map.png )

