#!/usr/bin/python
import os, re
import sys
import smtplib
 
#from email.mime.image import MIMEImage
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.MIMEText import MIMEText

 
SMTP_SERVER = 'smtpserver'
SMTP_PORT = 25

 
sender = 'ipam@localhost'
recipient = sys.argv[1]
subject = sys.argv[2]
message = sys.argv[3]
nicefilename = sys.argv[5]
 
def main():
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['To'] = recipient
    msg['From'] = sender
    
    
    part = MIMEText('text', "plain")
    part.set_payload(message)
    msg.attach(part)
    
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
 
    session.ehlo()

    fp = open(sys.argv[4], 'rb')
    msgq = MIMEBase('audio', 'audio')
    msgq.set_payload(fp.read())
    fp.close()
    # Encode the payload using Base64
    encoders.encode_base64(msgq)
    # Set the filename parameter
    msgq.add_header('Content-Disposition', 'attachment', filename=nicefilename)
    msg.attach(msgq)
    # Now send or store the message
    qwertyuiop = msg.as_string()



    session.sendmail(sender, recipient, qwertyuiop)
    
    session.quit()
 
if __name__ == '__main__':
    main()
