import urllib, json, time
import pandas as pd
from pandas.io.json import json_normalize

url = "http://citibikenyc.com/stations/json"
updateTime='intial time'
prevTime='last recorded time'

while True:
    try:
        response = urllib.urlopen(url)
        data = json.loads(response.read())
    except (IOError,ValueError) as e:
        print 'ERROR:',e,' at time:',updateTime
    df=json_normalize(data['stationBeanList'])
    updateTime = data['executionTime']
    df['time']=updateTime
    if updateTime != prevTime: #only want to update maindf if the time has changed
        prevTime=updateTime #now prevTime is set to the current updateTime
     	df.to_csv('data/citibike_data.csv',header=False, mode='a')
    time.sleep(60)
