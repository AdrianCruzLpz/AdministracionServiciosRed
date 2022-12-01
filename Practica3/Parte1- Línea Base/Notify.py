import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getSNMP import consultaSNMP

datos = ['localhost']

indice_ip = 0
comunidad = 'comunidadASR'

info = ['1.3.6.1.2.1.1.5.0', '1.3.6.1.2.1.1.4.0', '1.3.6.1.2.1.1.6.0']

name_user = consultaSNMP(comunidad,datos[indice_ip],info[0])
    # print(name_user)
contact = consultaSNMP(comunidad,datos[indice_ip],info[1])
    # print(system)
ubication = consultaSNMP(comunidad,datos[indice_ip],info[2])
    # print(ubication)

message = "name_user: " + name_user + "\n\n" + "contact: " + contact + "\n\n" + "ubication: " + ubication + "\n"
COMMASPACE = ', '
# Define params
rrdpath = '../RRD/'
imgpath = '../IMG/'
fname = 'trend.rrd'

mailsender = "acruzlopez071@gmail.com"
mailreceip = "cruzadrian342@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'sebluawkyexssqyh'

def send_alert_attached(subject):
    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
  
    fp = open(imgpath+'deteccionProcesador.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    
    msg.attach(MIMEText(message,'plain'))
    msg.attach(img)
    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()