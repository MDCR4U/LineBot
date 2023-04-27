#need to add
#   post back : get line id by event 
#   call token(msg,lineid)
#   in token writ continue token

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

#@ show text url 
#https://mdcgenius.000webhostapp.com/show.html?show=text1.txt

 #================= for send mail =================
import datetime
import smtplib
import time
import sys
import urllib.request
 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sendmails import *
from senddemomail import *

#==================  for email ===================

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from linebot.models import   TextSendMessage

#======這裡是呼叫的檔案內容=====
from message import *
from image_response import *
from button_response import *
from text_response import *
from carousel_response import *
from new import *
from Function import *
from gptapi import *
from get_token import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========
import json 
import urllib.request

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
#Global Variable
line_access_token = ''
line_channel_secret = ''
ftpurl = ''
gpt_token = ''
#line_bot_api = LineBotApi('gd2k8snxpn3PP+nC+spxDIgQF6ZTtjfS/vHmqOIEJ8W/B1bryahPh61EfFIepnHqfjTQ4zhc29120TvtHVjk4dMB5vkrJFtvcjO07389gomlkggI/rMJCoid9PCCr6O3v0dTY2R3n4FFA6IMr1D5twdB04t89/1O/w1cDnyilFU=')
#handler = WebhookHandler('82ab0090dc70c5f7d3a6c62fb1e09eb8')
line_user_id = ''
github_id ="MDCR4U"
github_prj="LineBot"
userFolder= ''
sendmail_auth = 'N'

ispostback = 'N'

#with open("config.json", "r", encoding="utf-8") as f:
#    loaded_data = json.load(f)
#
#ftpurl = loaded_data["ftpurl"]
#print(ftpurl) 

# 读取环境变量的值
ftpurl = os.environ.get('linebot_ftpurl')


# 确保当前目录下存在 "admin" 文件夹
if not os.path.exists("admin"):
    os.makedirs("admin")
    
# Channel Access Token 
#
# Channel Secret

line_access_token = os.environ.get('line_Token')
line_channel_secret = os.environ.get('line_Channel_Secret')

print("secret " + line_channel_secret)
print("token " + line_access_token)


line_bot_api = LineBotApi(line_access_token)
handler = WebhookHandler(line_channel_secret)




# 監聽所有來自 /callback 的 Post Request
@app.route("/rich4u", methods=['POST'])
def callback():

    print(" 0000 - 開始 call back 處理")
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
  
    try:
        print(" handle webhook body")
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
   #print("0000 - CALL BACK 處理結束 ")
    return 'OK'  #ok(200)


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):


    print("  0010 - 開始 處理 handle message entry")
    user_id = ""
    group_id = ""
    usr =event.source.user_id
    user_id = event.source.user_id
    user_type = event.source.type
    if user_type != "user" :
        group_id =  event.source.group_id
    
    line_user_id = usr
    ftpurl = get_ftpurl()

    userFolder = check_line_id(ftpurl ,line_user_id)
    print("userFolder " + userFolder)
    msg = event.message.text

    #@#SETUP#mdcgrniu           https://mdcgenius.000webhostapp.com/
    wkmsg = msg.split('#')

    line_access_token = os.environ.get('line_Token')
    #line_channel_secret = os.environ.get('line_Channel_Secret')
    line_bot_api = LineBotApi(line_access_token)
    if  msg[0:5].upper() == "@HELP"  :    
        msg = '@#token# \n/smail#nnn#\n/demomail#receiver#\n@INFO'
        message = TextSendMessage(text="指令表 \n" + msg)
        line_bot_api.reply_message(event.reply_token, message)  
        return 
     

    if  msg[0:5].upper() == "@INFO"  :
        
            wsinformation = get_informatiion(usr,group_id,user_type)
            message = TextSendMessage(text="informtion :" + wsinformation)
            line_bot_api.reply_message(event.reply_token, message)  
            return 


    if msg[1:8].upper()  == 'CONTINUE'  or msg[1:] == '繼續' :
        wscontinue =get_continue(line_user_id)
#        print("continue token" + wscontinue)
        msg = wscontinue
        message = TextSendMessage(text="上一次查閱進度 :" + msg)
        line_bot_api.reply_message(event.reply_token, message)  
        return 

    

    # first 4 char 
    # last 5 char string[-5:])
    # string.upper
    # string.lower
     

    
    if msg[0:1] == "@" :
#        print("token url " + ftpurl + "  token : " + msg[1:])
        wmsg = get_run_command(ftpurl,msg[1:].strip('\n') )
        if wmsg == 'NF' :
            message = TextSendMessage(text="找不到您要執行的命令 :" + msg)
            line_bot_api.reply_message(event.reply_token, message)   
            return 
        else :
#            print ("convert msg " + wmsg)
            msg = wmsg


    #if msg.startswith('#'):
