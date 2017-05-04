#### A file simply for testing ####

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

email_list = ['alexirion10@gmail.com', 'kdrewniak@utexas.edu', 'DARKTONY13@GMAIL.COM']

msg = MIMEMultipart()
msg['Subject'] = 'Get Phished Round 2!!'
msg['From'] = 'someoneelse@gmail.com'

phish_mail = open('phishing_email.txt', 'rb')
msg.attach(MIMEText(phish_mail.read()))
phish_mail.close()


fromaddr = 'alexirion10@gmail.com'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('alexirion10@gmail.com', 'password here')

for target in email_list:
    msg['To'] = target
    server.sendmail('someoneelse@gmail.com', target, msg.as_string())

server.quit()
