citibike-data-store
===================
Storing citibike data to make available for future analysis.

CitibikeDataStore.py scrapes citibike's streaming json feed which gives the number of available bikes and docks at each station at the present time. 
All data is timestamped and saved in a .csv datafile in the ./data directory.

Reduction.py (available in the data directory) reads in a datafile (given by the command line: >python Reduction.py filename.csv), selects the relevent columns, and outputs the data for every 10 minutes (instead of every minute in the full file). This is to make the datafiles easier to store and download, while still having a small enough time gap between data points.

