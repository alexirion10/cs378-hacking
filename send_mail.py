#### A file simply for testing ####

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

email_list = ['alexirion10@gmail.com', 'kdrewniak@utexas.edu', 'DARKTONY13@GMAIL.COM']

msg = MIMEMultipart()
msg['Subject'] = 'Get Phished Round 2!!'
msg['From'] = 'san@utexas.edu'

phish_mail = open('phishing_email.txt', 'rb')
msg.attach(MIMEText(phish_mail.read()))
phish_mail.close()

server = smtplib.SMTP('smtp.hushmail.com', 587)
server.starttls()
server.login('eth_hack@hushmail.com', 'hacker1234')
for target in email_list:
    msg['To'] = target
    server.sendmail('eth_hack@hushmail.com', target, msg.as_string())

server.quit()
