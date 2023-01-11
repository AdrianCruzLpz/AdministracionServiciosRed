from ftplib import FTP
from main import EnviarTelnetFtp, DescargarTelnetFtp

user = "rcp"
password = "rcp"

def enviarFTP():
    print("IP del router al que se enviara el archivo")
    host = input()

    print(" Desea generar el archivo de configuración de otro router?")
    opc = input()

    if(opc == "n"):
        print("Nombre del archivo a enviar")
        filename = input()
        print("Nuevo nombre del archivo")
        newFileName = input()

        ftp = FTP(host)
        ftp.login(user = user, passwd = password)
        print(ftp.getwelcome())
        f = open(filename, "rb")
        ftp.storbinary("STOR " + newFileName, f)
        ftp.quit()
    
    else:
        print("IP del siguiente router")
        ipAux = input()
        print("Nombre del archivo a enviar")
        filename = input()
        print("Nuevo nombre del archivo")
        newFileName = input()

        ftp = FTP(host)
        ftp.login(user = user, passwd = password)
        print(ftp.getwelcome())
        f = open(filename, "rb")
        ftp.storbinary("STOR " + newFileName, f)
        ftp.quit()

        EnviarTelnetFtp(host, ipAux, filename, newFileName)


def descargarFTP():
    print("IP del router del que desea recibir el archivo")
    host = input()

    print("Desea descargar el archivo de configuración de otro router? S/N")
    opc = input()

    if(opc == "n"):
        print("Nombre del archivo a descargar")
        filename = input()
        print("Nuevo nombre del archivo")
        newFileName = input()

        ftp = FTP(host)
        ftp.login(user = user, passwd = password)
        print(ftp.getwelcome())
        f = open(newFileName, "wb")
        ftp.retrbinary("RETR " + filename, f.write, 1024)
        ftp.quit()
    
    else:
        print(" IP del siguiente router")
        ipAux = input()
        print("Nombre del archivo a descargar")
        filename = input()
        print("Nuevo nombre del archivo")
        newFileName = input()

        DescargarTelnetFtp(host, ipAux, filename, newFileName)

        ftp = FTP(host)
        ftp.login(user = user, passwd = password)
        print(ftp.getwelcome())
        f = open(newFileName, "wb")
        ftp.retrbinary("RETR " + newFileName, f.write, 1024)
        ftp.quit()