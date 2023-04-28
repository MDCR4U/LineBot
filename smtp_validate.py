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
 
def smtp_validate(lineid,wmsg,userFolder, user_id,group_id):
   
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

    
 # 發送比數
    
    wssts = check_line_id(wsftpflr,lineid)
    if   wssts == ''  :
        return ('使用者 ' + lineid + ' 發送信件功能未啟動')
     
# 取得發送郵件  環境
    mailconfig= "mailconfig.json"
    url = wsftpflr + "admin/" + mailconfig #http://www.abc.com/cust.json"
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    smtpfn =js_dta["smtp"] 
    mailfn = js_dta["mail"] 
    subjectfn =js_dta["subject"] 
    bodyfn = js_dta["body"] 
    smtpidx = js_dta["smtpidx"] 
    mailidx = js_dta["mailidx"] 
    wspush = int(js_dta["push"])




    #https://github.com/MDCR4U/LineBot/blob/main/mail.csv
    
    smtp_server = "smtp.office365.com"
    smtp_port = 587

    url = wsftpflr + userFolder.strip('\n') + "/" + smtpfn   #"/smtp.csv"
    
    try:
        response = urllib.request.urlopen(url)                                              # 開啟 URL
        reader = csv.reader(response.read().decode('utf-8').splitlines())                   # 讀取 CSV 檔案
        next(reader)                                                                        # 跳過表頭
        smtp_list = [row for row in reader]                                                 # 轉換為列表
        response.close()                                                                    # 關閉 URL
        smtp_count = len(smtp_list)   
    except :
        return ("寄件者資料 讀取錯誤 \n " + url)


    try:
        with urllib.request.urlopen(url) as response:
            reader = csv.reader(response.read().decode('utf-8').splitlines())
            rows = [row for i, row in enumerate(reader) if i >= n]
    except urllib.error.URLError:
        return ("收件者資料讀取錯誤 : " + url )

# 設置發件人的初始賬戶信息
     
    smtp_username = smtp_list[smtp_idx][0]
    smtp_password = smtp_list[smtp_idx][1]
    smtp_sender = smtp_list[smtp_idx][2]

# 設置發送成功的郵件地址和主旨的列表
    sent_list = []

# 每個批次的大小
    batch_size = 2
#  初始化 發送紀錄數
   
    wssendcounter = 0
    wssenddetail = ""

#getbody 
    # 檢查 發送內容
    url = wsftpflr + userFolder.strip('\n') + "/" + bodyfn # '/body.txt'
    try:
        file = urllib.request.urlopen(url)
        content = ''
        wsbody  = file.readline()
        while wsbody:
            content  = content + wsbody.decode('utf-8') 
            wsbody  = file.readline()
    # 關閉 URL
        file.close()
    except :
         return ("信件內容錯誤 :" + url)     
    


#getsubject 

     # 檢查 主旨
    #url = url = wsftpflr + userFolder.strip('\n') +  '_subject.txt'
    url = wsftpflr + userFolder.strip('\n') +  "/" + subjectfn #'/subject.txt'
    try:
        file = urllib.request.urlopen(url)
        wsubject = ''
        wsubject  = file.readline()
        subject = wsubject.decode('utf-8') 
    # 關閉 URL
        file.close()
    except:     
        return ("信件主旨讀取錯誤:"+ url)
 
 

# 開始發送郵件
    sendcnt = 0
    loopidx = 0 
    
    #for j, row in enumerate(rows):    #rows : mail.csv
    smtp_idx = 0
    while  smtp_idx <  len(smtp_list) :
        smtp_username = smtp_list[smtp_idx][0]
        smtp_password = smtp_list[smtp_idx][1]
        smtp_idx = smtp_idx + 1

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


def loadfile(lineid,msg,userFolder ):
    
   #可以使用 Python 的 urllib 模組中的 urlretrieve() 函式來下載檔案。以下是一個示範程式碼：
   #ythonCopy code
    file = open('config.txt','r',encoding="utf-8")
    line = file.readline().strip('\n')    #line1 githubid
    line = file.readline().strip('\n')   #line1 githubproject
    line = file.readline().strip('\n')   #line1 githubproject
    #line=line.strip('\n')
    wsftpflr= line[12:].strip()
    
 
    file.close()
    wsflr = ''
    wssts = check_line_id(wsftpflr,lineid)
    if   wssts == ''  :
        print('使用者 ' + lineid + ' 發送信件功能未啟動')
        return ('使用者 ' + lineid + ' 發送信件功能未啟動')
    wsflr = wssts 

    #msg = '/load#smtp230409.csv#smtp.csv#
    wmsg = msg.split("#")
    if len(wmsg) !=3 :
        print ("load file layout error " + len(wmsg))
        return ("load file layout error " + len(wmsg))
    url = wsftpflr + wsflr + "/" + wmsg[1]

    #make folder
    if not os.path.exists(wsflr):
        os.makedirs(wsflr)


    #filename = wsflr + "_" + wmsg[2]
    filename = wsflr + "/" + wmsg[2]
    print ("source from : " + url  + " to: " + filename ) 

    
   #url 是要下載的檔案的 URL，
   # file_name 則是下載後要儲存的檔案名稱和路徑
   # （如果只指定檔案名稱，則預設儲存到目前的資料夾中）。 urlretrieve() 函式會從指定的 URL 下載檔案，並將其儲存在 file_name 指定的位置。   

    urllib.request.urlretrieve(url, filename)
    print("\n" + wmsg[2]  + "上傳完成")
    return("\n" + "source from : " + url  + " to: " + filename + "上傳完成")

   #可以使用 Python 的 urllib 模組中的 urlretrieve() 函式來下載檔案。以下是一個示範程式碼：
   #ythonCopy code


    #url = 'https://mdcgenius.tw/mdcr4ugpt/' + file_name 
     
    #filename = file_name  
    #urllib.request.urlretrieve(url, filename)
    #print("\n" + filename + "上傳完成")
   #url 是要下載的檔案的 URL，
   # file_name 則是下載後要儲存的檔案名稱和路徑
   # （如果只指定檔案名稱，則預設儲存到目前的資料夾中）。 urlretrieve() 函式會從指定的 URL 下載檔案，並將其儲存在 file_name 指定的位置。   