#        url=githubutl +  "key.txt"
#        url = "http://mdcgenius.tw/key.txt"
#        file = urllib.request.urlopen(url)
#        wkey =  file.readline()
#        openai.api_key = wkey.decode('utf-8') 
     #   openai.api_key = gpt_token.decode('utf-8') 
        #file.close()
     #   gpt_response = openai.Completion.create(
     #       engine='text-davinci-003',
     #       prompt=msg[1:],
     #       temperature=0.5,
     #       n=1,
     #       max_tokens=200
     #   ).choices[0].text

    #    gpt_response =gpt_response[0:20]
    #    print("Line BOT reply ======>" + gpt_response)
    #    try :
    #        line_bot_api.reply_message(
    #            event.reply_token,
    #            TextSendMessage(text="line bot reply gpt \n" + gpt_response)
    #        )
    #    except:
    #        exc_type, exc_value, exc_traceback = sys.exc_info()
    #        print("Exception Type:===>", exc_type)
    #        print("Exception Value:", exc_value)
    #        print("Traceback Object:", exc_traceback)
    
    if '/SMAIL' in msg.upper():     #isupper(), islower(), lower(), upper()
        print (" CALL Send Mail")
        if userFolder == '' :
            message = TextSendMessage(text= "找不到 發送信件的授權資料，請記住您的代碼 " + usr +"\n與 系統管理員聯絡申請授權 " )
            line_bot_api.reply_message(event.reply_token, message)              
        from datetime import datetime
        now = datetime.now() # current date and time
        #增加 user folder
        sendlog = send_mail(usr,msg,userFolder,user_id, group_id)
        print("send mail complete #############################################")
    
        #message = TextSendMessage(text= "完成信件發送 : " + sendlog)
        #line_bot_api.reply_message(event.reply_token, message)  
    elif msg.upper()[0:9] == '/DEMOMAIL'  :
        sendlog = demomail(msg)
        message = TextSendMessage(text= "完成信件發送 : " + sendlog)
        
        line_bot_api.reply_message(event.reply_token, message)          
           
    
#    elif '/init' in msg:
#        wsts = initcounter(usr,msg,userFolder) 
#        message = TextSendMessage(text= wsts)
#        line_bot_api.reply_message(event.reply_token, message)   
#    elif '/load' in msg:
#          loadsts  = loadfile(usr,msg,userFolder) 
#          print(loadsts)
#          message = TextSendMessage(text= "檔案設置處理 : " + loadsts)
#          line_bot_api.reply_message(event.reply_token, message)            
   
    #elif '最新合作廠商' in msg:
    #elif msg.upper()[0:5] == '/MAIN'  : #'/image#cbd' in msg:   
    #    message = imagemap_5(msg)
    #    line_bot_api.reply_message(event.reply_token, message)
    #elif '最新活動訊息' in msg:
    elif msg.upper()[0:2] == '&&' or msg.upper()[0:2] == "&%" :
        #write_continue(line_user_id,msg)
        message = token(msg)
        line_bot_api.reply_message(event.reply_token, message)
    else :
        user_id = event.source.user_id
        user_type = event.source.type
        print("echo message " + user_id)
        #if user_type == "user":
        #    if user_id.startswith("U"):
        #    # 手機版的 LINE
        #        reply_text = "您是使用手機版的 LINE"
        #    else:
        #        # 電腦版的 LINE
        #        reply_text = "您是使用電腦版的 LINE"
        #else:
        #    # 群組或聊天室
        #    reply_text = "您是在群組或聊天室中"

        #print(line_access_token)
        channel_access_token = "gd2k8snxpn3PP+nC+spxDIgQF6ZTtjfS/vHmqOIEJ8W/B1bryahPh61EfFIepnHqfjTQ4zhc29120TvtHVjk4dMB5vkrJFtvcjO07389gomlkggI/rMJCoid9PCCr6O3v0dTY2R3n4FFA6IMr1D5twdB04t89/1O/w1cDnyilFU="
        print("channel_access_token *" + channel_access_token + "*")
        print("   line_access_token *" + line_access_token + "*")
# 建立 LineBotApi 物件
        line_bot_api = LineBotApi(channel_access_token) #line_access_token)
        message = TextSendMessage(text=" 您說 " + msg  )
        line_bot_api.reply_message(event.reply_token,  message )
        return('')
    

        print(reply_text)    
        message = TextSendMessage(text= reply_text) # + "\您是說 : " + msg + "嗎? " )
        print("message \n" + message.text)
        line_bot_api.reply_message(event.reply_token,  message )

    
     
    

