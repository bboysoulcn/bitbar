#!/Users/bboysoul/.pyenv/versions/3.7.4/bin/python
import requests
import json
import os

xinzhi_public_key = ""
xinzhi_secret_key = ""
location = "宁波"
language = "zh-Hans"
unit = "c"

# 获取温度
def get_temperature():
    api_url = "https://api.seniverse.com/v3/weather/now.json?key=" + xinzhi_secret_key + "&location="+ location +"&language=" + language +"&unit=" + unit
    res = requests.get(api_url)
    res_content = json.loads(res.text)
    temperature = res_content["results"][0]["now"]["temperature"]
    weather_text = res_content["results"][0]["now"]["text"]
    weather = []
    weather.append(temperature)
    weather.append(weather_text)
    return weather


if __name__ == '__main__':
    weather = get_temperature()
    temperature = weather[0]
    weather_text = weather[1]
    print("温度: " + temperature + "c 天气: " + weather_text)





