#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

import json
import os

import urllib.request

#url = "http://www.abc.com/cust.json"

##response = urllib.request.urlopen(url)
##data = response.read().decode("utf-8")
#json_data = json.loads(data)

#ImagemapSendMessage(組圖訊息)
def imagemap_5 (msg):
    wsftpflr = os.environ.get('linebot_ftpurl')

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
 
    print("jsaon read complete")
    background_url  = js_dta["image"]                           #"https://i.ibb.co/mJfp6Nf/background.png"  #https://ibb.co/0BZHztf"
    url_top_left    = js_dta["url_top_left"]                             #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
    url_top_right   = js_dta["url_top_right"]                            #"https://www.youtube.com/watch?v=XFvgYYHvcfE"
    url_left_down   = js_dta["url_left_down"]                            #"https://www.youtube.com/watch?v=iOu5DwEQaJE"
    url_right_down1 = js_dta["url_right_down1"]                          #"https://www.youtube.com/watch?v=R9cx3kgwWD0"
    url_right_down2 = js_dta["url_right_down2"]                          #"https://www.youtube.com/watch?v=DAlIup87Aso&t=26s"
    alt_text        = js_dta ["alt_text"]                                     #"CBD"
    base_width = js_dta["base_width"]     #2000
    base_height = js_dta["base_height"]   #2000
    p1_x = js_dta["p1_x"]                 #0
    p1_y = js_dta["p1_y"]                 #0
    p1_width = js_dta["p1_width"]         #1000
    p1_height = js_dta["p1_height"]        #1000
    
    p2_x = js_dta["p2_x"]                 #1000
    p2_y = js_dta["p2_y"]                 #0
    p2_width = js_dta["p2_width"]         #1000
    p2_height = js_dta["p2_height"]       #1000
    
    p3_x = js_dta["p3_x"]                 #0
    p3_y = js_dta["p3_y"]                  #1000
    p3_width = js_dta["p3_width"]         #1000
    p3_height = js_dta["p3_height"]       #1000
 
    p4_x = js_dta["p4_x"]                 #1000
    p4_y = js_dta["p4_y"]                 #1000
    p4_width = js_dta["p4_width"]         #1000
    p4_height = js_dta["p4_height"]       #500
    
    p5_x = js_dta["p5_x"]                 #1000
    p5_y = js_dta["p5_y"]                 #1500
    p5_width = js_dta["p5_width"]         #1000
    p5_height = js_dta["p5_width"]        #500

    message = ImagemapSendMessage(
        base_url=background_url , 
       
        #base_url="https://i.ibb.co/TKZqd7P/background-CBD.jpg",
        alt_text=alt_text,
        base_size=BaseSize(height=base_height, width=base_width),
        actions=[                                       # 依據顯示 的圖片  做切割處理動作 
            URIImagemapAction(
                #後疫情
                link_uri=url_top_left ,
                area=ImagemapArea(
                    x=p1_x, y=p1_y, width=p1_width, height=p1_height                               #左上
                )
            ),
            URIImagemapAction(                                                     #右上
                #協槓人生
                link_uri=url_top_right,
                area=ImagemapArea(
                    x=p2_x, y=p2_y, width=p2_width, height=p2_height
                )
            ),
            URIImagemapAction(                                                     #左下
                #創業團隊
                link_uri=url_left_down,
                area=ImagemapArea(
                    x=p3_x, y=p3_y, width=p3_width, height=p3_height
                )
            ),
                    
            URIImagemapAction(
               #改變自己
                link_uri=url_right_down1,
                area=ImagemapArea(
                    x=p4_x, y=p4_y, width=p4_width, height=p4_height
                )
            ),
            URIImagemapAction(
                #財富密碼
                link_uri=url_right_down2,
                area=ImagemapArea(
                    x=p5_x, y=p5_y, width=p5_width, height=p5_height
                )
            )
        ]
    )
    return message

