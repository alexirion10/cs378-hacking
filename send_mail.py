## email tester
#
# Import smtplib for the actual sending function
# import smtplib

# # Import the email modules we'll need
# from email.mime.text import MIMEText

# # Open a plain text file for reading.  For this example, assume that
# # the text file contains only ASCII characters.
# # fp = open(textfile, 'rb')
# # Create a text/plain message
# msg = MIMEText('some email body stuff here')
# # fp.close()

# # me == the sender's email address
# # you == the recipient's email address
# msg['Subject'] = 'some contents...'
# msg['From'] = 'alexirion10@utexas.edu'
# msg['To'] = 'alexirion10@gmail.com'

# # Send the message via our own SMTP server, but don't include the
# # envelope header.
# s = smtplib.SMTP('localhost')
# s.sendmail(me, [you], msg.as_string()
# s.quit()
# 
## ///////////////////////////////////////////
import requests
#connect to canvas api to get student names in courses
# access_token = '1017~DSH05LRqWUsyMocT6hCsMHNuX2gA6Yl6NJlt0Zwnsde0uj9xC8bT66YhlmSgva6g'
# #1017~DSH05LRqWUsyMocT6hCsMHNuX2gA6Yl6NJlt0Zwnsde0uj9xC8bT66YhlmSgva6g
# canvas_request = 'https://canvas.instructure.com/api/v1/courses?q=enrollment_state=active&access_token=' + access_token
# r = requests.get(canvas_request)
# something = r.json()
# for line in something:
#     print(line)



### ///////////////////////////////////////////
student_names = ['alex irion', 'tony sampson', 'wes draper', 'sam langner', 'chad baldwin']  
student_emails = []

from bs4 import BeautifulSoup

for name in student_names:
    name_array = name.split()
    request_url = 'https://directory.utexas.edu/index.php?q=' # Set destination URL here
    request_url += name_array[0] + '+' + name_array[1]
    request_url += '&scope=all&submit=Search'
    #print(request_url)

    page = requests.get(request_url)
    soup = BeautifulSoup(page.content, "html.parser")
    print(soup.prettify())

    table = soup.find_all('table', class_='dir_info')

    for row in table:
        cells = row.find_all('tr')
        for tr in cells:
            tds = tr.find_all('td')
            if 'Email:' in str(tds[0].text):
                student_emails.append( str(tds[1].text) )


print(student_emails)




