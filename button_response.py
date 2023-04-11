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
def buttons_41(msg):    # 4 text, 1URL
    print (" process 4 text 1url button")
    message = TemplateSendMessage(
        alt_text='CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.ibb.co/NWrhxmc/cbd.jpg",
            title="CBD的百寶庫",
            text="選擇您想要的內容",
            actions=[
                #DatetimePickerTemplateAction(
                #    label="請選擇生日",
                #    data="input_birthday",
                #    mode='date',
                #    initial='1990-01-01',
                #    max='2019-03-10',
                #    min='1930-01-01'
                #),
                URITemplateAction(
                    label="認識CBD影片介紹",
                    uri="https://www.youtube.com/watch?v=0kOpOqHuiGo"
                ),
                MessageTemplateAction(
                    label="CBD的法律常識",
                    text="/C20"
                ),
                MessageTemplateAction(
                    label="CBD的研究報告",
                    text="/C30"
                ),
                URITemplateAction(
                    label="CBD與寵物",
                    uri="/C40"
                ),
                URITemplateAction(
                    label="CBD的未來性",
                    uri="/c50"
                )
            ]
        )
    )
    return message