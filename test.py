# -*- coding: utf-8 -*-
# @Author: Toufu
# @Date:   2022-08-23 13:05:28

import requests,json

def token(AppId,AppSecret):  #调用开发者的api 得到token
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}'.format(AppId,AppSecret)
    r=requests.get(url)
    print(r.text)
    data = json.loads(r.text)
    print(data["access_token"])
    return data["access_token"]

def send(t):   #带着token去发包
    print(t)
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={0}'.format(t)
    data = {
    "touser":"",  #填收信人的ID 她关注后 后台可以看见
    "template_id":"",  #填模板的ID 后台创建模板后可以看见
    #"url":"http://weixin.qq.com/download",
    "topcolor":"#FF0000",
    "data":{
            "first": {
                "value":"没问题吧",
                "color":"#000"
            },
            "keyword1":{
                "value":"简简单单",
                "color":"#000"
            },
            "keyword2":{
                "value":"好好读书",
                "color":"#000"
            },
            "keyword3":{
                "value":"不要想七想八",
                "color":"#000"
            },
            "keyword4":{
                "value":"respect",
                "color":"#000"
            }
}
}
    res = requests.post(url=url,data=json.dumps(data))
    print(res.text)

if __name__ == '__main__':
    Appid = ""
    AppSecret = ""
    t = token("Appid","AppSecret") #填写开发者的appid和appsecret
    send(t)
