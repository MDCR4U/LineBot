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
@app.route("/r4u_002", methods=['POST'])
def callback():
    # get X-Line-Signature header value
   
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        print("Handle event")
        handler.handle(body, signature)
        print("control return to   callback")
    except InvalidSignatureError:
        abort(400)
    
    print("call back return")
    return 'OK'  #ok(200)


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    usr =event.source.user_id
    line_user_id = usr
    msg = event.message.text
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

    print("\n   handle START===>           "+ msg +"\n")
    if msg.startswith('#'):
        openai.api_key = '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' #os.environ['OPENAI_API_KEY']
        url = "http://mdcgenius.tw/key.txt"
        file = urllib.request.urlopen(url)
        wkey =  file.readline()
        openai.api_key = wkey.decode('utf-8') 
        print(openai.api_key + msg)
        file.close()
        gpt_response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=msg[1:],
            temperature=0.5,
            n=1,
            max_tokens=200
        ).choices[0].text

        gpt_response ="abcdefgh"
        print("Line BOT reply ======>" + gpt_response)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="line bot reply gpt \n" + gpt_response)
        )
        #print("Line BOT reply ==xxxxxx====" + gpt_response)

        #line_bot_api.push_message(
        #    usr,
        #    TextSendMessage(text=msg +"\n" + gpt_response)            
        #)
        return 
     
 
    if '/SMAIL' in msg:
        from datetime import datetime
        now = datetime.now() # current date and time
        sendlog = send_mail(usr,msg)
        message = TextSendMessage(text= "完成信件發送 : " + sendlog)
        print("Line BOT reply ======  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        line_bot_api.reply_message(event.reply_token, message)  
           
        #line_bot_api.push_message(usr, message)
        #print("reply tokem" +event.reply_token)
        #line_bot_api.reply_message(event.reply_token, message)
        #line_bot_api.push_message(usr, message)
        print("Line BOT reply ===complete ===  bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb    " + msg)
    elif '/main' in msg:
        wsmenu = '目錄:\n 指令   命令內容\n==============\n/S001:圖片展示\n/S002:旅遊現金抵用券\n/S003:註冊會員\n/S004:旋轉木馬\n/S005:我們的產品\n/S006:功能列表'
        wsmenu = wsmenu + '\n/TSTMAIL:service@mdcr4u.com.tw \n 發送測試信件說明\n /TSTMAIL=> 指令 +":" + "收件者信箱")'
        wsmenu = wsmenu + '\n/SMAIL:8  \n  批量發送信件說明\n SMAIL=> 指令 + ":" + 發送數量'
        message = TextSendMessage(text= wsmenu)
        line_bot_api.reply_message(event.reply_token, message) 
    elif '/init' in msg:
        initcounter()   
        message = TextSendMessage(text= "完成信件處理 : initial counter complete =====")
        line_bot_api.reply_message(event.reply_token, message)            
    elif '/loadsmtp' in msg:
        loadsts = loadfile('smtp.csv')   
        message = TextSendMessage(text= "完成信件處理 : " + loadsts+ "\n==========================")
        line_bot_api.reply_message(event.reply_token, message)        
    elif '/loadmail' in msg:
        loadsts = loadfile('mail.csv')   
        message = TextSendMessage(text= "完成信件處理 : " + loadsts+ "\n==========================")
        line_bot_api.reply_message(event.reply_token, message)    
        '/S001:最新合作廠商\n/S002:最新活動訊息\n/S003:註冊會員\n/S004:旋轉木馬\n/S005:我們的產品\n/S006:'
    #elif '最新合作廠商' in msg:
    elif '/S001' in msg:        
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    #elif '最新活動訊息' in msg:
    elif '/S002' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    #elif '註冊會員' in msg:
    elif '/S003' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    #elif '旋轉木馬' in msg:
    elif 'S004' in msg:        
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    #elif '圖片畫廊' in msg:
    elif '/S005' in msg:
        message = image_carousel_message1() # test()
        line_bot_api.reply_message(event.reply_token, message)
    #elif '功能列表' in msg:
    #elif 'S006' in msg:        
    #    message = function_list()
    #    line_bot_api.reply_message(event.reply_token, message)
    else :
        user_id = event.source.user_id
        user_type = event.source.type
    
        if user_type == "user":
            if user_id.startswith("U"):
            # 手機版的 LINE
                reply_text = "您是使用手機版的 LINE"
            else:
                # 電腦版的 LINE
                reply_text = "您是使用電腦版的 LINE"
        else:
            # 群組或聊天室
            reply_text = "您是在群組或聊天室中"

        #line_bot_api.reply_message(
        #    event.reply_token,
        #    TextSendMessage(text=reply_text)
        
        print(reply_text)
        message = TextSendMessage(text= reply_text + "\您是說 : " + msg + "嗎?")
        line_bot_api.reply_message(event.reply_token,  message )
    print(' call back return OK')
    
     
    

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name

    message = TextSendMessage(text=f'{name}歡迎加入 MDC 富裕與您同在請輸入 /MAIN 顯示功能表')
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
