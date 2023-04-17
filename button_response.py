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
def buttons_01(msg):    # 0 text, 1URL
  
    file = open('config.txt','r',encoding="utf-8")
    line = file.readline().strip('\n')    #line1 githubid
    line = file.readline().strip('\n')   #line1 githubproject
    line = file.readline().strip('\n')   #line1 githubproject
    #line=line.strip('\n')
    wsftpflr= line[12:].strip()

    wsmsg = msg.split('#')
    
    wjson_file = wsmsg[1] + ".json"
 
    url = wsftpflr + "json/" + wjson_file #http://www.abc.com/cust.json"
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
    label3     = js_dta["label3"]
    label4     = js_dta["label4"]
    url1       = js_dta["url1"]
    text2      = js_dta["text2"]
    text3      = js_dta["text3"]
    text4      = js_dta["text4"]
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
                URITemplateAction(
                    label=label1   , #"認識CBD影片介紹",
                    uri=url1     #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
                )
            ]
        )
    )

    return message
    
def buttons_10(msg):    # 1 text, 0URL   
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
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    
    text1       = js_dta["text1"]
    
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
                PostbackTemplateAction(
                            label=label1,
                            data=text1
 
                )
            ]
        )
    )

  
    return message
def buttons_10t(msg):    # 1 text, 0URL   
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
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    
    text1       = js_dta["text1"]
    
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
                MessageTemplateAction(
                    label= label1 ,  #"CBD的法律常識",
                    text=text1     #"/C20"
 
                )
            ]
        )
    )

  
    return message
def buttons_02(msg):    # 0 text, 2URL
  
    file = open('config.txt','r',encoding="utf-8")
    line = file.readline().strip('\n')    #line1 githubid
    line = file.readline().strip('\n')   #line1 githubproject
    line = file.readline().strip('\n')   #line1 githubproject
    #line=line.strip('\n')
    wsftpflr= line[12:].strip()

    wsmsg = msg.split('#')
    
    wjson_file = wsmsg[1] + ".json"
 
    url = wsftpflr + "json/" + wjson_file #http://www.abc.com/cust.json"
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
    url1       = js_dta["url1"]
    url2       = js_dta["url2"]
    text4      = js_dta["text4"]
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
                URITemplateAction(
                    label=label1   , #"認識CBD影片介紹",
                    uri=url1     #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
                ),
                URITemplateAction(
                    label=label2   , #"認識CBD影片介紹",
                    uri=url2     #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
                )                
            ]
        )
    )

    return message
def buttons_11(msg):    # 1 text, 1URL
  
    file = open('config.txt','r',encoding="utf-8")
    line = file.readline().strip('\n')    #line1 githubid
    line = file.readline().strip('\n')   #line1 githubproject
    line = file.readline().strip('\n')   #line1 githubproject
    #line=line.strip('\n')
    wsftpflr= line[12:].strip()

    wsmsg = msg.split('#')
    
    wjson_file = wsmsg[1] + ".json"
 
    url = wsftpflr + "json/" + wjson_file #http://www.abc.com/cust.json"
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
 
    url1       = js_dta["url1"]
    text2      = js_dta["text2"]
     
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
                URITemplateAction(
                    label=label1   , #"認識CBD影片介紹",
                    uri=url1  ,   #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
                ),
                PostbackTemplateAction(
                            label=label2,
                            data=text2
 
                )
            ]
        )
    )
 
    return message
def buttons_20(msg):     # 2 text, 0URL
     
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
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
    text1       = js_dta["text1"]
    text2      = js_dta["text2"]
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
                MessageTemplateAction(
                    label= label1 ,  #"CBD的法律常識",
                    text=text1 ,    #"/C20"
                ),
                MessageTemplateAction(
                    label= label2 ,  #"CBD的法律常識",
                    text=text2     #"/C20"
                
                )
            ]
        )
    )

    return message

