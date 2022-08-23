# -*- coding: utf-8 -*-
# @Author: Toufu
# @Date:   2022-08-23 13:05:28

import requests,json

def token(AppId,AppSecret):  #调用开发者的api 得到token
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}'.format(AppId,AppSecret)
    r=requests.get(url)
    #print(r.text)
    data = json.loads(r.text)
    #print(data["access_token"])
    return data["access_token"]

def tianqi(city):
    Weather = 'https://www.yiketianqi.com/free/day?appid=79824366&appsecret=t14u0iwR&unescape=1&city={0}'.format(city) #修改为自己的城市地址、appid、appsecret
    Weatherapi = requests.get(Weather)
    W1 = json.loads(Weatherapi.text)
    #print(W1)
    ShiShiTQ = W1['wea']
    ShiShiWD = W1['tem_night']+'~'+W1['tem_day']
    return ShiShiTQ,ShiShiWD

def chp():
    qinghuaqiurl = 'https://api.shadiao.pro/chp'
    qinghuaapi = requests.get(qinghuaqiurl)
    chp = json.loads(qinghuaapi.text)
    chp1 = json.dumps(chp['data'])
    chp1 = json.loads(chp1)
    return chp1['text']

def send(t,tem1,tem2,chp):   #带着token去发包
    #print(t)
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={0}'.format(t)
    data = {
    "touser":"",  #填收信人的ID 她关注后 后台可以看见
    "template_id":"",  #填模板的ID 后台创建模板后可以看见
    #"url":"http://weixin.qq.com/download",
    "topcolor":"#FF0000",
    "data":{
            "first": {
                "value":"每个小时要起来走走哦，多喝水多喝水多喝水",
                "color":"#000"
            },
            "keyword1":{
                "value":tem1,
                "color":"#000"
            },
            "keyword2":{
                "value":tem2,
                "color":"#000"
            },
            "keyword3":{
                "value":"",
                "color":"#000"
            },
            "keyword4":{
                "value":chp,
                "color":"#000"
            }
}
}
    res = requests.post(url=url,data=json.dumps(data))
    print(res.text)

if __name__ == '__main__':
    AppID = ""   #填写开发者的appid和appsecret
    AppSecret = ""
    t = token(AppID,AppSecret)
    WD,TQ=tianqi("石狮") ##地址记得修改到你需要的地方
    WD1,TQ1=tianqi("南昌")
    tem1="\n石狮今天天气："+WD+"\n石狮今天温度："+TQ  ##文字描述也别忘了改哦
    tem2="南昌今天天气："+WD1+"\n南昌今天温度："+TQ1
    chp = chp()
    #print(chp)
    send(t,tem1,tem2,chp)  #需要去send里修改收件人信息、模板信息
