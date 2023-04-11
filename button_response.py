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
def buttons_31(msg):    # 3 text, 1URL
    print (" process 3 text 1url button")
    message = TemplateSendMessage(
        alt_text='CBD的法律常識～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.ibb.co/NWrhxmc/cbd.jpg",
            title="CBD的百寶庫",
            text="選擇您想要的內容",
            actions=[
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
                MessageTemplateAction(
                    label="更多選項",
                    uri="/C000"
                )
            ]
        )
    )

    print("button 4-1 complete")
    return message