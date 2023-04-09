# for upload file
import urllib.request

import sys
#
import os 
import csv
import datetime
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

 
from flask import Flask
#app = Flask(__name__)
#@app.route('/')
 #================= for send mail =================
 
def send_mail(lineid,wmsg,userFolder):
    wsftpflr = '' 
    #print("\n@@@@@ send mail folder @@@@@@@@@@@@@@@@@@@@  = " + userFolder +"@@@")

#讀取 config.sys 取得 information  ftp folder
    file = open('config.txt','r',encoding="utf-8")
    line = file.readline().strip('\n')    #line1 githubid
    line = file.readline().strip('\n')   #line1 githubproject
    line = file.readline().strip('\n')   #line1 githubproject
    #line=line.strip('\n')
    wsftpflr= line[12:].strip()
    #ftpurl = 'https://mdcgenius.000webhostapp.com/key.txt'
 
    file.close()

 
    wstarget = wmsg[7:]
     
    if (wstarget.isdigit()):
        targetno = int(wstarget)
    else : 
        targetno = 0
        return("發送信件格式 錯誤\n正確格式==>/SMAIL:nnnn\n 結束作業 :*" + wstarget +"*")   
     
    
    wssts = check_line_id(wsftpflr,lineid)
    if   wssts == ''  :
        print('使用者 ' + lineid + ' 發送信件功能未啟動')
        return ('使用者 ' + lineid + ' 發送信件功能未啟動')
     


    #https://github.com/MDCR4U/LineBot/blob/main/mail.csv
    
    smtp_server = "smtp.office365.com"
    smtp_port = 587

    print("=====send mail start ")
     
    url = wsftpflr + userFolder.strip('\n') + "_smtp.csv"
 
    
    try:
        response = urllib.request.urlopen(url)                                              # 開啟 URL
        reader = csv.reader(response.read().decode('utf-8').splitlines())                   # 讀取 CSV 檔案
        next(reader)                                                                        # 跳過表頭
        smtp_list = [row for row in reader]                                                 # 轉換為列表
        response.close()                                                                    # 關閉 URL
        smtp_count = len(smtp_list)   
    except :
        print ("寄件者資料 讀取錯誤 \n " + url)
        return ("寄件者資料 讀取錯誤 \n " + url)


# 讀取郵件發送記錄
    url = wsftpflr + userFolder.strip('\n') +  '_mail_counter.log'
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            counter = int(content.strip())
    except urllib.error.URLError:
        counter = 0
   
    #try:
    #    with open("mail_counter.log", "r", encoding="utf-8") as f:
    ##        counter = int(f.readline())
    #except FileNotFoundError:
    #    counter = 0
# 讀取SMTP發送記錄
    url = wsftpflr + userFolder.strip('\n') +  '_smtp_send_counter.log'
    try:
        with urllib.request.urlopen(url) as response:
            smtp_idx = response.read().decode('utf-8')
            smtp_idx = int(content.strip())
    except urllib.error.URLError:
        smtp_idx = 0
   #try:
    #    with open("smtp_send_counter.log", "r", encoding="utf-8") as f:
    #        smtp_idx  = int(f.readline())
    #except FileNotFoundError:
    #    smtp_idx  = 0        


