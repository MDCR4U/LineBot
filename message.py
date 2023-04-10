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
def imagemap_5_message(msg):
    file = open('config.txt','r',encoding="utf-8")
    line = file.readline().strip('\n')    #line1 githubid
    line = file.readline().strip('\n')   #line1 githubproject
    line = file.readline().strip('\n')   #line1 githubproject
    #line=line.strip('\n')
    wsftpflr= line[12:].strip()

    print ("process image * 5" + wsftpflr)
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
 
    print("jsaon read complete")
    background_url  = js_dta["image"]                           #"https://i.ibb.co/mJfp6Nf/background.png"  #https://ibb.co/0BZHztf"
    print ("image" + background_url)
    url_top_left    = js_dta["url_top_left"]                             #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
    url_top_right   = js_dta["url_top_right"]                            #"https://www.youtube.com/watch?v=XFvgYYHvcfE"
    url_left_down   = js_dta["url_left_down"]                            #"https://www.youtube.com/watch?v=iOu5DwEQaJE"
    url_right_down1 = js_dta["url_right_down1"]                          #"https://www.youtube.com/watch?v=R9cx3kgwWD0"
    url_right_down2 = js_dta["url_right_down2"]                          #"https://www.youtube.com/watch?v=DAlIup87Aso&t=26s"
    alt_text        = js_dta ["alt_text"]                                     #"CBD"
    base_width = js_dta["base_width"]     #2000
    base_height = js_dta["base_height"]   #2000
    print("aaaaa")
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

    print(background_url)
    message = ImagemapSendMessage(
        #base_url="https://i.imgur.com/BfTFVDN.jpg",    #顯示的圖片 2000 * 2000
        #base_url = "https://mdcgenius.000webhostapp.com/resource/background_CBD.jpg",
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

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="是否要獲得旅遊補助金活動？",
            text="輸入生日可獲得生日驚喜禮得機會",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),
                MessageTemplateAction(
                    label="索取百元美金旅遊補助金",
                    text="開啟網站\nhttps://mydailychoice.com/shop?selected_brands=7&ref=lifefree\n百元美金旅遊補助等著您"
                ),
                URITemplateAction(
                    label="免費註冊享回饋",
                    uri="https://mydailychoice.com/lifefree"
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template():

    message = TemplateSendMessage(
        alt_text='是否註冊成為會員？',
        template=ConfirmTemplate(
            text="是否註冊成為會員？",
            actions=[
                PostbackTemplateAction(
                    label="馬上註冊",
                    text="現在、立刻、馬上",
                    data="會員註冊"
                ),
                MessageTemplateAction(
                    label="查詢其他功能",
                    text="查詢其他功能"
                )
            ]
        )
    )
    return message

#旋轉木馬按鈕訊息介面

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png',
                    title='這是第一塊模板',
                    text='一個模板可以有三個按鈕',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是1'
                        ),
                        URITemplateAction(
                            label='進入1的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
                    title='這是第二塊模板',
                    text='副標題可以自己改',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是2'
                        ),
                        URITemplateAction(
                            label='進入2的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png',
                    title='這是第三個模塊',
                    text='最多可以放十個',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=3'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是3'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png'
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