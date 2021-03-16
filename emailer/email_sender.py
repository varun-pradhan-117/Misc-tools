import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html=Template(Path("mail.html").read_text())
email=EmailMessage()
email['from']='<sender name>'
email['to']='<recipient>'
email['subject']='You won 5 Million Dollars'

email.set_content(html.substitute({'name':'Miyamura'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('<sender mail>','<app password>')
    smtp.send_message(email)
    print("This works")
    