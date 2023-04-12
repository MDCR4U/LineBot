#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

import json

import urllib.request
#https://www.learncodewithmike.com/2020/07/line-bot-buttons-template-message.html
#https://ithelp.ithome.com.tw/articles/10195640
# study postback 
#actions=[
#                                    PostbackTemplateAction(
#                                        label='台北市',
#                                        text='台北市',
#                                        data='A&台北市'
#                                    ),

def text_20(msg):     # 2 text, 0URL
     
    file = open('config.txt','r',encoding="utf-8")
    line = file.readline().strip('\n')    #line1 githubid
    line = file.readline().strip('\n')   #line1 githubproject
    line = file.readline().strip('\n')   #line1 githubproject
    #line=line.strip('\n')
    wsftpflr= line[12:].strip()

    wsmsg = msg.split('#')
    
    wjson_file = wsmsg[1] + ".json"
# 讀取 JSON 檔案  local
#   # with open("cbd.json" , "r") as f:
    #with open(wjson_file , "r") as f:
    #    js_dta = json.load(f)

    url = wsftpflr + "json/" + wjson_file #http://www.abc.com/cust.json"
    print(url)
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)

    text1       = js_dta["text1"]

    message = TextSendMessage(text= text1)
     
 

    print(message)
    return message


