import sys
import argparse                    #parsing command line args
from bs4 import BeautifulSoup      #webscraping
from subprocess import call
import requests
import json
import httplib

####### HOW TO RUN THIS FILE ###########
# elit3_h4ck -file filename.txt         #uses email addresses already in text file
# elit3_h4ck -n                         #pulls email addresses from canvas

# get student names from canvas / finger cs machines
# look up student email addresses on student api directory
# add email to list to send to
# send advising bar 

COURSE_ID = 1195393
ACCESS_TOKEN = 'ask alex.  This is private'

def call(path, request_type='GET', data=None):
    connection = httplib.HTTPSConnection("utexas.instructure.com")
    headers = {"Content-type": "application/json", "Authorization": "Bearer " + ACCESS_TOKEN}

    json_data = json.dumps(data) if data is not None else ""
    connection.request(request_type, "/api/v1/" + path, json_data, headers)
    response = connection.getresponse()
    s = response.read().decode()
    return json.loads(s)

def get_student_names(cur_course_id):
    #returns a list of up to 100 student names and emails given a course ID
    return call("courses/{}/users?per_page=100&include[]=email".format(cur_course_id))


def find_canvas_student_names():
    student_names = []
    student_names.append('hello world')
    student_names.append('alex irion')
    student_names.append('tony sampson')
    return student_names

def ut_directory_lookup(student_names):
    my_user_names = get_student_names(COURSE_ID)
    for name in my_user_names:
        print(name['name'] + '        ' + name['email'])

    # GET request to UT directory, webscrape for email address
    for name in student_names:
        name_array = name.split()
        request_url = 'https://directory.utexas.edu/index.php?q=' # Set destination URL here
        request_url += name_array[0] + '+' + name_array[1]
        request_url += '&scope=all&submit=Search'
        print(request_url)

        # page = requests.get(request_url)
        # soup = BeautifulSoup(page.content, "html.parser")

        # table = soup.find_all('table', class_='dir_info')
        # for row in table:
        #     cells = row.find_all('tr')
        #     for tr in cells:
        #         tds = tr.find_all('td')
        #         if 'Email:' in str(tds[0].text):
        #             email_list.append( str(tds[1].text)[1:-1] )


####################################
# Parse args to determine where to get email addresses
####################################
parser = argparse.ArgumentParser(description="Send email addresses a UT registration phishing attack.")
parser.add_argument('-file', help='use a file')
parser.add_argument('-n', action='store_true', help='find email addresses from finger, canvas, and UT directory')
args = parser.parse_args()
email_list = []

if args.file:
    #gets email addresses from a text file
    print("Sending phishing emails to addresses in file ~" + args.file + "~")
    file = open(args.file, "r", encoding="utf-8")
    try:
        email_list = file.read().splitlines()
    finally:
        file.close()

if args.n:
    print("Sending phishing emails to addresses found from UTCS finger, Canvas groups, and UT directory")
    # run finger on UTCS machines
    # find student names from canvas api
    student_names = find_canvas_student_names()
    #find student email address from student name
    ut_directory_lookup(student_names)


####################################
# send email to list of addresses
####################################



#####################################
# listener for clicked submit buttons on our fake web server???
####################################
# call(['python3', 'evil_server.py'])


#####################################
# save/use stolen credentials
####################################
#



