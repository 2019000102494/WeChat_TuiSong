# Wecat_tuisong  公众号推送模板
最近抖音的情侣推送天气有点火，顺手用python写了一个模板的发送；不只是普通模板和天气，咱们可以在网上找api修改模板的内容，自定义比如每日星座运势、搞笑段子等。
api尽量在网上找到免费、免验证的。

网上看见了php完成的推送天气代码，一朋友一直说py写不了，那我就写写吧(什么歪理~_~)。


### test.py 测试用的
可以收到通知，自定义内容

#### 1、首先访问 https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login
登录后台得到appID 和 appsecret  分别填入test.py文件中
![image](https://user-images.githubusercontent.com/110412182/186095663-3146adbf-a6e3-4e55-8add-41079d77b870.png)
写到这
![image](https://user-images.githubusercontent.com/110412182/186095557-18b10574-e5ec-49f2-9cd7-31abe1f74675.png)


#### 2、新建的模板 (用于test.py)
```
{{first.DATA}}
测试1：{{keyword1.DATA}}
测试2：{{keyword2.DATA}}
测试3：{{keyword3.DATA}}
测试4：{{keyword4.DATA}}
测试5：{{remark.DATA}}
```
![image](https://user-images.githubusercontent.com/110412182/186095313-44742895-21a5-4ac7-b865-76ac96523ff5.png)
写到这；扫二维码关注后可以看见多了用户的微信号信息，放到touser里就好。
![image](https://user-images.githubusercontent.com/110412182/186095797-1064d417-f37b-4797-8793-f1af13dd2863.png)

#### 3、效果
![image](https://user-images.githubusercontent.com/110412182/186096703-ad0b6622-addc-4121-a8c2-93f8446e2d74.png)


### tianqi.py  天气推送
最近还在忙，等我写好了再发出来

忙好了，大概效果是这样的

![image](https://user-images.githubusercontent.com/110412182/186146560-1f14c54b-61f3-4937-bc95-0d0e308bb855.png)

别的功能大噶酌情增加吧

模板名称用到的颜文字 ʕ•ᴥ•ʔ
```
{{first.DATA}} 
{{keyword1.DATA}} 
{{keyword2.DATA}} 
{{keyword3.DATA}} 
{{keyword4.DATA}}
{{remark.DATA}} 
```

运行
```
python3 tianqi.py
```
![image](https://user-images.githubusercontent.com/110412182/186146991-9e4453d3-02c6-4825-8ad1-a06cf7353003.png)

然后在linux服务器中或者云函数里写一个定时任务就好了

0 8 * * * 

