import smtplib
from email.mime.text import MIMEText
list=open('/home/ayush/Desktop/list_of_emails','r').readlines()
s = smtplib.SMTP('smtp.gmail.com', port=587)
s.starttls()
s.login('galgotiashackathon@gmail.com', 'gcetloop')
for i in list:
    try:
        msg = MIMEText('hello msg received?')
        msg['Subject'] = 'test_e-mail_sending'
        msg['From'] = 'galgotiashackathon@gmail.com'
        msg['To'] = str(i[-1])
        print('successful')
    except:
        print('not successful')
s.quit()