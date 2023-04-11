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
import sys
import urllib.request
 
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
from image_response import *
from button_response import *
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
#Global Variable
line_access_token = ''
line_channel_secret = ''
ftpurl = ''
gpt_token = ''
line_bot_api = LineBotApi('gd2k8snxpn3PP+nC+spxDIgQF6ZTtjfS/vHmqOIEJ8W/B1bryahPh61EfFIepnHqfjTQ4zhc29120TvtHVjk4dMB5vkrJFtvcjO07389gomlkggI/rMJCoid9PCCr6O3v0dTY2R3n4FFA6IMr1D5twdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('82ab0090dc70c5f7d3a6c62fb1e09eb8')
line_user_id = ''
github_id ="MDCR4U"
github_prj="LineBot"
userFolder= ''
sendmail_auth = 'N'

#讀取 config.sys 取得 information  
file = open('config.txt','r',encoding="utf-8")
line = file.readline().strip('\n')    #line1 githubid
github_id = line[12:].strip()         # 去除  頭尾 space

line = file.readline().strip('\n')   #line1 githubproject
#line=line.strip('\n')
github_prj = line[12:].strip()
line = file.readline().strip('\n')   #line1 githubproject
line=line.strip('\n')
ftpurl= line[12:].strip()
print(ftpurl + "*")
file.close()

 

 
# download key file
url = ftpurl #+ "ket.txt" #'https://mdcgenius.000webhostapp.com/key.txt'   #githuburl + "key.txt"
url = ftpurl + "key.txt"
filename = 'key.txt'
#url = 'https://mdcgenius.000webhostapp.com/key.txt' 
#print(url + "-" + filename)
print("#####################" + url + "######################")
try:
    urllib.request.urlretrieve(url, filename)
except:
    print("url get error " + url)    
    exit()
#取得 系統 KEY 

#print("========================= " + url )
file = open('key.txt','r',encoding="utf-8")
line = file.readline().strip('\n')                 #line_access_token = ''
line_access_token =line[17:].strip()


line = file.readline().strip('\n')                #line_channel_secret = ''
line_channel_secret = line[17:].strip()

line = file.readline().strip('\n')                #gpt_token
gpt_token = line[17:].strip()


# Channel Access Token 
line_bot_api = LineBotApi(line_access_token)
# Channel Secret
handler = WebhookHandler(line_channel_secret)

# 監聽所有來自 /callback 的 Post Request
@app.route("/rich4u_004", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    print("start CALL BACK PROCESS")
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    #print("body = " + body)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        print("Handle event " + body)
        handler.handle(body, signature)
#        print("control return to   callback")
    except InvalidSignatureError:
        abort(400)
    
#    print("call back return")
    return 'OK'  #ok(200)


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("??????????????????????????????????????????????????????")
    usr =event.source.user_id
    line_user_id = usr
    print("\n====handle_message=========\n"+ line_user_id)
    userFolder = check_line_id(ftpurl ,line_user_id)
    print("USER Folder " + userFolder + "*")
    msg = event.message.text
    print("\n====handle_message=========\n"+ msg)
    # first 4 char 
    # last 5 char string[-5:])
    # string.upper
    # string.lower
  

    print("\n   handle START===>           "+ msg +"\n")
    if msg.startswith('#'):
#        url=githubutl +  "key.txt"
#        url = "http://mdcgenius.tw/key.txt"
#        file = urllib.request.urlopen(url)
#        wkey =  file.readline()
#        openai.api_key = wkey.decode('utf-8') 
        openai.api_key = gpt_token.decode('utf-8') 
        print(openai.api_key + msg)
        #file.close()
        gpt_response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=msg[1:],
            temperature=0.5,
            n=1,
            max_tokens=200
        ).choices[0].text

        gpt_response =gpt_response[0:20]
        print("Line BOT reply ======>" + gpt_response)
        try :
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="line bot reply gpt \n" + gpt_response)
            )
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print("Exception Type:===>", exc_type)
            print("Exception Value:", exc_value)
            print("Traceback Object:", exc_traceback)
    elif '/SMAIL' in msg.upper():     #isupper(), islower(), lower(), upper()
        if userFolder == '' :
            message = TextSendMessage(text= "找不到 發送信件的授權資料，請記住您的代碼 " + usr +"\n與 系統管理員聯絡申請授權 " )
            line_bot_api.reply_message(event.reply_token, message)              
        from datetime import datetime
        now = datetime.now() # current date and time
        #增加 user folder
        sendlog = send_mail(usr,msg,userFolder)
        message = TextSendMessage(text= "完成信件發送 : " + sendlog)
        #print("Line BOT reply ======  aaaaaaaaaaaaaaaaaaaa")
        line_bot_api.reply_message(event.reply_token, message)  
           
        #line_bot_api.push_message(usr, message)
        #print("reply tokem" +event.reply_token)
        #line_bot_api.reply_message(event.reply_token, message)
        #line_bot_api.push_message(usr, message)
        #print("Line BOT reply ===complete ===  bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb    " + msg)
    #elif '/main' in msg:
    #    wsmenu = '目錄:\n 指令   命令內容\n==============\n/S001:圖片展示\n/S002:旅遊現金抵用券\n/S003:註冊會員\n/S004:旋轉木馬\n/S005:我們的產品\n/S006:功能列表'
    #    wsmenu = wsmenu + '\n/TSTMAIL:service@mdcr4u.com.tw \n 發送測試信件說明\n /TSTMAIL=> 指令 +":" + "收件者信箱")'
    #    wsmenu = wsmenu + '\n/SMAIL:8  \n  批量發送信件說明\n SMAIL=> 指令 + ":" + 發送數量'
    #    message = TextSendMessage(text= wsmenu)
    #    line_bot_api.reply_message(event.reply_token, message) 
    elif '/init' in msg:
        initcounter(usr,msg,userFolder) 
        message = TextSendMessage(text= "完成信件處理 : initial counter complete =====")
        line_bot_api.reply_message(event.reply_token, message)   
    elif '/load' in msg:
          loadsts  = loadfile(usr,msg,userFolder) 
          message = TextSendMessage(text= "檔案設置處理 : " + loadsts)
          line_bot_api.reply_message(event.reply_token, message)            
   
    #elif '最新合作廠商' in msg:
    elif msg.upper()[0:5] == '/MAIN'  : #'/image#cbd' in msg:   
        print(" will proces simage message")
        message = imagemap_5(msg)
        line_bot_api.reply_message(event.reply_token, message)
    #elif '最新活動訊息' in msg:
    elif msg.upper()[0:2] == '&&' :
        print("msg   for token" + msg)
        message = token(msg)
        line_bot_api.reply_message(event.reply_token, message)
    elif msg.upper()[0:4] == '/CBD' :
        message = buttons_31("&&#C000#button31#")
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
        print("echo message " + user_id)
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

def token(msg):
    wmsg = msg[2:]
    wkmsg = wmsg.split('#')
    
    if  wkmsg[2]  == "button_30" :
        wsmessage = buttons_30(wkmsg[1])
    elif wkmsg[2] == "button_31" :
        wsmessage = buttons_31(wkmsg[1])    
    elif wkmsg[2] == "button_01" :
        wsmessage = buttons_01(wkmsg[1])    
    elif wkmsg[2] == "button_10" :
        wsmessage = buttons_10(wkmsg[1])    
    elif wkmsg[2] == "button_02" :
        wsmessage = buttons_02(wkmsg[1])                  
    elif wkmsg[2] == "button_11" :
        wsmessage = buttons_11(wkmsg[1])          
    elif wkmsg[2] == "button_20" :
        wsmessage = buttons_20(wkmsg[1])          
    elif wkmsg[2] == "button_03" :
        wsmessage = buttons_03(wkmsg[1])  
    elif wkmsg[2] == "button_04" :
        wsmessage = buttons_04(wkmsg[1])  
    elif wkmsg[2] == "button_40" :
        wsmessage = buttons_40(wkmsg[1])                          
    return wsmessage    
            
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
