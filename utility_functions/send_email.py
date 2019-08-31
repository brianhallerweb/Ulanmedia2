from ulanmedia2_config.config import *
import smtplib

def send_email(to, subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login("brianshallerdev@gmail.com", brianshallerdev_password)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail('brianshallerdev@gmail.com', to, message)
        server.quit()
        print("email sent")
    except:
        print("email did not send - there was a problem with send_email()")
        