@handler.add(PostbackEvent)
def handle_message(event):
    message = token(event.postback.data)
    #print (" message = " + message )
    line_bot_api.reply_message(event.reply_token, message)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id

    print("add member event ")
    print(event)
    profile = line_bot_api.get_group_member_profile(gid, uid)

    print(" new member profile : ")
    print (profile)
    name = profile.display_name
    ids = profile.user_id
    text = input("Enter text: ")
    filename = "users.txt"
    if os.path.exists(filename):
        mode = "a"
    else:
        mode = "w"

    with open(filename, mode) as file:
        file.write(ids + "-" + name  + "\n")

    print( " add new one : " +ids + "-" + name  + "\n")

    message = TextSendMessage(text=f'{name}歡迎加入 MDC 富裕與您同在')
    line_bot_api.reply_message(event.reply_token, message)

def token(msg):
#def token(line_user_id,msg):
    wmsg = msg[2:]
    wkmsg = msg.split('#')
    with open("admin/config.json", "r", encoding="utf-8") as f:
         loaded_data = json.load(f)

    wsftpflr = loaded_data["ftpurl"]
     
    print("TOKEN + "  + msg)
    url = wsftpflr + "json/" + wkmsg[1] + ".json"
    wurlfile = check_url_file(url)
    message = ''

    if wurlfile != '' :
        message = TextSendMessage(text= "工作指令" + url + " 不存在\n請與管理者聯絡")
        return message
  
    if msg[0:2] == "&&" :
        write_continue(line_user_id,msg)

    if  wkmsg[2]  == "carousel_1" :
        message = carousel_1(msg)
    elif  wkmsg[2]  == "carousel_2" :
        message = carousel_2(msg)
    elif  wkmsg[2]  == "carousel_3" :
        message = carousel_3(msg)
    elif  wkmsg[2]  == "text_10" :
        message = text_10(msg)        
    elif  wkmsg[2]  == "text_20" :
        message = text_20(msg)
    elif  wkmsg[2]  == "button_dd" : 
        message = buttons_dd(msg)         
    elif  wkmsg[2]  == "button_ud" : 
        message = buttons_ud(msg)    
    elif  wkmsg[2]  == "button_u2d" : 
        message = buttons_u2d(msg)              
    elif  wkmsg[2]  == "button_40" :
        message = buttons_40(msg)
    elif  wkmsg[2]  == "button_30" :
        message = buttons_30(msg)
    elif wkmsg[2] == "button_31" :
        message = buttons_31(msg)    
    elif wkmsg[2] == "button_01" :
        message = buttons_01(msg)    
    elif wkmsg[2] == "button_10" :
        message = buttons_10(msg)    
    elif wkmsg[2] == "button_02" :
        message = buttons_02(msg)                  
    elif wkmsg[2] == "button_11" :
        message = buttons_11(msg)          
    elif wkmsg[2] == "button_20" :
        message = buttons_20(msg)          
    elif wkmsg[2] == "button_03" :
        message = buttons_03(msg)  
    elif wkmsg[2] == "button_04" :
        message = buttons_04(msg)  
    elif wkmsg[2] == "button_40" :
        message = buttons_40(msg)   
    elif wkmsg[2] == "image_50" :    
        message = imagemap_5(wmsg)   
    else :
        message = TextSendMessage(text=  "\您是說 : " + msg + "嗎?")    

    return message    

def get_ftpurl():
    #with open("config.json", "r", encoding="utf-8") as f:
    #    loaded_data = json.load(f)
    #    ftpurl = loaded_data["ftpurl"]
    #    return(ftpurl)
    ftpurl = os.environ.get('linebot_ftpurl')
    return(ftpurl)

def get_informatiion(wsusr,group_id,user_type) :
    wsftp = get_ftpurl()
    #url = ftpurl + "admin/key.json" #+ wjson_file #http://www.abc.com/cust.json"
    #print (" key url " + url )
    ##response = urllib.request.urlopen(url)
    #data = response.read().decode("utf-8")
    #loaded_data = json.loads(data)

    wsline_access_token = os.environ.get('linebot_Token')
    wsline_channel_secret = os.environ.get('line_Channel_Secret')
    

    return ("\ntype : " + user_type + "\n\nGroup :" + group_id + "\n\nUSER : " + wsusr + "\n\n work ftp " + wsftp + "\n\n Line Access token " +  wsline_access_token + "\n\nChannel Secret" + wsline_channel_secret)
    
    
def loadfile():
   #可以使用 Python 的 urllib 模組中的 urlretrieve() 函式來下載檔案。以下是一個示範程式碼：
   #ythonCopy code


   url = 'https://www.example.com/example_file.txt'
   file_name = 'example_file.txt'

   urllib.request.urlretrieve(url, file_name)
   
   #url 是要下載的檔案的 URL，
   # file_name 則是下載後要儲存的檔案名稱和路徑
   # （如果只指定檔案名稱，則預設儲存到目前的資料夾中）。 urlretrieve() 函式會從指定的 URL 下載檔案，並將其儲存在 file_name 指定的位置。   

 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
