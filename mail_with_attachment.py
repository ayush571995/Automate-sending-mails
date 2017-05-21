import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
fromaddr = "your mail address"
list=open('list containing mail ids ','r').readlines()
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['Subject'] = "Subject of the Mail"
body = "Body_of_the_mail"
msg.attach(MIMEText(body, 'plain'))
list_for_attachment=['']#absolute path without extension
for k in list_for_attachment:
    filename=k.split('/').pop()
    attachment = open(k,"rb")
    p = MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "password")
for i in list:
    try:
        msg['To']=str(i[:-1])
        text = msg.as_string()
        s.sendmail(fromaddr,str(i[:-1]),text)
        print('successfully sent to '+str(i[:-1]))
    except:
        print('unable to send to '+str(i[:-1]))
s.quit()
