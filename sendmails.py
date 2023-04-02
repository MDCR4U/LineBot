# for upload file
import urllib.request
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
 
def send_mail(lineid,wmsg):
    '/smail'
    wstarget = wmsg[6:]
    if (wstarget.isdigit()):
        targetno = int(wstarget)
        print("要求發送筆數" + str(wstarget))
    else : 
        targetno = 0
        return("發送信件數 錯誤 結束作業")   
    

    print("LINE @ id = " + lineid)
    wssts = check_line_id(lineid)
    if  'not found ' in wssts :
        return (wssts)
     


    #https://github.com/MDCR4U/LineBot/blob/main/mail.csv
    github_id ="MDCR4U"
    github_prj="LineBot"
    githubutl="https://github.com/" + github_id + "/" + github_prj + "blob/main/"
    
    smtp_server = "smtp.office365.com"
    smtp_port = 587

    print("send mail start ")
    with open("smtp.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # 跳過表頭
        smtp_list = [row for row in reader]
    smtp_count = len(smtp_list)   
    
    #wssmtp = ',$'.join(list  for list in smtp_list) 
    #return wssmtp
# 讀取郵件發送記錄
    try:
        with open("mail_counter.log", "r", encoding="utf-8") as f:
            counter = int(f.readline())
    except FileNotFoundError:
        counter = 0
# 讀取SMTP發送記錄
    try:
        with open("smtp_send_counter.log", "r", encoding="utf-8") as f:
            smtp_idx  = int(f.readline())
    except FileNotFoundError:
        smtp_idx  = 0        


# 讀取收件人列表
    with open("mail.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # 跳過表頭
        rows = [row for i, row in enumerate(reader) if i >= counter]
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
    uid = 'mdcr4ugpt'
    url = "http://mdcgenius.tw/" + uid + "/body.txt"
    wschkfile = check_url_file(url)
    if wschkfile != '' :
        return wschkfile
     # 讀取文件內容
    file = urllib.request.urlopen(url)
    content = ''
    wsbody  = file.readline()
    while wsbody:
        content  = content + wsbody.decode('utf-8') 
        wsbody  = file.readline()
    # 關閉 URL
    file.close()
    


#getsubject 

     # 檢查 主旨
     
    url = "http://mdcgenius.tw/" + uid + "/subject.txt"
     
    wschkfile = check_url_file(url)
    if wschkfile != '' :
        return wschkfile
     # 讀取文件內容
    file = urllib.request.urlopen(url)
    wsubject = ''
    wsubject  = file.readline()
    subject = wsubject.decode('utf-8') 
  
    # 關閉 URL
     
   
 
 

# 開始發送郵件
    loopidx = 0
    for j, row in enumerate(rows):
        print ("looping loopidx = " + str(j) + row[0]) 
        if j % batch_size == 0:
            # 切換到下一個發件人賬戶
            smtp_idx = (smtp_idx + 1) % len(smtp_list)
            print("   j = " + str(j )+ " CHANGE SMTP  "  )
            time.sleep(2)  # 每發送一批次的郵件等待 10 秒
        print("   loopidx  = " + str(loopidx )  )    
        smtp_username = smtp_list[smtp_idx][0]
        smtp_password = smtp_list[smtp_idx][1]
 
        
        to_addr = row[0]
       
        cc_addrs = [x for x in row[1:batch_size+1] if x and "@" in x]
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
            time.sleep(1)
            wk_addr="$$$$$"
            server.login(smtp_username,       smtp_password)
            time.sleep(1)

            wk_addr = to_addr 
            #print(f"準備發送第 {i+1} 封郵件 {to_addr}") # {smtp_list[smtp_idx][4]}  {to_addr}")
            
            server.sendmail(smtp_username,  wk_addr  , message.as_string())
             
            server.quit()
            wssendcounter = wssendcounter + 1
        except Exception as e:
            print(f"第 {loopidx } 封郵件發送失敗：{e} \n {smtp_username} {smtp_password} {smtp_port} {wk_addr} \n ")
            if 'Authentication unsuccessful' in e:
                wssenddetail = "\n\n  信箱 " + smtp_username + "  可能暫時被封鎖 ，請使用 outlook.com 登入，並依照指示作解鎖\n"
            return(f"第 {+1} 封郵件發送失敗：{e}  {smtp_username} {smtp_password} {smtp_port} \n + {wssenddetail}")
        print (" loopidx " + str(loopidx) +"  send complete  ")    
        loopidx = loopidx + 1

        if loopidx  == targetno :
            print(f"{targetno} emails complete ")  
            wssenddetail = wssenddetail + str(loopidx)  + ",  "   + " " + smtp_username + "=> " + to_addr   + "\n"
            return("發送 " + targetno + "  完成 \n" + wssenddetail)

       
    # 記錄已發送的郵件
        sent_list.append(f"{to_addr},{subject}")
        with open("SEND.LOG", "a", encoding="utf-8") as f:
            f.write(f"{loopidx} , {datetime.datetime.now()},  {to_addr},{subject}\n")
            now = datetime.datetime.now()
            wssenddetail = wssenddetail + str(loopidx)  + ",  "  + " " + smtp_username + "=> " + to_addr   + "\n"
        
        print(f"第 {j+1} 封郵件發送成功 {smtp_username}  ===>  {to_addr}  ")
    # 更新郵件smtp記錄
        with open("smtp_send_counter.log", "w", encoding="utf-8") as f:
            f.write(str(smtp_idx))        
    # 更新郵件發送記錄
        counter += 1
        with open("mail_counter.log", "w", encoding="utf-8") as f:
            f.write(str(counter))
        print (" j = " + str(j) + " sleep 3 for next send")
        time.sleep(3)

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

def check_line_id(lineid) :
    url = "http://mdcgenius.tw/authids.txt"
     
    wschkfile = check_url_file(url)
    if wschkfile != '' :
        return ("授權記錄檔案 authids.txt not found ") 
     # 讀取文件內容
    file = urllib.request.urlopen(url)
    wauthid = ''
    wauthid  = file.read()
    wauthid  = wauthid.decode('utf-8')     
    print ( wauthid)
    if  lineid  in wauthid :
        print('授權成功')
        return ('')
    if  lineid  not in wauthid : 
        print('授權錯誤')
        return ('授權紀錄檔 not found ,請洽 群組館理員')

       
#if __name__ == '__main__':
#    app.run()