import sys
from subprocess import call
import argparse

# get student names from canvas / finger cs machines
# look up student email addresses on student api directory
# add email to list to send to
# send advising bar 

####### HOW TO RUN THIS FILE ###########
# elit3_h4ck -file filename.txt
# elit3_h4ck -n

####################################
# Parse args to determine where to get email addresses
####################################
parser = argparse.ArgumentParser(description="Send email addresses a UT registration phishing attack.")
parser.add_argument('-file', help='use a file')
parser.add_argument('-n', action='store_true', help='find email addresses from finger, canvas, and UT directory')
args = parser.parse_args()
email_list = []

if args.file:
    print("Sending phishing emails to addresses in file ~" + args.file + "~")
    # if a file is being used.....
    file = open(args.file, "r", encoding="utf-8")
    try:
        email_list = file.read().splitlines()
    finally:
        file.close()

if args.n:
    print("Sending phishing emails to addresses found from UTCS finger, Canvas groups, and UT directory")

print(email_list)



####################################
# send email to list of addresses
####################################
#
# Import smtplib for the actual sending function
# import smtplib

# # Import the email modules we'll need
# from email.mime.text import MIMEText

# # Open a plain text file for reading.  For this example, assume that
# # the text file contains only ASCII characters.
# fp = open(textfile, 'rb')
# # Create a text/plain message
# msg = MIMEText(fp.read())
# fp.close()

# # me == the sender's email address
# # you == the recipient's email address
# msg['Subject'] = 'The contents of %s' % textfile
# msg['From'] = me
# msg['To'] = you

# # Send the message via our own SMTP server, but don't include the
# # envelope header.
# s = smtplib.SMTP('localhost')
# s.sendmail(me, [you], msg.as_string())
# s.quit()


#
#####################################
# listener for clicked submit buttons on our fake web server???
####################################
#

#
#####################################
# save/use stolen credentials
####################################
#