def buttons_03(msg):    # 0 text, 3URL
  
    file = open('config.txt','r',encoding="utf-8")
    line = file.readline().strip('\n')    #line1 githubid
    line = file.readline().strip('\n')   #line1 githubproject
    line = file.readline().strip('\n')   #line1 githubproject
    #line=line.strip('\n')
    wsftpflr= line[12:].strip()

    wsmsg = msg.split('#')
    
    wjson_file = wsmsg[1] + ".json"
 
    url = wsftpflr + "json/" + wjson_file #http://www.abc.com/cust.json"
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
    label3     = js_dta["label3"]
    url1       = js_dta["url1"]
    url2       = js_dta["url2"]
    url3       = js_dta["url3"]
    text4      = js_dta["text4"]
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
                URITemplateAction(
                    label=label1   , #"認識CBD影片介紹",
                    uri=url1     #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
                ),
                URITemplateAction(
                    label=label2   , #"認識CBD影片介紹",
                    uri=url2,     #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
                ) ,               
                URITemplateAction(
                    label=label3   , #"認識CBD影片介紹",
                    uri=url3     #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
                )                

            ]
        )
    )

    return message
#def buttons_12(msg):     #1 text 2url
#def buttons_21(msg):     #2 text 1url
def buttons_30(msg):     # 3 text, 1URL   
  
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
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
    label3     = js_dta["label3"]
    label4     = js_dta["label4"]
    text1      = js_dta["text1"]
    text2      = js_dta["text2"]
    text3      = js_dta["text3"]
    text4      = js_dta["text4"]
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
               PostbackTemplateAction(
                            label=label1,
                            data=text1
                ),
                PostbackTemplateAction(
                            label=label2,
                            data=text2
                ),
                PostbackTemplateAction(
                            label=label3,
                            data=text3
                )
                #PostbackTemplateAction(
                #            label=label4,
                #            data=text4
                #)
            ]
        )
    )

     
    return message
def buttons_30t(msg):     # 3 text, 0URL
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
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
    label3     = js_dta["label3"]
    label4     = js_dta["label4"]
    text1       = js_dta["text1"]
    text2      = js_dta["text2"]
    text3      = js_dta["text3"]
    text4      = js_dta["text4"]
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
                MessageTemplateAction(
                    label= label1 ,  #"CBD的法律常識",
                    text=text1 ,    #"/C20"
                ),
                MessageTemplateAction(
                    label= label2 ,  #"CBD的法律常識",
                    text=text2 ,    #"/C20"
                ),
                MessageTemplateAction(
                    label=label3  ,   #"CBD的研究報告",
                    text=text3     #"/C30"

                )
            ]
        )
    )

    return message


def buttons_04(msg):    # 0 text, 4URL
  
    file = open('config.txt','r',encoding="utf-8")
    line = file.readline().strip('\n')    #line1 githubid
    line = file.readline().strip('\n')   #line1 githubproject
    line = file.readline().strip('\n')   #line1 githubproject
    #line=line.strip('\n')
    wsftpflr= line[12:].strip()

    wsmsg = msg.split('#')
    
    wjson_file = wsmsg[1] + ".json"
 
    url = wsftpflr + "json/" + wjson_file #http://www.abc.com/cust.json"
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
    label3     = js_dta["label3"]
    label4     = js_dta["label4"]
    url1       = js_dta["url1"]
    url2       = js_dta["url2"]
    url3       = js_dta["url3"]
    url4       = js_dta["url4"]
    text4      = js_dta["text4"]
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
                URITemplateAction(
                    label=label1   , #"認識CBD影片介紹",
                    uri=url1     #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
                ),
                URITemplateAction(
                    label=label2   , #"認識CBD影片介紹",
                    uri=url2,     #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
                )  ,              
                URITemplateAction(
                    label=label3   , #"認識CBD影片介紹",
                    uri=url3     #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
                )  ,              
                URITemplateAction(
                    label=label4   , #"認識CBD影片介紹",
                    uri=url4     #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
                ) 
            ]
        )
    )

    return message
#def buttons_13(msg):     #1 text 3url
#def buttons_22(msg):     #2 text 2url
def buttons_31t(msg):     # 3 text, 1URL   
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
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
    label3     = js_dta["label3"]
    label4     = js_dta["label4"]
    url1       = js_dta["url1"]
    text2      = js_dta["text2"]
    text3      = js_dta["text3"]
    text4      = js_dta["text4"]
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
                URITemplateAction(
                    label=label1   , #"認識CBD影片介紹",
                    uri=url1  ,   #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
                ),
                MessageTemplateAction(
                    label= label2 ,  #"CBD的法律常識",
                    text=text2 ,    #"/C20"
                ),
                MessageTemplateAction(
                    label=label3  ,   #"CBD的研究報告",
                    text=text3  ,   #"/C30"
                ),
                MessageTemplateAction(
                    label=label4 ,   #"更多選項",
                    text=text4
                )
            ]
        )
    )
    return message
