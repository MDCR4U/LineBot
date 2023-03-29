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
import datetime
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_mail():
    url = 'https://mdcgenius.tw/smtp.csv'
    file_name = 'smtp.csv'
    urllib.request.urlretrieve(url, file_name)
    print ("Get smtp complete")

    file_path = "smtp.csv"

    if os.path.isfile(file_path):
        return ("檔案存在。")
    else:
        return ("檔案不存在。")
    
# 讀取寄件者資訊
    with open("SMTP.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # 跳過表頭
        smtp_list = [row for row in reader]
    smtp_count = len(smtp_list)    

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
    smtp_server = smtp_list[smtp_idx][2]
    smtp_port = smtp_list[smtp_idx][3]

# 設置發送成功的郵件地址和主旨的列表
    sent_list = []

# 每個批次的大小
    batch_size = 3
#  初始化 發送紀錄數
   
    wssendcounter = 0
    wssenddetail = ""

# 開始發送郵件
    for i, row in enumerate(rows):
        if i % batch_size == 0:
            # 切換到下一個發件人賬戶
            smtp_idx = (smtp_idx + 1) % len(smtp_list)
            smtp_username = smtp_list[smtp_idx][0]
            #smtp_username = "jry_yeh@hotmail.com"
            smtp_password = smtp_list[smtp_idx][1]
            smtp_server = smtp_list[smtp_idx][2]
            smtp_port = smtp_list[smtp_idx][3]
            print(" CHANGE SMTP SLEEP 20   " + smtp_idx + " " + smtp_username)
            time.sleep(20)  # 每發送一批次的郵件等待 10 秒
        to_addr = row[0]
        print("to:" + to_addr)

        cc_addrs = [x for x in row[1:batch_size+1] if x and "@" in x]
        #print(cc_addrs)
        subject = "臉書優質紛絲團，邀請您 按讚支持"
        content = "收件者 " + to_addr + " ==> buddhisty@gmail.com , 寄件者 ==>" + smtp_list[smtp_idx][4] + " " + smtp_list[smtp_idx][0]+ "\n www.mydailychoice.com"
    # 準備發送郵件
        message = MIMEMultipart()
        #message["From"] = smtp_list
        message["From"] =    f"{smtp_list[smtp_idx][4]} <{smtp_username}>" #smtp_list[smtp_idx][4]  # 寄件者姓名
               
        message["To"] = to_addr #"buddhisty@gmail.com"
    
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
            print("smtp_username=" + smtp_username)
            server.login(smtp_username, smtp_password)
            print("start send mail")

            wk_addr = to_addr #"buddhisty@gmail.com" #to_addr
            print(f"準備發送第 {i+1} 封郵件 {to_addr}") # {smtp_list[smtp_idx][4]}  {to_addr}")
            
            server.sendmail(smtp_username,  wk_addr  , message.as_string())
             
            print ("send complete")
            server.quit()
            wssendcounter = wssendcounter + 1
        except Exception as e:
            print(f"第 {i+1} 封郵件發送失敗：{e}")
            return(f"第 {i+1} 封郵件發送失敗：{e}  \n + {wssenddetail}")

        if wssendcounter == 5:    
            return("測試發送五封 完成 \n" + wssenddetail)
        
    # 記錄已發送的郵件
        sent_list.append(f"{to_addr},{subject}")
        with open("SEND.LOG", "a", encoding="utf-8") as f:
            f.write(f"{i+1} , {datetime.datetime.now()},  {to_addr},{subject}\n")
            wssenddetail = wssenddetail + str(i+1)  + ",  " + datetime.datetime.now() + " " + to_addr  
        print(f"第 {i+1} 封郵件發送成功")
    # 更新郵件smtp記錄
        with open("smtp_send_counter.log", "w", encoding="utf-8") as f:
            f.write(str(smtp_idx))        
    # 更新郵件發送記錄
        counter += 1
        with open("mail_counter.log", "w", encoding="utf-8") as f:
            f.write(str(counter))
        print (" sleep 10 for next send")
        time.sleep(10)

    return("send mil complete   \n" + wssenddetail)
#def loadfile():
   #可以使用 Python 的 urllib 模組中的 urlretrieve() 函式來下載檔案。以下是一個示範程式碼：
   #ythonCopy code


#   url = 'https://www.example.com/example_file.txt'
#   file_name = 'example_file.txt'

#   urllib.request.urlretrieve(url, file_name)
   #url 是要下載的檔案的 URL，
   # file_name 則是下載後要儲存的檔案名稱和路徑
   # （如果只指定檔案名稱，則預設儲存到目前的資料夾中）。 urlretrieve() 函式會從指定的 URL 下載檔案，並將其儲存在 file_name 指定的位置。   

#if __name__ == '__main__':
#    app.run()