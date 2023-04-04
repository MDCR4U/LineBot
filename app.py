#使用 LINE BOT SDK
#搭配Flask使用 LINE BOT SDK
#https://qiu-yan-ming.gitbook.io/python-chatbot/shi-yong-line-bot-sdk
#LINE BOT SDK Github
#pip3 install line-bot-sdk

#deploy hook https://api.render.com/deploy/srv-cgftbvm4daddcg1ea0k0?key=0o-gtqaF06g


#deploy setting :
# build command : $ pip install -r requirement , when fail by pip upgrade 
# change to :  pip install --upgrade pip  for upgrade

# error : Bash: gunicorn: command not found requirement 20.1.0 ==> 19.7.1
#  ==> ref to : https://community.render.com/t/bash-gunicorn-command-not-found/1485/7
#https://www.youtube.com/watch?v=OBGaCULCZzg


#https://engineering.linecorp.com/zh-hant/blog/line-bot-guideline-3/

 #================= for send mail =================
import datetime
import smtplib
import time
 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sendmails import *
#==================  for email ===================

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
from gptapi import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('gd2k8snxpn3PP+nC+spxDIgQF6ZTtjfS/vHmqOIEJ8W/B1bryahPh61EfFIepnHqfjTQ4zhc29120TvtHVjk4dMB5vkrJFtvcjO07389gomlkggI/rMJCoid9PCCr6O3v0dTY2R3n4FFA6IMr1D5twdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('82ab0090dc70c5f7d3a6c62fb1e09eb8')
#@app.route("/")

line_user_id = ''

# 監聽所有來自 /callback 的 Post Request
@app.route("/r4u005", methods=['POST'])
def callback():
    # get X-Line-Signature header value
   
#   print("aaaaaaaaaaa  call back aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        print("entry handler \n\################################")
        handler.handle(body, signature)
    #    print("handler finish")
    except InvalidSignatureError:
        print("error handler \n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        abort(9400)

    #print("call back return")
    #return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("handle start here ")
    usr =event.source.user_id
    line_user_id = usr
    print("user id = " + usr )
    msg = event.message.text
    print("\n\n\n\n\n\n\n\n\n")
    #message = TextSendMessage(text= "您是說 : " + msg  + "嗎?(pushed)\n" + usr)
    #line_bot_api.push_message(usr, message)
    #print("event type :" + event.type)
    #print ("event source\n==================================================================")
    #print(event.source)
    #print (msg)
    #print ("event source\n==================================================================")

    # first 4 char 
    # last 5 char string[-5:])
    # string.upper
    # string.lower
    #if msg[0:4] == '/gpt':   
    #   print ('\n** link function to get gpt response' + '**') 
    #   gpt_response = gptapi()
    #   message = TextSendMessage(text='GPT response : ' + gpt_response  )
    #   line_bot_api.reply_message(event.reply_token, message) 
    #elif 'gpt' in msg:
    #   #gpt_response = gptapi()
    #   #message = TextSendMessage(text="GPT 回應 : " + gpt_response )
    #   message = TextSendMessage(text="GPT Auto : " + msg )
    #   line_bot_api.reply_message(event.reply_token, message) 

    print ('msg = ' + msg)
    #if '/smail' in msg :
    #     message = TextSendMessage(text= "您是說 : " +msg + "嗎?")
    #    line_bot_api.reply_message(event.reply_token,  message )
    if '/smail' in msg:
    
        from datetime import datetime

        now = datetime.now() # current date and time
        print("call send_mails : " )
        print(now.strftime("%m/%d/%Y, %H:%M:%S") + " start send message")
        sendlog = send_mail(usr,msg)
        print ("send mail return")
        print (sendlog)
    #    sendlog = "manual test message"
        print ("send reply message ")
    #    print(sendlog)
        
        message = TextSendMessage(text= "完成信件發送 : ")
        line_bot_api.reply_message(event.reply_token, message)  
        print ('return OK')   
        return      ('OK')
        #line_bot_api.push_message(usr, message)
        #print("reply tokem" +event.reply_token)
        #line_bot_api.reply_message(event.reply_token, message)
        #line_bot_api.push_message(usr, message)

    print ("not mail ")
    if '/init' in msg:
        initcounter()   
        message = TextSendMessage(text= "完成信件發送 : initial counter complete =====")
        line_bot_api.reply_message(event.reply_token, message)            
    if '/loadsmtp' in msg:
        loadsts = loadfile('smtp.csv')   
        message = TextSendMessage(text= "完成信件發送 : " + loadsts+ "\n==========================")
        line_bot_api.reply_message(event.reply_token, message)        
    if '/loadmail' in msg:
        loadsts = loadfile('mail.csv')   
        message = TextSendMessage(text= "完成信件發送 : " + loadsts+ "\n==========================")
        line_bot_api.reply_message(event.reply_token, message)    
             
    #elif '最新合作廠商' in msg:
    #    message = imagemap_message()
    #    line_bot_api.reply_message(event.reply_token, message)
    #elif '最新活動訊息' in msg:
    #    message = buttons_message()
    #    line_bot_api.reply_message(event.reply_token, message)
    #elif '註冊會員' in msg:
    #    message = Confirm_Template()
    #    line_bot_api.reply_message(event.reply_token, message)
    #elif '旋轉木馬' in msg:
    #    message = Carousel_Template()
    #    line_bot_api.reply_message(event.reply_token, message)
    #elif '圖片畫廊' in msg:
    #    message = test()
    #    line_bot_api.reply_message(event.reply_token, message)
    #elif '功能列表' in msg:
    #    message = function_list()
    #    line_bot_api.reply_message(event.reply_token, message)
    #else:


    print ("reply aaaaaa")
    wsmsg = test_func(msg)
    print("return from text_func : " + wsmsg)
    message = TextSendMessage(text= "您是說 : " + wsmsg + "嗎?")
    line_bot_api.reply_message(event.reply_token,  message )
    return 'OK'
     
    

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入'  + 'MDC make Rich for You')
    line_bot_api.reply_message(event.reply_token, message)
        
#def loadfile():
   #可以使用 Python 的 urllib 模組中的 urlretrieve() 函式來下載檔案。以下是一個示範程式碼：
   #ythonCopy code


#   url = 'https://www.example.com/example_file.txt'
#   file_name = 'example_file.txt'

#   urllib.request.urlretrieve(url, file_name)
   #url 是要下載的檔案的 URL，
   # file_name 則是下載後要儲存的檔案名稱和路徑
   # （如果只指定檔案名稱，則預設儲存到目前的資料夾中）。 urlretrieve() 函式會從指定的 URL 下載檔案，並將其儲存在 file_name 指定的位置。   

 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
