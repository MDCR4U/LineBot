#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

import json

import urllib.request

#url = "http://www.abc.com/cust.json"

##response = urllib.request.urlopen(url)
##data = response.read().decode("utf-8")
#json_data = json.loads(data)

#ImagemapSendMessage(組圖訊息)
 
#旋轉木馬按鈕訊息介面

def carousel_2(msg):

    print(' carousel_2 ' + msg)
    #LINE bot的Carousel Template可以有最多10個columns
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
    c1_image_url  = js_dta["c1_image"]   
    c1_alt_text   = js_dta["c1_alt_text"]
    c1_title      = js_dta["c1_title"]
    c1_text0      = js_dta["c1_text0"]
    c1_label1     = js_dta["c1_label1"]
    c1_label2     = js_dta["c1_label2"]
    c1_label3     = js_dta["c1_label3"]
    c1_text1      = js_dta["c1_text1"]
    c1_text2      = js_dta["c1_text2"]
    c1_text3      = js_dta["c1_text3"]
    c2_image_url  = js_dta["c2_image"]   
    c2_title      = js_dta["c2_title"]
    c2_text0      = js_dta["c2_text0"]
    c2_label1     = js_dta["c2_label1"]
    c2_label2     = js_dta["c2_label2"]
    c2_label3     = js_dta["c2_label3"]
    c2_text1      = js_dta["c2_text1"]
    c2_text2      = js_dta["c2_text2"]
    c2_text3      = js_dta["c2_text3"]
    message = TemplateSendMessage(
        alt_text=c1_alt_text,
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=c1_image_url,
                    title=c1_title,
                    text=c1_text0,
                    actions=[
                        PostbackTemplateAction(
                            label= c1_label1,
                            data=c1_text1
                        ),
                        PostbackTemplateAction(
                            label= c1_label2,
                            data=c1_text2
                        ),
                        PostbackTemplateAction(
                            label= c1_label3,
                            data=c1_text3
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=c2_image_url,
                    title=c2_title,
                    text=c2_text0,
                    actions=[
                        PostbackTemplateAction(
                            label= c2_label1,
                            data=c2_text1
                        ),
                        PostbackTemplateAction(
                            label= c2_label2,
                            data=c2_text2
                        ),
                        PostbackTemplateAction(
                            label= 'aaaa', #c2_label3,
                            data='bbbb' #c2_text3
                        )
                    ]
                )
            ]
        )
    )
    return message
