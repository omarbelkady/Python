import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
gmailaddr=input("What is your gmail address?:\n")
gmailpswd=input("What is the password for the email address?:\n")
mailto=input("What email address do you want to send your message to?:\n")
msg= input("What is your message?:\n")
mServer=smtplib.SMTP('smtp.gmail.com', 587)
mServer.ehlo()
'''
MORE SAFER WAY TO DO IT IS THIS by placing your email password in text file:
with open('password.txt','r') as f:
    password = f.read()
'''


mServer.starttls()
#How to login to your mail Server
mServer.login(gmailaddr,gmailpswd)
mServer.sendmail(gmailaddr, mailto,msg)
print(" \n Message Sent Successfully!")
mServer.quit()

#PART II
msg = MIMEMultipart()
msg['From']='Omar'
msg['To']='alanngo673@gmail.com'
msg['Subject']= 'C-Lover'
with open('message.txt','r') as f:
    message=f.read()

msg.attach(MIMEText(message,'plain'))


