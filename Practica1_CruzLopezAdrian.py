"""
SNMPv1
++++++
Send SNMP GET request using the following options:
  * with SNMPv1, community 'comunidadASR'
  * over IPv4/UDP
  * to an Agent at localhost
  * for two instances of SNMPv2-MIB::sysDescr.0 MIB object,
Functionally similar to:
| $ snmpget -v1 -c comunidadASR localhost 1.3.6.1.2.1.1.1.0
"""#
import os

from pysnmp.hlapi import *
import datetime

def consultaOID(comunidad,ip,OID):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(comunidad, mpModel=0),
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(OID))
        )
    return iterator

def imprimirRespuesta(iterator):

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
            return varBinds


### --- FUNCION PARA CREAR AGENTES --- ###

def createAgent():
    print("*** Datos del agente a agregar ***\n")
    ipAgent = input("Direccion IP: ")
    port = input("Puerto: ")
    community = input("Comunidad: ")
    version = input("Version: ")

    f = open('./agentes.txt', 'a')
    f.write(ipAgent)
    f.write('\n')
    f.write(port)
    f.write('\n')
    f.write(community)
    f.write('\n')
    f.write(version)
    f.write('\n\n')
    f.close()

### --- FUNCION PARA MODIFICAR AGENTES --- ###

