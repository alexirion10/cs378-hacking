import sys
from subprocess import call
import argparse

# get student names from canvas / finger cs machines
# look up student email addresses on student api directory
# add email to list to send to
# send advising bar 

# sys.stdout = open('output.txt', 'w')
# call(["ls", "-l"])
# elite_hack -f filename.txt
# elite_hack -n

####################################
# Parse args to determine where to get email addresses
####################################
parser = argparse.ArgumentParser(description="Determine where to find email addresses for phishing attack.")
parser.add_argument('filename', help='use a file')
# parser.add_argument('-n', dest='accumulate', action='store_const', default=max,
#                    help='find email addresses from current local internet')
args = parser.parse_args()
email_list = []

## if a file is being used.....
file = open(args.filename, "r", encoding="utf-8")
try:
    email_list = file.read().splitlines()
finally:
    file.close()


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