def check_url_file(wsurl):
     
    url = wsurl #'http://www.example.com/filename.txt'
    
    # 使用 urlretrieve() 下載文件
    wsreturn = ''
    
    try:
        filename, headers = urllib.request.urlretrieve(url)
        
    except urllib.error.HTTPError as e:
        print('1.HTTPError:', e.code, url)
        wsreturn  = 'HTTPError:' +  str(e.code) + " " + url
        return wsreturn
    except urllib.error.URLError as e:
        print('URLError:', e.reason, url)
        wsreturn = 'URLError:' +  e.reason + " " +  url
        return wsreturn 
    return ''    
def file_exsit(filename):
    # 檢查文件是否存在
    if os.path.exists(filename):
        print(f'File {filename} exists')
        return  ''
    else:
        print(f'File {filename} does not exist')
        wsreturn = 'File  : ' + filename + ' does not exist'
        return wsreturn 
def initcounter(lineid,msg,userFolder ):
    
   
    file = open('config.txt','r',encoding="utf-8")
    line = file.readline().strip('\n')    #line1 githubid
    line = file.readline().strip('\n')   #line1 githubproject
    line = file.readline().strip('\n')   #line1 githubproject
    #line=line.strip('\n')
    wsftpflr= line[12:].strip()
    file.close()
    wsflr = ''
    wssts = check_line_id(wsftpflr,lineid)
    if   wssts == ''  :
        print('使用者 ' + lineid + ' 發送信件功能未啟動')
        return ('使用者 ' + lineid + ' 發送信件功能未啟動')
    
    #msg = '/initcounter#admin#
    wsflr = wssts

    if wsflr != 'admin':
        return('權限錯誤' + wsflr)

    #url = wsftpflr + wsflr  + "/smtp_send_counter.log" 
    url =  wsflr  + "_smtp_send_counter.log" 
    wslog = url 
    print(" initialize " + url )
    #with open(url, "w", encoding="utf-8") as f:
    with open(url, "w", encoding="utf-8") as f:
            f.write(str(0))        
    # 更新郵件發送記錄
    print("complete ")
    url =  wsflr + "_mail_counter.log" 
    wslog = wslog + "\n" + url
    print(" initialize " + url )
    with open(url , "w", encoding="utf-8") as f:
            f.write(str(0))
    
    return("counter initialize complete " + wslog)


def tracemsg(line_access_token,msg,to ):
    line_bot_api = LineBotApi(line_access_token)
    message = TextSendMessage(text=msg )
    line_bot_api.push_message(to , message)

def check_line_id(ftpurl ,lineid):
     
    url = ftpurl + "authids.txt"

#    print ("authids url " + url )
# 讀取文件內容
    file = urllib.request.urlopen(url)
    line = file.readline()
    while line:
        wslineid = line.decode('utf-8').strip('\n')
        xx = wslineid.split("#", 2)
#        print("authids - " + xx[0] + "-" + xx[1] + "*")
        if   lineid == xx[0]:
#             print("check_line_id return " +xx[1] +"##")
             return(xx[1])  
        line = file.readline()
#    print("check_line_id return space")    
    return("")    


    filename = 'authids.txt'
    print("check_line_id " + url + "-" + filename)
    print(" line id : " + lineid)
    urllib.request.urlretrieve(url, filename)

    with open("authids.txt", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        ids = [row for row in reader]

    print(ids + " " + str(len(ids)  ))
    
    for j, row in enumerate(ids): 
        print(ids[j])
        if   lineid in ids[j]:
             return(ids[j][34:])  
    return (" ")    
 

def test_func(msg):
    wmsg =  "我跟你說一樣的 : " + msg 
    
    return (wmsg )
 
#if __name__ == '__main__':
#    app.run()