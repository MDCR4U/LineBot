#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def image_carousel_message1():
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