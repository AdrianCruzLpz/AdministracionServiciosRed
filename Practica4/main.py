from telnetlib import Telnet
import time

def telnetRCP1(HOST):
    with Telnet(HOST, 23) as tn:
        user = "rcp"
        password = "rcp"
        
        tn.read_until(b'User: ', float(10))
         
        tn.write(user.encode("ascii") + b'\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.read_until(b'Password: ', float(10))
        tn.write(password.encode("ascii") + b'\n')
        print(tn.read_eager().decode('ascii'))
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'en\n')
         
        print(tn.read_eager().decode('ascii') + "-----")
        tn.write(b'config\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'service ftp\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'copy running-config startup-config\n')
         
        print(tn.read_eager().decode('ascii') + "-----")
        
        

def telnetRCP2(HOST, HOST2):
    with Telnet("30.30.30.1", 23) as tn:
        user = "rcp"
        password = "rcp"
        
        tn.read_until(b'User: ', float(10))
         
        tn.write(user.encode("ascii") + b'\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.read_until(b'Password: ', float(10))
        tn.write(password.encode("ascii") + b'\n')
        print(tn.read_eager().decode('ascii'))
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'en\n')
         
        print(tn.read_eager().decode('ascii') + "-----")
        tn.write(b'config\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'telnet 192.168.1.2\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.read_until(b'User: ', float(10))
         
        tn.write(user.encode("ascii") + b'\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.read_until(b'Password: ', float(10))
        tn.write(password.encode("ascii") + b'\n')
        print(tn.read_eager().decode('ascii'))
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'en\n')
         
        print(tn.read_eager().decode('ascii') + "-----")
        tn.write(b'config\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'service ftp\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'copy running-config startup-config\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

def EnviarTelnetFtp(HOST, HOST2, fileName, newFileName):
    with Telnet("30.30.30.1", 23) as tn:
        user = "rcp"
        password = "rcp"
        
        tn.read_until(b'User: ', float(10))
         
        tn.write(user.encode("ascii") + b'\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.read_until(b'Password: ', float(10))
        tn.write(password.encode("ascii") + b'\n')
        print(tn.read_eager().decode('ascii'))
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'en\n')
         
        print(tn.read_eager().decode('ascii') + "-----")
        tn.write(b'config\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'service ftp\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'telnet 192.168.1.2\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.read_until(b'User: ', float(10))
         
        tn.write(user.encode("ascii") + b'\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.read_until(b'Password: ', float(10))
        tn.write(password.encode("ascii") + b'\n')
        print(tn.read_eager().decode('ascii'))
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'en\n')
         
        print(tn.read_eager().decode('ascii') + "-----")
        tn.write(b'config\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'service ftp\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'exit\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'exit\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'copy ' + newFileName.encode("ascii") + b' ftp://rcp:rcp@192.168.1.2/' + newFileName.encode("ascii") + b'\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

def DescargarTelnetFtp(HOST, HOST2, fileName, newFileName):
    with Telnet("30.30.30.1", 23) as tn:
        user = "rcp"
        password = "rcp"
        
        tn.read_until(b'User: ', float(10))
         
        tn.write(user.encode("ascii") + b'\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.read_until(b'Password: ', float(10))
        tn.write(password.encode("ascii") + b'\n')
        print(tn.read_eager().decode('ascii'))
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'en\n')
         
        print(tn.read_eager().decode('ascii') + "-----")
        tn.write(b'config\n')
         
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'service ftp\n')
        time.sleep(5) 
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'telnet 192.168.1.2\n')
        time.sleep(5) 
        print(tn.read_eager().decode('ascii') + "-----")

        tn.read_until(b'User: ', float(10))
        time.sleep(5)
        tn.write(user.encode("ascii") + b'\n')
        time.sleep(5)
        print(tn.read_eager().decode('ascii') + "-----")

        tn.read_until(b'Password: ', float(10))
        tn.write(password.encode("ascii") + b'\n')
        print(tn.read_eager().decode('ascii'))
        
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'en\n')
         
        print(tn.read_eager().decode('ascii') + "-----")
        tn.write(b'config\n')
        time.sleep(5) 
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'service ftp\n')
        time.sleep(5)
        print(tn.read_eager().decode('ascii') + "-----")

        tn.write(b'copy ' + fileName.encode("ascii") + b' ftp://rcp:rcp@30.30.30.1/' + newFileName.encode("ascii") + b'\n')
        time.sleep(5)
        print(tn.read_eager().decode('ascii') + "-----")