def buttons_ud(msg):    # uri + post 
  
    file = open('config.txt','r',encoding="utf-8")
    line = file.readline().strip('\n')    #line1 githubid
    line = file.readline().strip('\n')   #line1 githubproject
    line = file.readline().strip('\n')   #line1 githubproject
    #line=line.strip('\n')
    wsftpflr= line[12:].strip()

    wsmsg = msg.split('#')
    
    wjson_file = wsmsg[1] + ".json"
 
    url = wsftpflr + "json/" + wjson_file #http://www.abc.com/cust.json"
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
 
    url1       = js_dta["url1"]
    text2      = js_dta["text2"]
     
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
                URITemplateAction(
                    label=label1   , #"認識CBD影片介紹",
                    uri=url1  ,   #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
                ),
                PostbackTemplateAction(
                            label=label2,
                            data=text2
 
                )
            ]
        )
    )

    return message
def buttons_u2d(msg):    # 2uri + post 
    print("u2d ==>" + msg)
    file = open('config.txt','r',encoding="utf-8")
    line = file.readline().strip('\n')    #line1 githubid
    line = file.readline().strip('\n')   #line1 githubproject
    line = file.readline().strip('\n')   #line1 githubproject
    #line=line.strip('\n')
    wsftpflr= line[12:].strip()

    wsmsg = msg.split('#')
    
    wjson_file = wsmsg[1] + ".json"
 
    url = wsftpflr + "json/" + wjson_file #http://www.abc.com/cust.json"
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
    label3     = js_dta["label3"]
 
    url1       = js_dta["url1"]
    url2       = js_dta["url2"]    
    text3      = js_dta["text3"]
     
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, 
            title= title,     
            text=text0,       
            actions=[
                URITemplateAction(
                    label=label1   , 
                    uri=url1  ,   
                ),
                URITemplateAction(
                    label=label2  , 
                    uri=url2  ,   
                ),
                PostbackTemplateAction(
                            label=label3,
                            data=text3
 
                )
            ]
        )
    )

 
    return message
def buttons_dd(msg):    # uri + post 
  
    file = open('config.txt','r',encoding="utf-8")
    line = file.readline().strip('\n')    #line1 githubid
    line = file.readline().strip('\n')   #line1 githubproject
    line = file.readline().strip('\n')   #line1 githubproject
    #line=line.strip('\n')
    wsftpflr= line[12:].strip()

    wsmsg = msg.split('#')
    
    wjson_file = wsmsg[1] + ".json"
 
    url = wsftpflr + "json/" + wjson_file #http://www.abc.com/cust.json"
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
 
    text1      = js_dta["text1"]
    text2      = js_dta["text2"]
     
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
                PostbackTemplateAction(
                            label=label1,
                            data=text1
                ),
                PostbackTemplateAction(
                            label=label2,
                            data=text2
 
                )
            ]
        )
    )

 
    return message 
def buttons_du(msg):    # post + url
    file = open('config.txt','r',encoding="utf-8")
    line = file.readline().strip('\n')    #line1 githubid
    line = file.readline().strip('\n')   #line1 githubproject
    line = file.readline().strip('\n')   #line1 githubproject
    #line=line.strip('\n')
    wsftpflr= line[12:].strip()

    wsmsg = msg.split('#')
    
    wjson_file = wsmsg[1] + ".json"
 
    url = wsftpflr + "json/" + wjson_file #http://www.abc.com/cust.json"
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
    url2       = js_dta["url2"]
    text1      = js_dta["text1"]
     
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
                PostbackTemplateAction(
                            label=label1,
                            data=text1
                ),
                URITemplateAction(
                    label=label2   , #"認識CBD影片介紹",
                    uri=url2  ,   #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
                )
            ]
        )
    )

 
    return message


def buttons_tu(msg):     #Text + url
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
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]

    url2        = js_dta["url2"]
    text1      = js_dta["text1"]

    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
                MessageTemplateAction(
                    label= label1 ,  #"CBD的法律常識",
                    text=text1 ,    #"/C20"        
                ),
                URITemplateAction(
                    label=label2   , #"認識CBD影片介紹",
                    uri=url2  ,   #"https://www.youtube.com/watch?v=0kOpOqHuiGo"

                )
            ]
        )
    )
    return message
