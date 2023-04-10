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
def buttons_message():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="是否要獲得旅遊補助金活動？",
            text="輸入生日可獲得生日驚喜禮得機會",
            actions=[
                #DatetimePickerTemplateAction(
                #    label="請選擇生日",
                #    data="input_birthday",
                #    mode='date',
                #    initial='1990-01-01',
                #    max='2019-03-10',
                #    min='1930-01-01'
                #),
                MessageTemplateAction(
                    label="索取百元美金旅遊補助金",
                    text="開啟網站\nhttps://mydailychoice.com/shop?selected_brands=7&ref=lifefree\n百元美金旅遊補助等著您"
                ),
                MessageTemplateAction(
                    label="索取百元美金旅遊補助金",
                    text="開啟網站\nhttps://mydailychoice.com/shop?selected_brands=7&ref=lifefree\n百元美金旅遊補助等著您"
                ),
                URITemplateAction(
                    label="免費註冊享回饋",
                    uri="https://mydailychoice.com/lifefree"
                ),
                URITemplateAction(
                    label="免費註冊享回饋",
                    uri="https://mydailychoice.com/lifefree"
                )
            ]
        )
    )
    return message