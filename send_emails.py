import smtplib
from email.mime.text import MIMEText
list=open('location of text file ','r').readlines()
s = smtplib.SMTP('smtp.gmail.com', port=587)
s.starttls()
s.login('e-mailid', 'password')
for i in list:
    try:
        msg = MIMEText('hello msg received?')
        msg['Subject'] = 'test_e-mail_sending'
        msg['From'] = 'galgotiashackathon@gmail.com'
        msg['To'] = str(i[-1])
        print('successfully delivered to '+i)
    except:
        print('not successful')
s.quit()