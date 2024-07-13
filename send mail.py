import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
sender ="ab0910342239@gmail.com"
receiver =["s0910342239@gmail","ab0910342239@gmail.com"]
for i in receiver:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = i
    header = Header("Test Send Email","utf-8")
    msg["Subject"] = header.encode()

    body ="This is email sendvfrom python"
    msg.attach(MIMEText(body))
    ssl_context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:
    server.login("ab0910342239@gmail.com","wgqj aena wahy jsgq")
    server.sendmail("ab0910342239@gmail.com","s0910342239@gmail.com,aa0910342239@gmail.com",msg.as_string())
    print("success send email")