import urllib, json, time
import pandas as pd
import datetime as dt
from pandas.io.json import json_normalize

url = "http://citibikenyc.com/stations/json"
maindf = pd.DataFrame() #this will be the main dataframe that gets appended to.
updateTime='intial time'
prevTime='last recorded time'
count=0
while dt.date.today().year == 2014:
    try:
        response = urllib.urlopen(url)
        data = json.loads(response.read())
    except (IOError,ValueError) as e:
        print 'ERROR:',e,' at time:',updateTime
    df=json_normalize(data['stationBeanList'])
    updateTime = data['executionTime']
    df['time']=updateTime
    if updateTime != prevTime: #only want to update maindf if the time has changed
        maindf=maindf.append(df,ignore_index=True)
        prevTime=updateTime #now prevTime is set to the current updateTime
        if count%10==0:
            maindf.to_csv('/home/deena/citibike_data/citibike'+updateTime.replace(' ','-')+'.csv')
        count += 1
    time.sleep(60)
    