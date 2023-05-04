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
import requests

# LINT BOT API
from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
from linebot import LineBotApi, WebhookHandler
#from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from flask import Flask, request, abort
# LINEＢＯＴ　ＡＰＩ
 
from bs4 import BeautifulSoup

 
from flask import Flask
#app = Flask(__name__)
#@app.route('/')
 #================= for send mail =================
 
def send_mail(lineid,wmsg,userFolder, user_id,group_id):
    print(" aaaa 開始發送信件 " + wmsg )
    smtpfn =""
    mailfn = ""
    subjectfn =""
    bodyfn = ""
    smtpidx = ""
    mailidx = ""
    isnew = 'N'
    wsftpflr = '' 
    wsftpflr =  os.environ.get('linebot_ftpurl')
    line_access_token = os.environ.get('line_Token')


#    tracemsg(line_access_token,"開始發送信件 ",user_id)
    push_to = ""
    if group_id != "":
        push_to = group_id 
    else :
        push_to = user_id    
    line_bot_api = LineBotApi(line_access_token)
    message = TextSendMessage(text= "send_heartbeat")
    line_bot_api.push_message(push_to, message)

    send_heartbeat1(line_access_token,push_to)
    line_bot_api = LineBotApi(line_access_token)
    message = TextSendMessage(text= "send_heartbeat complete")
    line_bot_api.push_message(push_to, message)

 # 發送比數
    wsmsg =  wmsg.split('#')   # msg = '/smail#90#'
    wstarget = wsmsg[1]
    if (wstarget.isdigit()):
        targetno = int(wstarget)
    else : 
        targetno = 0
        return("發送信件格式 錯誤\n正確格式==>/SMAIL:nnnn\n 結束作業 :*" + wstarget +"*")   
     
    
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


    directory = "tmp"  # 要创建的目录名称

    #try:
    #    os.makedirs(directory)
    #    print("目录已成功创建")
    #except FileExistsError:
    ##    print("目录已经存在")
    #except OSError as e:
    #    print("创建目录时出错:", e)

    
  #  if not os.path.exists('tmp' ):
  #      os.makedirs('tmp')

# 取得 發送紀錄
    logfn = 'sendmail.log'  #build_logfn(mailfn) + '_log.txt'
    if file_exsit(logfn) == 'N':
        wserrmsg = "發送紀錄 不存在 "
        tracemsg(line_access_token,wserrmsg,push_to)
        return()
    
    file = open('sendmail.log','r',encoding="utf-8")
    wslog  = file.readline()
    wslogs = wslog.split(',') #subject = wsubject #.decode('utf-8') 
    wserrmsg =  ' '.join (str(e) for e in wslogs)  + " sendmail.log " + wslogs[0] + ' ' + mailfn 
    wserrmsg =  wslog   + "- sendmail.log " + wslogs[0] + ' ' + mailfn 
    #tracemsg(line_access_token,wserrmsg,push_to)
   
    if wslogs[0] != mailfn  :
        wslogs[1] = mailidx
        wslogs[2] = smtpidx 
        wslogs[3] = '0'
        wstr = mailfn + "," + mailidx + "," + smtpidx + "," + '0'
        isnew = 'Y'
        #tracemsg(line_access_token,"writ new sendmail.log ",push_to)
        with open("sendmail.log", "w", encoding="utf-8") as f:            
            f.write(wstr) 
            f.close()
        file = open('sendmail.log','r',encoding="utf-8")
        wslog  = file.readline()
        wslogs = wslog.split(',') #subject = wsubject #.decode('utf-8')     
        wserrmsg =  ' '.join (str(e) for e in wslogs)  + " sendmail.log " + wslogs[0] + ' ' + mailfn 
        #tracemsg(line_access_token,wserrmsg,push_to)
        
        f.close()
             
    #else :
    #    tracemsg(line_access_token,wserrmsg,push_to)

    mailidx = wslogs[1]
    smtpidx = wslogs[2]
    sendcnt = int(wslogs[3]) + 1
    #return()
    file.close()

