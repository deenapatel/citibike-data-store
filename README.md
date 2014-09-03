citibike-data-store
===================
Citibike has a json feed that displays the number of empty bikes and docks at each station in the system at the present time. They do not provide any information on past times. 
This python script is used to download citibike streaming json data, add it onto an existing datatable and save in .csv format. The dataframe is constantly added to, so it contains the full history of json downloads since the script was started. Once every 10 updates to the dataframe, the dataframe is saved as a .csv file, named with the timestamp of the last update.
