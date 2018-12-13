import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import getpass
ImgFileName='C:\\Users\\Sahaj\\Desktop\\img.jpg'
img_data=open(ImgFileName,'rb').read()
msg=MIMEMultipart()
msg['From']='gargvishu404@gmail.com'
password=getpass.getpass("Enter Your Password: ")
msg['To']=input("Enter gmail of the recipient: ")
msg['cc']=input("Enter gmail of another recipient: ")
rcpt=[msg['cc'],msg['To']]
msg['Subject']=input("Enter Subject: ")
body=input("Enter the body of mail: ")
text=MIMEText(body)
msg.attach(text)
image=MIMEImage(img_data,name=os.path.basename(ImgFileName))
msg.attach(image)
s=smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
s.starttls()
s.login(msg['From'],password)
s.sendmail(msg['From'],rcpt,msg.as_string())
s.quit()
print('Email Sent Succesfully.')