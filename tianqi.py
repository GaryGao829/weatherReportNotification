import requests
import sys
import time

reload(sys)
sys.setdefaultencoding("utf-8")



ApiUrl = \
    "http://www.weather.com.cn/data/cityinfo/101190401.html"

r = requests.get(ApiUrl)

weatherinfo = r.json
tianqi = time.strftime("%Y-%m-%d %X",time.localtime()) + " City: " + weatherinfo["weatherinfo"]["city"] + " Weather: " + weatherinfo["weatherinfo"]["weather"]+ " Lowest Temperature: " + weatherinfo["weatherinfo"]["temp1"]+ " Highest Temperature: " + weatherinfo["weatherinfo"]["temp2"]