# 讀取收件人列表
    url = wsftpflr + userFolder.strip('\n') + '_mail.csv'
    n = counter                                                 # 要跳過的行數

    try:
        with urllib.request.urlopen(url) as response:
            reader = csv.reader(response.read().decode('utf-8').splitlines())
            rows = [row for i, row in enumerate(reader) if i >= n]
    except urllib.error.URLError:
        print ("收件者資料讀取錯誤 : " + url )
        return ("收件者資料讀取錯誤 : " + url )
    #    rows = []
    #with open("mail.csv", "r", encoding="utf-8") as f:
    #    reader = csv.reader(f)
    #    next(reader)  # 跳過表頭
    #    rows = [row for i, row in enumerate(reader) if i >= counter]
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
    url = wsftpflr + userFolder.strip('\n') + '_body.txt'
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
    url = url = wsftpflr + userFolder.strip('\n') +  '_subject.txt'
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
    loopidx = -1 
    print (str(len(smtp_list)))
    for j, row in enumerate(rows):    #rows : mail.csv
         
        if smtp_idx >= len (smtp_list) :
           print("smtp idx reach max reset")
           smtp_idx  = 0
        else :
            smtp_idx = smtp_idx + 1
        print("**" + str(smtp_idx) + " - " + str(len(smtp_list)) + "**" )
        smtp_username = smtp_list[smtp_idx][0]
        print("user name " + smtp_username)
        smtp_password = smtp_list[smtp_idx][1]
        
        to_addr = row[0]

        print("to_addr = " + to_addr + "-" + row[0])
       
        #cc_addrs = [x for x in row[1:batch_size+1] if x and "@" in x]
        #print(cc_addrs)
        #subject = smtp_username +"臉書優質紛絲團，邀請您 按讚支持"
        #content =  "陌生開發優質粉絲團，人員募集中\n歡迎加入\n分享陌開心法及免費工具\n邀起您加入我們 請開啟網址 https://www.facebook.com/profile.php?id=100065188140659 按讚留言 獲取更多的資訊\n www.mydailychoice.com"
    # 準備發送郵件
        message = MIMEMultipart()
        #message["From"] = smtp_list
        message["From"] =    smtp_sender + "<" + smtp_username +">"  
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
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
#            time.sleep(1)
            wk_addr="$$$$$"
            server.login(smtp_username,       smtp_password)
            time.sleep(1)

            wk_addr = to_addr 
            server.sendmail(smtp_username,  wk_addr  , message.as_string())
             
            server.quit()
            wssendcounter = wssendcounter + 1
        #except Exception as e:
        except :
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print("Exception Type:===>", exc_type)
            print("Exception Value:", exc_value)
            print("Traceback Object:", exc_traceback)
        #    print(f"第 {loopidx } 封郵件發送失敗：{e} \n {smtp_username} {smtp_password} {smtp_port} {wk_addr} \n ")


            #if 'Authentication unsuccessful' in e.decode('utf-8') :
            #    print(f"第 {loopidx } 封郵件發送失敗： Authentication unsuccessful\n  {e} \n {smtp_username} {smtp_password} {smtp_port} {wk_addr} \n ")
            #if 'Authentication unsuccessful' in e.decode('utf-8') :
            wssenddetail = "\n\n  信箱 " + smtp_username + "  可能暫時被封鎖 ，請使用 outlook.com 登入，並依照指示作解鎖\n"
            #return(f"第 {+1} 封郵件發送失敗：{e}  {smtp_username} {smtp_password} {smtp_port} \n + {wssenddetail}")
            return(f"第 {+1} 封郵件發送失敗：   {smtp_username} {smtp_password} {smtp_port} \n + {wssenddetail}")
         
        loopidx = loopidx + 1

        if loopidx  == targetno :
            print(f"{targetno} emails complete ")  
            wssenddetail = wssenddetail + str(loopidx)  + ",  "   + " " + smtp_username + "=> " + to_addr   + "\n"
            return("發送 " + str(targetno) + "  完成 \n" + wssenddetail)

       
    # 記錄已發送的郵件
        sent_list.append(f"{to_addr},{subject}")
        with open(userFolder.strip('\n') + "_SEND.LOG", "a", encoding="utf-8") as f:
            f.write(f"{loopidx} , {datetime.datetime.now()},  {to_addr},{subject}\n")
            now = datetime.datetime.now()
            wssenddetail = wssenddetail + str(loopidx)  + ",  "  + " " + smtp_username + "=> " + to_addr   + "\n"
 

    # 更新郵件smtp記錄
        with open(userFolder.strip('\n') + "_smtp_send_counter.log", "w", encoding="utf-8") as f:
            f.write(str(smtp_idx))        
    # 更新郵件發送記錄
        counter += 1
        with open(userFolder.strip('\n') +"_mail_counter.log", "w", encoding="utf-8") as f:
            f.write(str(counter))
        
        time.sleep(0.5)

    print(  " return from email \n" + wssenddetail)
    return("郵件發送完成  \n" + wssenddetail)


def loadfile(file_name):
   #可以使用 Python 的 urllib 模組中的 urlretrieve() 函式來下載檔案。以下是一個示範程式碼：
   #ythonCopy code


    url = 'https://mdcgenius.tw/mdcr4ugpt/' + file_name + '.csv'
     
    filename = file_name + '.csv'
    urllib.request.urlretrieve(url, filename)
    print("\n" + filename + "上傳完成")
   #url 是要下載的檔案的 URL，
   # file_name 則是下載後要儲存的檔案名稱和路徑
   # （如果只指定檔案名稱，則預設儲存到目前的資料夾中）。 urlretrieve() 函式會從指定的 URL 下載檔案，並將其儲存在 file_name 指定的位置。   

   #可以使用 Python 的 urllib 模組中的 urlretrieve() 函式來下載檔案。以下是一個示範程式碼：
   #ythonCopy code


    url = 'https://mdcgenius.tw/mdcr4ugpt/' + file_name 
     
    filename = file_name  
    urllib.request.urlretrieve(url, filename)
    print("\n" + filename + "上傳完成")
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
def initcounter()   :
    with open("smtp_send_counter.log", "w", encoding="utf-8") as f:
            f.write(str(0))        
    # 更新郵件發送記錄
    with open("mail_counter.log", "w", encoding="utf-8") as f:
            f.write(str(0))


def check_line_id(ftpurl ,lineid):
     
    url = ftpurl + "authids.txt"
# 讀取文件內容
    file = urllib.request.urlopen(url)
    line = file.readline()
    while line:
        wslineid = line.decode('utf-8').strip('\n')
        xx = wslineid.split("#", 2)
        print("authids - " + xx[0] + "-" + xx[1] + "*")
        if   lineid == xx[0]:
             print("check_line_id return " +xx[1] +"##")
             return(xx[1])  
        line = file.readline()
    print("check_line_id return space")    
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
def check_line_idx(lineid) :
    url = "http://mdcgenius.tw/authids.txt"
     
    wschkfile = check_url_file(url)
    if wschkfile != '' :
        return ("授權記錄檔案 authids.txt not found ") 
     # 讀取文件內容
    file = urllib.request.urlopen(url)
    wauthid = ''
    wauthid  = file.read()
    wauthid  = wauthid.decode('utf-8')     
#    print ( wauthid)


    if  lineid  in wauthid :
#        print('授權成功')
        return ('')
    if  lineid  not in wauthid : 
        print('授權錯誤')
        return ('授權紀錄檔 not found ,請洽 群組館理員')

def test_func(msg):
    wmsg =  "我跟你說一樣的 : " + msg 
    
    return (wmsg )
 
#if __name__ == '__main__':
#    app.run()