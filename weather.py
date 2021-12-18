#!python
print("Content-Type: text/html; charset=utf-8\n")
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import requests
import json

response = requests.get("http://api.weatherapi.com/v1/current.json?key=0bf0490714354e3ea5781347211712&q=Seoul&aqi=yes")
jsonobj=json.loads(response.text)
update_time=jsonobj["current"]["last_updated"]
Seoul_is_day=jsonobj["current"]["is_day"] #day면 1
if Seoul_is_day==1:
    Seoul_daynight="day"
else:
    Seoul_daynight="night"
Seoul_temp=jsonobj["current"]["temp_c"]
Seoul_feeltemp=jsonobj["current"]["feelslike_c"]
Seoul_wind=round(jsonobj["current"]["wind_kph"]/3.6,1)
Seoul_precip=jsonobj["current"]["precip_mm"]
Seoul_cloud=jsonobj["current"]["cloud"]
Seoul_humidity=jsonobj["current"]["humidity"]
Seoul_condition_text=jsonobj["current"]["condition"]["text"]
Seoul_condition_icon=jsonobj["current"]["condition"]["icon"]

print('''<!doctype html>
<html>
<head>
  <title>DK studio</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1><a class="Title" href="index.html">DK studio</a></h1>
  <div class="grid">
    <div class="contents">
      <ol>
        <li><a href="aboutme.html">개발자 소개</a><br></li>
        <li><a href="playlist.html">Playlist</a><br></li>
        <li><a href="weather.py" id="active">현재 서울 날씨</a></li>
      </ol>
    </div>
    <div class="article">
    <h2>{update_time}, 
    서울 기준</h2>
    <p style="text-align: center; " align="center">
    기온: {temp}℃</p><p style="text-align: center; " align="center">
    날씨: {cond}</p><p style="text-align: center; " align="center">
    강수량: {prec}mm</p><p style="text-align: center; " align="center">
    풍속: {wind}m/s</p><p style="text-align: center; " align="center">
    <img src={icon} width="50px">
    </p>
    

    </div>
  </div>

</body>
</html>
'''.format(
      update_time=update_time
      ,temp=Seoul_temp
      ,cond=Seoul_condition_text
      ,prec=Seoul_precip
      ,wind=Seoul_wind
    ,icon=Seoul_condition_icon)

)
