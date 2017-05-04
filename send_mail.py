#### A file simply for testing ####

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

email_list = ['alexirion10@gmail.com', 'alexirion10@utexas.edu', 'alex.irion@ciraconnect.com', 'kdrewniak@utexas.edu', 'DARKTONY13@GMAIL.COM']

msg = MIMEMultipart()
msg['Subject'] = 'Get Phished!'
msg['From'] = 'someoneelse@gmail.com'

body = 'A very bad link here!\n\nThe emails are ready to go...\ncreate a message for me to send Tony/Kry'
msg.attach(MIMEText(body, 'plain'))

fromaddr = 'alexirion10@gmail.com'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('alexirion10@gmail.com', 'Chargers101')

for target in email_list:
    msg['To'] = target
    server.sendmail('someoneelse@gmail.com', target, msg.as_string())

server.quit()
