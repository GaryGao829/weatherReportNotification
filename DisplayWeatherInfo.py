import requests
import sys
import time

#reload(sys)
#sys.setdefaultencoding("utf-8")

#print time.strftime("%Y-%m-%d %X",time.localtime())

ApiUrl = \
    "http://www.weather.com.cn/data/sk/101190401.html"

r = requests.get(ApiUrl)

weatherinfo = r.json
print "City: " + weatherinfo["weatherinfo"]["city"]
print "Temperature: " + weatherinfo["weatherinfo"]["temp"]
print "Winds from the: " + weatherinfo["weatherinfo"]["WD"] + weatherinfo["weatherinfo"]["WS"]
print "Humidity: " + weatherinfo["weatherinfo"]["SD"]
#print "Time: " + weatherinfo["weatherinfo"]["time"]

