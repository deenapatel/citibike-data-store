citibike-data-store
===================
CitibikeDataStore.py scrapes citibike's streaming json feed, which tells the number of available bikes and docks at each station. 
All data is timestamped and saved in a .csv datafile in the /data directory.
Reduction.py (available in the data directory) reads in a datafile (given by the command line: >python Reduction.py filename.csv), selects the relevent columns, and outputs the data for every 10 minutes (instead of every minute in the full file).

