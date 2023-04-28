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
 
def smtp_check(  user_id,group_id):
   
    smtpfn =""
    mailfn = ""
    subjectfn =""
    bodyfn = ""
    smtpidx = ""
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
    smtp_idx = 0
    smtp_username = smtp_list[smtp_idx][0]
    smtp_password = smtp_list[smtp_idx][1]
    smtp_sender = smtp_list[smtp_idx][2]

 


     
    
    #for j, row in enumerate(rows):    #rows : mail.csv
    smtp_idx = 0
    while  smtp_idx <  len(smtp_list) :
        smtp_username = smtp_list[smtp_idx][0]
        smtp_password = smtp_list[smtp_idx][1]
        smtp_idx = smtp_idx + 1
        wserrmsg = ("第 " + str(smtp_idx) + " 登錄中 ：" +  smtp_username )
        message = TextSendMessage(text=wserrmsg )
        line_bot_api.push_message(push_to , message)
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()

            server.login(smtp_username,       smtp_password)
            time.sleep(1)

        except :
            exc_type, exc_value, exc_traceback = sys.exc_info()
            #print("Exception Type:===>", exc_type)
            #print("Exception Value:", exc_value)
            #print("Traceback Object:", exc_traceback)
            wserrmsg = ("第 " + str(smtp_idx) + " 登錄失敗 ：" +  smtp_username )
            print("第 " + str(smtp_idx) + " 登錄失敗 ：" +  smtp_username )
            message = TextSendMessage(text=wserrmsg )
            line_bot_api.push_message(push_to , message)
    
                        
         
    line_bot_api = LineBotApi(line_access_token)
    message = TextSendMessage(text="結束 Smtp Check  " )
    return("")


