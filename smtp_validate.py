# for upload file
import urllib.request

import sys
#
import os  
import json
import csv
import datetime
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# LINT BOT API
from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
from linebot import LineBotApi, WebhookHandler
#from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from flask import Flask, request, abort
# LINEＢＯＴ　ＡＰＩ

 
from flask import Flask
#app = Flask(__name__)
#@app.route('/')
 #================= for send mail =================
def tracemsg(line_access_token,msg,to ):
    line_bot_api = LineBotApi(line_access_token)
    message = TextSendMessage(text=msg )
    line_bot_api.push_message(to , message) 

def smtp_check(  msg,user_id,group_id):
    wmsg =msg.split('#')
    if len(wmsg) == 1 :
        print ("invalid no  /smpt#n#")

    smtpfn =""
    mailfn = ""
    subjectfn =""
    bodyfn = ""
    print(wmsg[1])
 
    smtp_idx = int(wmsg[1])

    mailidx = ""

    wsftpflr = '' 
    wsftpflr =  os.environ.get('linebot_ftpurl')
    line_access_token = os.environ.get('line_Token')
 
    line_bot_api = LineBotApi(line_access_token)


#    tracemsg(line_access_token,"開始發送信件 ",user_id)
    push_to = ""
    if group_id != "":
        push_to = group_id 
    else :
        push_to = user_id    
 
     
# 取得發送郵件  環境
    mailconfig= "mailconfig.json"
    url = wsftpflr + "admin/" + mailconfig #http://www.abc.com/cust.json"
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    smtpfn =js_dta["smtp"] 
     




    #https://github.com/MDCR4U/LineBot/blob/main/mail.csv
    
    smtp_server = "smtp.office365.com"
    smtp_port = 587

    url = wsftpflr +  "admin/" + smtpfn   #"/smtp.csv"
    
    try:
        response = urllib.request.urlopen(url)                                              # 開啟 URL
        reader = csv.reader(response.read().decode('utf-8').splitlines())                   # 讀取 CSV 檔案
        next(reader)                                                                        # 跳過表頭
        smtp_list = [row for row in reader]                                                 # 轉換為列表
        response.close()                                                                    # 關閉 URL
        smtp_count = len(smtp_list)   
    except :
        return ("寄件者資料 讀取錯誤 \n " + url)

 

# 設置發件人的初始賬戶信息
    #smtp_idx = 0
    smtp_username = smtp_list[smtp_idx][0]
    smtp_password = smtp_list[smtp_idx][1]
    smtp_sender = smtp_list[smtp_idx][2]

 


     
    
    #for j, row in enumerate(rows):    #rows : mail.csv
    #smtp_idx = 0
    wsc = 1
    wsfail = "N"
    while  smtp_idx <  len(smtp_list) :
        smtp_username = smtp_list[smtp_idx][0]
        smtp_password = smtp_list[smtp_idx][1]
        smtp_idx = smtp_idx + 1
        if wsfail == 'Y':
            wserrmsg = ("第 " + str(smtp_idx) + "-" + str(len(smtp_list)) + "  登錄中 ：" +  smtp_username )
            message = TextSendMessage(text=wserrmsg )
            line_bot_api.push_message(push_to , message)
            
        try:
            if wsfail == 'Y':
                tracemsg( line_access_token,"init server " ,push_to)
                
            server = smtplib.SMTP(smtp_server, smtp_port)
            if wsfail == 'Y':
                tracemsg( line_access_token,"start ttls " ,push_to)
            server.starttls()
            if wsfail == 'Y':
                tracemsg( line_access_token,"login" ,push_to)
            
            server.login(smtp_username,       smtp_password)
            if wsfail == 'Y':
                tracemsg( line_access_token,"login complete  " ,push_to)
                wsfail = 'N'
                        
            time.sleep(0.5)

        except :
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print("Exception Type:===>", exc_type)
            print("Exception Value:", exc_value)
            print("Traceback Object:", exc_traceback)
           
            print("第 " + str(smtp_idx) + " 登錄失敗 ：" +  smtp_username )
            wsfail = "Y"
            
        if wsfail == 'Y'    :
             wserrmsg = ("第 " + str(smtp_idx) + " 登錄失敗 ：" +  smtp_username  + " " + smtp_password )
             message = TextSendMessage(text=wserrmsg )
             line_bot_api.push_message(push_to , message)
        if wsmail == 'N':     
            server.quit()
        if wsc == 3 :
            if wsmail =='N':
                wserrmsg = ("第 " + str(smtp_idx) + "-" + str(len(smtp_list)) + "  登錄成功 ：" +  smtp_username )
                message = TextSendMessage(text=wserrmsg )
                line_bot_api.push_message(push_to , message)
                wsc = 0
            else :
                wsc = wsc - 1    
        wsc = wsc +1
                        
         
    line_bot_api = LineBotApi(line_access_token)
    message = TextSendMessage(text="結束 Smtp Check  " )
    line_bot_api.push_message(push_to , message)
    return("")