def updateAgent():
    datos_agente = []
    ipToUpdate = input("Direccion IP del agente a modificar: ")

    with open("agentes.txt") as archivo:
        for lineas in archivo:
            datos_agente.extend(lineas.split())

    posicion = datos_agente.index(ipToUpdate)
    aux = int(posicion/4)
    portLine = posicion + aux + 1
    communityLine = posicion + aux + 2
    versionLine = posicion + aux + 3


    ### --- DIRECCION IP --- ###

    newIp = input("Nueva direccion IP: ")

    with open("agentes.txt", "rt") as file:
        x = file.read()

    with open("agentes.txt", "wt") as file:
        x = x.replace(ipToUpdate, newIp)
        file.write(x)

    ### --- PUERTO --- ###

    newPort = input("Nueva puerto: ")
    with open('agentes.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    data[portLine] = newPort + '\n'
    with open('agentes.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)

    ### --- COMUNIDAD --- ###

    newCommunity = input("Nueva comunidad: ")
    with open('agentes.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    data[communityLine] = newCommunity + '\n'
    with open('agentes.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)

    ### --- VERSION --- ###

    newVersion = input("Nueva version: ")
    with open('agentes.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()

    data[versionLine] = newVersion + '\n'
    with open('agentes.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)


### --- FUNCION PARA ELIMINAR AGENTES --- ###

def deleteAgent():
    datos_agente = []
    print('Direccion IP del agente a eliminar')
    ipToDelete = input()

    with open("agentes.txt") as archivo:
        for lineas in archivo:
            datos_agente.extend(lineas.split())

    posicion = datos_agente.index(ipToDelete)
    aux = int(posicion/4)
    print(aux)
    ipPosition = posicion + aux
    portLine = posicion + aux + 1
    communityLine = posicion + aux + 2
    versionLine = posicion + aux + 3
    jumpLine = posicion + aux + 4

    with open('agentes.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    data[ipPosition] = ''
    data[portLine] = ''
    data[communityLine] = ''
    data[versionLine] = ''
    data[jumpLine] = ''
    with open('agentes.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)


### --- FUNCION PARA CREAR EL REPORTE DE UN AGENTE --- ###

def createReport():
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    

    print('Direccion IP del agente a generar reporte')
    ipAgentReport = input()

    w, h = letter
    c = canvas.Canvas("ReportAgent_{}.pdf".format(ipAgentReport), pagesize=letter)
    
    datos = []
    ip = []
    comunidad = []

    with open('agentes.txt') as archivo:
        for lineas in archivo:
            datos.extend(lineas.split())

    numero_agentes = int(len(datos)/3)
    interlineado = 70

    indice_ip = datos.index(ipAgentReport)
    comunidad = datos[indice_ip + 2]

    c.drawString(200, h - interlineado, "Administración de Servicios en Red")
    c.drawString(200, h - (interlineado+20), "Práctica 1")
    c.drawString(200, h - (interlineado+40), "Adquisión de información utilizando SNMP")
    c.drawString(200, h - (interlineado+60), "Cruz López Adrián  Grupo: 4CM13")

    c.drawString(100, h - (interlineado+100), "Información del agente")
    sysDescr = str(imprimirRespuesta(consultaOID(comunidad, datos[indice_ip], "1.3.6.1.2.1.1.1.0"))[0])
    sysOpWin = 'Windows'
    sysOpLin = 'Linux'

    if sysOpWin in sysDescr:
        c.drawString(50, h - (interlineado+120), "Sistema: " + sysOpWin)

    else:
        c.drawString(50, h - (interlineado+120), "Sistema: " + sysOpLin)

    sysName = str(imprimirRespuesta(consultaOID(comunidad, datos[indice_ip], "1.3.6.1.2.1.1.5.0"))[0])
    sysNameSplit = sysName.split('=')

    sysContact = str(imprimirRespuesta(consultaOID(comunidad, datos[indice_ip], "1.3.6.1.2.1.1.4.0"))[0])
    sysContactSplit = sysContact.split('=')

    sysLocation = str(imprimirRespuesta(consultaOID(comunidad, datos[indice_ip], "1.3.6.1.2.1.1.6.0"))[0])
    sysLocationSplit = sysLocation.split('=')

    ifNumberInterfaces = str(imprimirRespuesta(consultaOID(comunidad, datos[indice_ip], "1.3.6.1.2.1.2.1.0"))[0])
    numberInterfaceSplit = ifNumberInterfaces.split('=')

    numberInterfaces = int(numberInterfaceSplit[1])

    c.drawString(50, h - (interlineado+140), "Nombre: " + sysNameSplit[1])
    c.drawString(50, h - (interlineado+160), "Contacto: " + sysContactSplit[1])
    c.drawString(50, h - (interlineado+180), "Ubicación: " + sysLocationSplit[1])
    c.drawString(50, h - (interlineado+200), "Número de interfaces: " + numberInterfaceSplit[1])

    c.drawString(80, h - (interlineado+230), "Descripción y estatus de cada interface")
    aux = 0

    sysDescr = str(imprimirRespuesta(consultaOID(comunidad, datos[indice_ip], "1.3.6.1.2.1.1.1.0"))[0])
    sysOpWin = 'Windows'
    sysOpLin = 'Linux'

    if sysOpWin in sysDescr:
        for i in range(numberInterfaces):
            oidDesc = str(imprimirRespuesta(consultaOID(comunidad, datos[indice_ip], "1.3.6.1.2.1.2.2.1.2." + str(i + 1)))[0])
            oidDesc_split = oidDesc.split('=')

            oidStatus = str(imprimirRespuesta(consultaOID(comunidad, datos[indice_ip], "1.3.6.1.2.1.2.2.1.8." + str(i + 1)))[0])
            

            oidStatus_split = oidStatus.split('= ')

            int_hex_split = oidDesc_split[1].split('0x')
            byte_array = bytearray.fromhex(int_hex_split[1])
            int_hex = byte_array.decode()

            espacios = interlineado + 250 + (aux*20)

            if (str(oidStatus_split[1]) == "1"):
                text = c.beginText(50, h - espacios)
                text.setFont("Times-Roman", 12)
                text.textLines(str(int_hex) + " === UP")
                c.drawText(text)
                aux += 1

            elif (str(oidStatus_split[1]) == "2"):
                text = c.beginText(50, h - espacios)
                text.setFont("Times-Roman", 12)
                text.textLines(str(int_hex) + " === DOWN")
                c.drawText(text)
                aux += 1
            else:
                text = c.beginText(50, h - espacios)
                text.setFont("Times-Roman", 12)
                text.textLines(str(int_hex) + " === TESTING")
                c.drawText(text)
                aux += 1

    else:
        for i in range(numberInterfaces):
            oidDesc = str(imprimirRespuesta(consultaOID(comunidad, datos[indice_ip], "1.3.6.1.2.1.2.2.1.2." + str(i + 1)))[0])
            oidDesc_split = oidDesc.split('=')

            oidStatus = str(imprimirRespuesta(consultaOID(comunidad, datos[indice_ip], "1.3.6.1.2.1.2.2.1.8." + str(i + 1)))[0])
            
            oidStatus_split = oidStatus.split('= ')

            espacios = interlineado + 250 + (aux*20)

            if (str(oidStatus_split[1]) == "1"):
                text = c.beginText(50, h - espacios)
                text.setFont("Times-Roman", 12)
                text.textLines(str(oidDesc_split[1]) + " === UP")
                c.drawText(text)
                aux += 1

            elif (str(oidStatus_split[1]) == "2"):
                text = c.beginText(50, h - espacios)
                text.setFont("Times-Roman", 12)
                text.textLines(str(oidDesc_split[1]) + " === DOWN")
                c.drawText(text)
                aux += 1
            else:
                text = c.beginText(50, h - espacios)
                text.setFont("Times-Roman", 12)
                text.textLines(str(oidDesc_split[1]) + " === TESTING")
                c.drawText(text)
                aux += 1

        if espacios % 710 == 0:
            c.showPage()
            aux = 0
    c.showPage()
    c.save()


def mostrar():
    print("1. Agregar agente")
    print("2. Modificar agente")
    print("3. Eliminar agente")
    print("4. Generar reporte")
    print("5. Salir")
    opt = int(input(">>> "))

    return opt 

def menu_principal():
    opt = mostrar()
    while opt != 5:
        if opt == 1:
            createAgent()
        elif opt == 2:
            updateAgent()
        elif opt == 3:
            deleteAgent()
        elif opt == 4:
            createReport()
        elif opt == 5:
            exit()
        else:
            print("Opcion incorrecta")
        
        opt = mostrar()


if __name__ == "__main__":
    #main()
    menu_principal()