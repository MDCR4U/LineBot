import csv
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 設置發件人的賬戶信息
username = "tt6395b@outlook.com" 
#username = "pq7419a@outlook.com"
password = "bqm2151#"
smtp_server = "smtp.office365.com"
smtp_port = 587

# 讀取收件人列表

receiver = "buddhisty@gmail.com" #"tt6395b@outlook.com" 
subject = "臉書優質紛絲團，邀請您 按讚支持" 
content =  "陌生開發優質粉絲團，人員募集中\n歡迎加入\n分享陌開心法及免費工具\n邀起您加入我們 請開啟網址 https://www.facebook.com/profile.php?id=100065188140659 按讚留言 獲取更多的資訊\n www.mydailychoice.com"
   
        # 設置郵件內容
username = input("user name : ")
message = MIMEMultipart()
message["From"] = "Facebook <" +  username + ">"
message["To"] =  receiver 
message["Subject"] = subject + username

message.attach(MIMEText(content, "plain"))
        # 添加附件
#filename = "attachment.pdf"
#with open(filename, "rb") as attachment:
#    part = MIMEApplication(attachment.read(), Name=filename)
#    part["Content-Disposition"] = f'attachment; filename="{filename}"'
#    message.attach(part)
        # 發送郵件
try:
     
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    print (username +"-" + password + "-" + smtp_server  + "-" + str(smtp_port))
    smtp.login(username, password)
    print("smtp sendmail")
    smtp.sendmail(username, [receiver], message.as_string())
    smtp.quit()
    print(f"郵件已發送至 {receiver}")
except Exception as e:
            print(f"郵件發送失敗：{e}")