def Carousel_5(msg):
    #LINE bot的Carousel Template可以有最多10個columns
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
    c1_image_url  = js_dta["c1_image"]   
    c1_alt_text   = js_dta["c1_alt_text"]
    c1_title      = js_dta["c1_title"]
    c1_text0      = js_dta["c1_text0"]
    c1_label1     = js_dta["c1_label1"]
    c1_label2     = js_dta["c1_label2"]
    c1_label3     = js_dta["c1_label3"]
    c1_text1      = js_dta["c1_text1"]
    c1_text2      = js_dta["c1_text2"]
    c1_text3      = js_dta["c1_text3"]
    c2_image_url  = js_dta["c2_image"]   
    c2_title      = js_dta["c2_title"]
    c2_text0      = js_dta["c2_text0"]
    c2_label1     = js_dta["c2_label1"]
    c2_label2     = js_dta["c2_label2"]
    c2_label3     = js_dta["c2_label3"]
    c2_text1      = js_dta["c2_text1"]
    c2_text2      = js_dta["c2_text2"]
    c2_text3      = js_dta["c2_text3"]
    c3_image_url  = js_dta["c3_image"]   
    c3_title      = js_dta["c3_title"]
    c3_text0      = js_dta["c3_text0"]
    c3_label1     = js_dta["c3_label1"]
    c3_label2     = js_dta["c3_label2"]
    c3_label3     = js_dta["c3_label3"]
    c3_text1      = js_dta["c3_text1"]
    c3_text2      = js_dta["c3_text2"]
    c3_text3      = js_dta["c3_text3"]
    c4_image_url  = js_dta["c4_image"]   
    c4_title      = js_dta["c4_title"]
    c4_text0      = js_dta["c4_text0"]
    c4_label1     = js_dta["c4_label1"]
    c4_label2     = js_dta["c4_label2"]
    c4_label3     = js_dta["c4_label3"]
    c4_text1      = js_dta["c4_text1"]
    c4_text2      = js_dta["c4_text2"]
    c4_text3      = js_dta["c4_text3"]
    c5_image_url  = js_dta["c5_image"]   
    c5_title      = js_dta["c5_title"]
    c5_text0      = js_dta["c5_text0"]
    c5_label1     = js_dta["c5_label1"]
    c5_label2     = js_dta["c5_label2"]
    c5_label3     = js_dta["c5_label3"]
    c5_text1      = js_dta["c5_text1"]
    c5_text2      = js_dta["c5_text2"]
    c5_text3      = js_dta["c5_text3"]
    message = TemplateSendMessage(
        alt_text=c1_alt_text,
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=c1_image_url,
                    title=c1_title,
                    text=c1_text0,
                    actions=[
                        PostbackTemplateAction(
                            label= c1_label1,
                            data=c1_text1
                        ),
                        PostbackTemplateAction(
                            label= c1_label2,
                            data=c1_text2
                        ),
                        PostbackTemplateAction(
                            label= c1_label3,
                            data=c1_text3
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=c2_image_url,
                    title=c2_title,
                    text=c2_text0,
                    actions=[
                        PostbackTemplateAction(
                            label= c2_label1,
                            data=c2_text1
                        ),
                        PostbackTemplateAction(
                            label= c2_label2,
                            data=c2_text2
                        ),
                        PostbackTemplateAction(
                            label= c2_label3,
                            data=c2_text3
                        )
                    ]
                ),

                CarouselColumn(
                    thumbnail_image_url=c3_image_url,
                    title=c3_title,
                    text=c3_text0,
                    actions=[
                        PostbackTemplateAction(
                            label= c3_label1,
                            data=c3_text1
                        ),
                        PostbackTemplateAction(
                            label= c3_label2,
                            data=c3_text2
                        ),
                        PostbackTemplateAction(
                            label= c3_label3,
                            data=c3_text3
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=c4_image_url,
                    title=c4_title,
                    text=c4_text0,
                    actions=[
                        PostbackTemplateAction(
                            label= c4_label1,
                            data=c4_text1
                        ),
                        PostbackTemplateAction(
                            label= c4_label2,
                            data=c4_text2
                        ),
                        PostbackTemplateAction(
                            label= c4_label3,
                            data=c4_text3
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=c5_image_url,
                    title=c5_title,
                    text=c5_text0,
                    actions=[
                        PostbackTemplateAction(
                            label= c5_label1,
                            data=c5_text1
                        ),
                        PostbackTemplateAction(
                            label= c5_label2,
                            data=c5_text2
                        ),
                        PostbackTemplateAction(
                            label= c5_label3,
                            data=c5_text3
                        )
                    ]
                )
            ]
        )
    )
    return message
#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
def image_carousel_message1_z():
    message = TemplateSendMessage(
        alt_text='我們的產品',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.ibb.co/kh0bzyX/Daily-Spray.jpg",
                    action=URITemplateAction(
                        label="營養噴劑",
                        uri="https://mydailychoice.com/shop?selected_brands=2&ref=lifefree"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.ibb.co/54BG4j1/mantra.jpg",
                    action=URITemplateAction(
                        label="精油系列",
                        uri="https://mydailychoice.com/shop?selected_brands=3&ref=lifefree"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.ibb.co/1MKhZpW/Cosmikology.jpg",
                    action=URITemplateAction(
                        label="美妝系列",
                        uri="https://mydailychoice.com/shop?selected_brands=5&ref=lifefree"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.ibb.co/Sx0Tw7M/hlt.jpg",
                    action=URITemplateAction(
                        label="高品質旅遊",
                        uri="https://mydailychoice.com/shop?selected_brands=4&ref=lifefree"
                    )
                )
            ]
        )
    )
    return message

#關於LINEBOT聊天內容範例