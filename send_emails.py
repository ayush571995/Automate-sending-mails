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
<<<<<<< HEAD
        msg['From'] = 'galgotiashackathon@gmail.com'
        msg['To'] = str(i[-1])
        print('successful')
=======
        msg['From'] = 'address_of_sender'
        msg['To'] = str(i[:-1])
        s.sendmail('address_of_sender',str(i[:-1]),msg)
        print('successfully delivered to '+i)
>>>>>>> 84844d2a20019acdcfbb73a9f275143705ad9b5d
    except:
        print('not successfully delivered to '+i)
s.quit()
