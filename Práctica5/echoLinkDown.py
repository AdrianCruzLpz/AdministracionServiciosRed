import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mailsender = "acruzlopez071@gmail.com"
mailreceip = "cruzadrian342@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'sebluawkyexssqyh'

msg = MIMEMultipart()
msg['Subject'] = "Alerta LinkDown"
msg['From'] = mailsender
msg['To'] = mailreceip

fichero = open('echoLinkDown.txt')
Dispositivo = fichero.read()

msg.attach(MIMEText('SE HA DETECTADO UNA ALERTA LINKDOWN\n\nDISPOSITIVO: DESKTOP-H83CUKU\nCONTACTO: adrianlopez-cruz@ouruz@outlook.com\nUBICACION: Laboratorio de Redes - ESCOM IPN\n\n\n', 'plain'))
msg.attach(MIMEText(Dispositivo, 'plain'))
s = smtplib.SMTP(mailserver)

s.starttls()
# Login Credentials for sending the mail
s.login(mailsender, password)