#  @@@@@@@@   mailfn + "_log"   123,11   123 :mailidx   11:smtpidx
#  檢查  local mail.csv 
#     如如果 不存在 copy url file 

    #https://github.com/MDCR4U/LineBot/blob/main/mail.csv
    
    smtp_server = "smtp.office365.com"
    smtp_port = 587

    
    if isnew == 'Y' :
        tracemsg(line_access_token," copy from url ",push_to)
        url = wsftpflr + userFolder.strip('\n') + "/" + smtpfn   #"/smtp.csv"
        copy_to_local(url ,  smtpfn )
        send_heartbeat()
        url = wsftpflr + userFolder.strip('\n') +"/" + mailfn #'/mail.csv'
        copy_to_local(url , mailfn )
        send_heartbeat()
        url = wsftpflr + userFolder.strip('\n') + "/" + bodyfn # '/body.txt'
        copy_to_local(url , bodyfn )
        send_heartbeat()
        url = wsftpflr + userFolder.strip('\n') +  "/" + subjectfn #'/subject.txt'
        copy_to_local(url , subjectfn )
        send_heartbeat()


    with open( smtpfn, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        smtp_list = [row for row in reader]        
    wsstr = ' '.join (str(e) for e in smtp_list)
    wserrmsg = "smtp list   \n" + wsstr
    #tracemsg(line_access_token,wserrmsg,push_to)
    
    # url file
    if 1 == 2 :                # url file
        try:
            response = urllib.request.urlopen(url)                                              # 開啟 URL
            reader = csv.reader(response.read().decode('utf-8').splitlines())                   # 讀取 CSV 檔案
            next(reader)                                                                        # 跳過表頭
            smtp_list = [row for row in reader]                                                 # 轉換為列表
            response.close()                                                                    # 關閉 URL
            smtp_count = len(smtp_list)   
        except :
            return ("寄件者資料 讀取錯誤 \n " + url)

#    print("發信者 人數" + str(len(smtp_list)))
# 讀取郵件發送記錄
    counter = int(mailidx)
    smtp_idx = int(smtpidx)    
   #try:
    #    with open("smtp_send_counter.log", "r", encoding="utf-8") as f:
    #        smtp_idx  = int(f.readline())
    #except FileNotFoundError:
    #    smtp_idx  = 0        


# 讀取收件人列表
    #url = wsftpflr + userFolder.strip('\n') + '_mail.csv'

    n = counter                                                 # 要跳過的行數
  

    with open(mailfn, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = [row for i, row in enumerate(reader) if i >= n]
        #rows = [row for i, row in enumerate(reader) if i == n]   # 只得取  第 n筆
        wsstr = ' '.join (str(e) for e in rows)  + '----' + str(counter)
        wserrmsg = "mails   \n" + wsstr + "-" + str(len(rows))
        #tracemsg(line_access_token,wserrmsg,push_to)

    if 1 ==2 :       # url file
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

    file = open(bodyfn,'r',encoding="utf-8")
    content = ''
    wsbody  = file.readline()
    while wsbody:
            content  = content + wsbody #.decode('utf-8') 
            wsbody  = file.readline()
    file.close()

    #wserrmsg = "body   \n" +  content 
    #tracemsg(line_access_token,wserrmsg,push_to)


    if 1==2  :    #url file
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

    file = open(subjectfn,'r',encoding="utf-8")
    wsubject  = file.readline()
    subject = wsubject #.decode('utf-8') 
    file.close()
    wserrmsg = "subject  \n" +  subject  + wmsg
    #tracemsg(line_access_token,wserrmsg,push_to)

    #return 

    if 1 == 2:    #ｕｒｌ　ｆｉｌｅ
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
    #sendcnt = 0
    loopidx = 0 
    wsmail_cnt = len(rows)
    
    for j, row in enumerate(rows):    #rows : mail.csv
         
        if smtp_idx >= len (smtp_list) :
           smtp_idx  = 0
        else :
            smtp_idx = smtp_idx + 1
        smtp_username = smtp_list[smtp_idx][0]
        smtp_password = smtp_list[smtp_idx][1]
        
        to_addr = row[0]

        #cc_addrs = [x for x in row[1:batch_size+1] if x and "@" in x]
        #print(cc_addrs)
        #subject = smtp_username +"臉書優質紛絲團，邀請您 按讚支持"
        #content =  "陌生開發優質粉絲團，人員募集中\n歡迎加入\n分享陌開心法及免費工具\n邀起您加入我們 請開啟網址 https://www.facebook.com/profile.php?id=100065188140659 按讚留言 獲取更多的資訊\n www.mydailychoice.com"
    # 準備發送郵件
        message = MIMEMultipart()
        #message["From"] = smtp_list
        message["From"] =    smtp_sender + " <" + smtp_username +">"  
        message["To"] = to_addr  
    
    #if cc_addrs:
    #    message["Cc"] = ",".join(cc_addrs)
            #cc_email = 'eel.honey@yahoo.com.tw,ejob@livemail.tw'.split(',')
    #message['Cc'] = ','.join(cc_email)
        message["Subject"] = subject
        message.attach(MIMEText(content, "plain", "utf-8"))
    # 添加附件
    #filename = "test.txt"
    #with open(filename, "rb") as attachment:
    #    part = MIMEApplication(attachment.read(), Name=filename)
    #    part["Content-Disposition"] = f'attachment; filename="{filename}"'
    #    message.attach(part)
    
    # 發送郵件
        wserr = 'N'
        seq = j
        send_heartbeat()
        try:
            send_heartbeat()
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            wk_addr="$$$$$"
            send_heartbeat()
            server.login(smtp_username,       smtp_password)
            time.sleep(0.5)

            wk_addr = to_addr 
            #tracemsg(line_access_token,"server.sendmail " ,user_id)    
            send_heartbeat() 
            server.sendmail(smtp_username,  wk_addr  , message.as_string())
            server.quit()
            send_heartbeat()
            wssendcounter = wssendcounter + 1
        #except Exception as e:
        except :
            exc_type, exc_value, exc_traceback = sys.exc_info()
            #print("Exception Type:===>", exc_type)
            #print("Exception Value:", exc_value)
            #print("Traceback Object:", exc_traceback)
            print("第 " + str( seq  + 1) + " 封郵件發送失敗 ：" +  smtp_username )
            wserrmsg = "第 " +  str(counter) + " 信件發送失敗 " + "\n\n  信箱 " + smtp_username + "  可能暫時被封鎖 ，請使用 outlook.com 登入，並依照指示作解鎖\n"
            tracemsg(line_access_token,wserrmsg,push_to)
            wserr = 'Y'
            
         
        #loopidx = loopidx + 1
        sendcnt = sendcnt + 1
        if wserr == 'N':
            print (" 第 " + str(counter) + "發送成功")
            line_bot_api = LineBotApi(line_access_token)
            message = TextSendMessage(text= "發送   :" +  str(counter) + "封 信件發送"  + smtp_sender + " <" + smtp_username +">   ==> " +  to_addr + " " + str(wspush) + " " + str(sendcnt))
            #line_bot_api.push_message(push_to, message)
        else:
            line_bot_api = LineBotApi(line_access_token)
            message = TextSendMessage(text= "continue 發送   :")
            line_bot_api.push_message(push_to, message)            
            
        if sendcnt >= wspush :
                line_bot_api = LineBotApi(line_access_token)
                message = TextSendMessage(text="累計已完成   :" +  str(counter) + "-" + str(targetno) + " 封 信件發送" )
                line_bot_api.push_message(push_to, message)
                sendcnt = 0
        send_heartbeat()
        if counter   >= targetno    :
            print(f"{targetno} emails complete " + push_to)  
        #    wssenddetail = wssenddetail + str(loopidx)  + ",  "   + " " + smtp_username + "=> " + to_addr   + "\n"
            message = TextSendMessage(text="發送完成  累計發送   :" +  str(targetno)  + " 封信件" )
            line_bot_api = LineBotApi(line_access_token)
            line_bot_api.push_message(push_to, message)
            return("") 
        print(wserr)

        line_bot_api = LineBotApi(line_access_token)
        #if wserr == 'Y':
        ##    
        #    message = TextSendMessage(text= "continue " )
        #    line_bot_api.push_message(push_to, message)

        message = TextSendMessage(text= "trace message" )
        line_bot_api.push_message(push_to, message)
        send_heartbeat()
        print("sleep佛如nextprocess")
        message = TextSendMessage(text= str(counter) )
        line_bot_api.push_message(push_to, message)            
        print(" sleep 0.5 sec contiue")
        counter = counter +1
        #sendcnt = sendcnt + 1
        wstr = mailfn + "," + str(counter) + "," + str(smtp_idx) + "," + str(sendcnt) 
        with open("sendmail.log", "w", encoding="utf-8") as f:            
                f.write(wstr) 
        print (wstr)   
        f.close()
        print("sleep for next")
        time.sleep(0.5)
        line_bot_api = LineBotApi(line_access_token)
        message = TextSendMessage(text= " sleep 0.5 sec contiue" )
        #line_bot_api.push_message(push_to, message)
        print(" sleep 0.5 sec contiue")
        send_heartbeat()

    message = TextSendMessage(text=" raise send post msg " + wstr  )
    line_bot_api = LineBotApi(line_access_token)
    line_bot_api.push_message(push_to, message)
    
    # 記錄已發送的郵件
    #    sent_list.append(f"{to_addr},{subject}")
    #    #with open(userFolder.strip('\n') + "_SEND.LOG", "a", encoding="utf-8") as f:
    #    with open(userFolder.strip('\n') + "_SEND.LOG", "a", encoding="utf-8") as f:
    #        f.write(f"{loopidx} , {datetime.datetime.now()},  {to_addr},{subject}\n")
    #        now = datetime.datetime.now()
    #        wssenddetail = wssenddetail + str(loopidx)  + ",  "  + " " + smtp_username + "=> " + to_addr   + "\n"
 

    # 更新郵件smtp記錄
    #    #with open(userFolder.strip('\n') + "_smtp_send_counter.log", "w", encoding="utf-8") as f:
    #    with open(userFolder.strip('\n') + "_smtp_send_counter.log", "w", encoding="utf-8") as f:            
    #        f.write(str(smtp_idx))        
    # 更新郵件發送記錄
    #    counter += 1
        #with open(userFolder.strip('\n') +"_mail_counter.log", "w", encoding="utf-8") as f:
        #with open(userFolder.strip('\n') +"/mail_counter.log", "w", encoding="utf-8") as f:    
        #    f.write(str(counter))
        
    time.sleep(0.5)
    line_bot_api = LineBotApi(line_access_token)
    message = TextSendMessage(text="結束 SMAIL " )
    #line_bot_api.push_message(push_to , message)
    
    return("")
def build_logfn(wsfn):
    wssplit = wsfn.split('.')
    return wssplit[0]

def copy_to_local(url , filename):
    print ("copy to local " + url  + " " + filename)
    try:
        urllib.request.urlretrieve(url, filename)
        print("文件已成功复制到本地")
    except urllib.error.URLError as e:
        print("下载文件时出错:", e)
    print("download " + url   + " to " + filename )

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
    print ('check file ' + filename)
    if os.path.exists(filename):
        print(f'File {filename} exists')
        return  ''
    else:
        print(f'File {filename} does not exist')
        wsreturn = 'File  : ' + filename + ' does not exist'
        return 'N' #wsreturn 
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


 
#
##from linebot.models import TextSendMessage
#import requests

def send_heartbeat1(line_access_token, to):
    # 发送心跳请求
    line_bot_api = LineBotApi(line_access_token)
    message = TextSendMessage(text="REQUEST GET")
    line_bot_api.push_message(to, message)

    response = requests.get('https://mdcbot9.onrender.com/heartbeat')  # 替换为你的应用程序的 URL
    if response.status_code == 200:
        response_text = response.text
        line_bot_api = LineBotApi(line_access_token)
        message = TextSendMessage(text=response_text)
        line_bot_api.push_message(to, message)
    else:
        error_message = "Failed to send heartbeat"
        line_bot_api = LineBotApi(line_access_token)
        message = TextSendMessage(text=error_message)
        line_bot_api.push_message(to, message)

    # 检查响应状态码
    if response.status_code == 200:
        print('Heartbeat sent successfully')
    else:
        print('Failed to send heartbeat')    
def send_heartbeat():
    # 发送心跳请求
  

    response = requests.get('https://mdcbot9.onrender.com/heartbeat')  # 替换为你的应用程序的 URL
   

    # 检查响应状态码
    if response.status_code == 200:
        print('Heartbeat sent successfully')
    else:
        print('Failed to send heartbeat')

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

from linebot import LineBotApi
from linebot.models import TextSendMessage, PostbackAction, QuickReply

#https://mdcgenius.000webhostapp.com/admin/smail.html?from=facebook%20%3Cjj0922792265@outlook.com%3E&pwd=toyota1234&to=ejob@livemail.tw&subject=subject230409.txt&body=body230409.txt

def listfile():

    url = "https://mdcbot9.onrender.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all("a"):
        file_url = url + link.get("href")
        print(file_url)
#if __name__ == '__main__':
#    app.run()