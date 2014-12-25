import urllib, time, os.path
import simplejson as json
import pandas as pd
from pandas.io.json import json_normalize

url = "http://citibikenyc.com/stations/json"
updateTime='current time'
prevTime='last recorded time'

#checks first to see if the file exits
if not os.path.exists('data/citibike_data.csv'):
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    df=json_normalize(data['stationBeanList'])
    updateTime = data['executionTime']
    df['time']=updateTime
    prevTime=updateTime
    df.to_csv('data/citibike_data.csv')#writes a new file to disk
    time.sleep(60)
    
#this keeps adding on to the file, infinite loop
while True:
    try:
        response = urllib.urlopen(url)
        data = json.loads(response.read())
    except (IOError,ValueError) as e:
        print 'ERROR:',e,' at time:',updateTime
    except:
        print 'other ERROR at time:',updateTime
    try:    
	df=json_normalize(data['stationBeanList'])
    	updateTime = data['executionTime']
    	df['time']=updateTime
    	if updateTime != prevTime: #only want to update if the time has changed
            prevTime=updateTime
     	    df.to_csv('data/citibike_data.csv',header=False, mode='a')
   	time.sleep(60)
    except (IOError,ValueError) as e:
        print 'ERROR:',e,' at time:',updateTime
    except:
        print 'other ERROR at time:',updateTime
