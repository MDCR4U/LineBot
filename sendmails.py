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
 
def send_mail():
    smtp_server = "smtp.office365.com"
    smtp_port = 587


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
 
# 讀取 發送內容
    body_file = 'body.txt'
    if os.path.exists(body_file):
        with open(body_file, 'r', encoding='utf-8') as f:
           content = f.read()
    else:
        print(f'{body_file} does not exist')
        return('找不到信件發送內容')    
 # 讀取 主旨
    subject_file = 'subject.txt'
    if os.path.exists(subject_file):
        with open(subject_file, 'r', encoding='utf-8') as f:
           subject = f.read()
    else:
        print(f'{subject_file} does not exist')
        return('找不到發送主旨')    

    print (subject)
    print(content)  
     

# 開始發送郵件
    for i, row in enumerate(rows):
        if i % batch_size == 0:
            # 切換到下一個發件人賬戶
            smtp_idx = (smtp_idx + 1) % len(smtp_list)
            print(" CHANGE SMTP SLEEP 10   "  )
            time.sleep(5)  # 每發送一批次的郵件等待 10 秒
        smtp_username = smtp_list[smtp_idx][0]
        smtp_password = smtp_list[smtp_idx][1]
 
        
        to_addr = row[0]
       
        cc_addrs = [x for x in row[1:batch_size+1] if x and "@" in x]
        #print(cc_addrs)
        #subject = smtp_username +"臉書優質紛絲團，邀請您 按讚支持"
        content =  "陌生開發優質粉絲團，人員募集中\n歡迎加入\n分享陌開心法及免費工具\n邀起您加入我們 請開啟網址 https://www.facebook.com/profile.php?id=100065188140659 按讚留言 獲取更多的資訊\n www.mydailychoice.com"
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
            time.sleep(3)
            wk_addr="$$$$$"
            server.login(smtp_username,       smtp_password)
            time.sleep(3)

            wk_addr = to_addr 
            #print(f"準備發送第 {i+1} 封郵件 {to_addr}") # {smtp_list[smtp_idx][4]}  {to_addr}")
            
            server.sendmail(smtp_username,  wk_addr  , message.as_string())
             
            server.quit()
            wssendcounter = wssendcounter + 1
        except Exception as e:
            print(f"第 {i+1} 封郵件發送失敗：{e} \n {smtp_username} {smtp_password} {smtp_port} {wk_addr} \n ")
            if 'Authentication unsuccessful' in e:
                wssenddetail = "\n\n  信箱 " + smtp_username + "  可能暫時被封鎖 ，請使用 outlook.com 登入，並依照指示作解鎖\n"
            return(f"第 {i+1} 封郵件發送失敗：{e}  {smtp_username} {smtp_password} {smtp_port} \n + {wssenddetail}")

        if wssendcounter == 10 :
            print(f"第 {i+1} 封郵件發送成功 {smtp_username}  ===>  {to_addr}  ")  
            wssenddetail = wssenddetail + str(i+1)  + ",  " +  now.strftime("%m/%d/%Y, %H:%M:%S")  + " " + smtp_username + "===> " + to_addr   + "\n"
            return("測試發送 10 封 完成 \n" + wssenddetail)
        
    # 記錄已發送的郵件
        sent_list.append(f"{to_addr},{subject}")
        with open("SEND.LOG", "a", encoding="utf-8") as f:
            f.write(f"{i+1} , {datetime.datetime.now()},  {to_addr},{subject}\n")
            now = datetime.datetime.now()
            wssenddetail = wssenddetail + str(i+1)  + ",  " +  now.strftime("%m/%d/%Y, %H:%M:%S")  + " " + smtp_username + "===> " + to_addr   + "\n"
        print(f"第 {i+1} 封郵件發送成功 {smtp_username}  ===>  {to_addr}  ")
    # 更新郵件smtp記錄
        with open("smtp_send_counter.log", "w", encoding="utf-8") as f:
            f.write(str(smtp_idx))        
    # 更新郵件發送記錄
        counter += 1
        with open("mail_counter.log", "w", encoding="utf-8") as f:
            f.write(str(counter))
        #print (" sleep 5 for next send")
        time.sleep(3)

    return("郵件發送完成  \n" + wssenddetail)
def loadfile(file_name):
   #可以使用 Python 的 urllib 模組中的 urlretrieve() 函式來下載檔案。以下是一個示範程式碼：
   #ythonCopy code


    url = 'https://mdcgenius.tw/mdcr4ugpt/' + file_name 
     
    filename = file_name  
    urllib.request.urlretrieve(url, filename)
    print("\n" + filename + "上傳完成")
    return ("\n" + filename + "上傳完成")
 
#if __name__ == '__main__':
#    app.run()