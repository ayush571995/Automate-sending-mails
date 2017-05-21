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
        msg['From'] = 'address_of_sender'
        msg['To'] = str(i[:-1])
        s.sendmail('address_of_sender',str(i[:-1]),msg)
        print('successfully delivered to '+i)
    except:
        print('not successfully delivered to '+i)
s.quit()