def buttons_ut(msg):     # url + test
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
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]

    url1       = js_dta["url1"]
    text2      = js_dta["text2"]

    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
                URITemplateAction(
                    label=label1   , #"認識CBD影片介紹",
                    uri=url1  ,   #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
                ),
                MessageTemplateAction(
                    label= label2 ,  #"CBD的法律常識",
                    text=text2 ,    #"/C20"
                )
            ]
        )
    )
    return message
def buttons_31(msg):     # 3 text, 1URL   
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
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
    label3     = js_dta["label3"]
    label4     = js_dta["label4"]
    url1       = js_dta["url1"]
    text2      = js_dta["text2"]
    text3      = js_dta["text3"]
    text4      = js_dta["text4"]
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
                URITemplateAction(
                    label=label1   , #"認識CBD影片介紹",
                    uri=url1  ,   #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
                ),
                PostbackTemplateAction(
                            label=label2,
                            data=text2
                ),
                PostbackTemplateAction(
                            label=label3,
                            data=text3
                ),
                PostbackTemplateAction(
                            label=label4,
                            data=text4
                )
            ]
        )
    )

     
    return message
def buttons_40(msg):     # 3 text, 1URL   
  
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
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
    label3     = js_dta["label3"]
    label4     = js_dta["label4"]
    text1      = js_dta["text1"]
    text2      = js_dta["text2"]
    text3      = js_dta["text3"]
    text4      = js_dta["text4"]
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
               PostbackTemplateAction(
                            label=label1,
                            data=text1
                ),
                PostbackTemplateAction(
                            label=label2,
                            data=text2
                ),
                PostbackTemplateAction(
                            label=label3,
                            data=text3
                ),
                PostbackTemplateAction(
                            label=label4,
                            data=text4
                )
            ]
        )
    )

     
    return message
def buttons_40t(msg):     # 3 text, 1URL   
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
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
    label3     = js_dta["label3"]
    label4     = js_dta["label4"]
    url1       = js_dta["url1"]
    text1      = js_dta["text1"]
    text2      = js_dta["text2"]
    text3      = js_dta["text3"]
    text4      = js_dta["text4"]
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url,  
            title= title,       
            text=text0,       
            actions=[
                MessageTemplateAction(
                    label=label1   , 
                    text=text1  ,    
                ),
                MessageTemplateAction(
                    label= label2 ,  
                    text=text2 ,     
                ),
                MessageTemplateAction(
                    label=label3  ,  
                    text=text3  ,    
                ),
                MessageTemplateAction(
                    label=label4 ,   
                    text=text4
                )
            ]
        )
    )

    return message
def xbuttons_40(msg):    # 4 text, 0URL
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
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
    label3     = js_dta["label3"]
    label4     = js_dta["label4"]
    text1       = js_dta["text1"]
    text2      = js_dta["text2"]
    text3      = js_dta["text3"]
    text4      = js_dta["text4"]
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
               MessageTemplateAction(
                    label=label1   , #"認識CBD影片介紹",
                    uri=text1  ,   #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
                ),
                MessageTemplateAction(
                    label= label2 ,  #"CBD的法律常識",
                    text=text2 ,    #"/C20"
                ),
                MessageTemplateAction(
                    label=label3  ,   #"CBD的研究報告",
                    text=text3  ,   #"/C30"
                ),
                # PostbackTemplateAction(
                #    label ='1', # label4,
                #    data='2'
                 
                MessageTemplateAction(
                    label='123' ,   #"更多選項",
                   text='abc' 
                )
            ]
        )
    )

    return message

def text_10(msg):     # 2 text, 0URL
     
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
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
    text1       = js_dta["text1"]
    text2      = js_dta["text2"]
    message = TextSendMessage(text= text1)
    return message


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
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    image_url  = js_dta["image"]   
    alt_text   = js_dta["alt_text"]
    title      = js_dta["title"]
    text0      = js_dta["text0"]
    label1     = js_dta["label1"]
    label2     = js_dta["label2"]
    text1       = js_dta["text1"]
    text2      = js_dta["text2"]
    message = TemplateSendMessage(
        alt_text= alt_text ,   #'CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url= image_url, #"https://i.ibb.co/NWrhxmc/cbd.jpg",
            title= title,      #CBD的百寶庫",
            text=text0,       #"選擇您想要的內容",
            actions=[
                MessageTemplateAction(
                    label= label1 ,  #"CBD的法律常識",
                    text=text1 ,    #"/C20"
                ),
                MessageTemplateAction(
                    label= label2 ,  #"CBD的法律常識",
                    text=text2     #"/C20"
                
                )
            ]
        )
    )

    return message
