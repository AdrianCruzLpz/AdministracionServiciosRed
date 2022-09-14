from pysnmp.hlapi import *
from base64 import decode
from fpdf import FPDF

def consultaSNMP(community, host, oid):

    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(), CommunityData(community),
               UdpTransportTarget((host, 161)), ContextData(),
               ObjectType(ObjectIdentity(oid))))

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' %
              (errorStatus.prettyPrint(),
               errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            varB = (' = '.join([x.prettyPrint() for x in varBind]))
            resultado = varB.split()[2]
    return resultado

def optionsMenu():
    print("1. Agregar Agente\n2. Modificar Agente\n3. Eliminar Agente\n4. Generar Reporte")

    return int(input("\n>>> "))

def insertDatAgent():
    datAgent = {}

    datAgent["agentIP"] = input("Direccion IP: ")
    datAgent["port"] = int(input("Puerto: "))
    datAgent["community"] = input("Comunidad: ")
    datAgent["version"] = input("Versión de SNMP: ")

    return datAgent

def createAgent(agentes):

    datoFAgent = insertDatAgent()
    agentes.append(Agente(**datoFAgent))

    print("\nAgregado")

class Agente:

    def __init__(self, agentIP, port, community, version):
        self.agentIP = agentIP
        self.port = port
        self.community = community
        self.version = version

    def ipAgent(self):
        return self.agentIP

    def datAgent(self):
        datAgent = "Direccion IP: " + self.ipAgent() + "\nPuerto: " + str(
            self.port
        ) + "\nComunidad: " + self.community + "\nVersion SNMP: " + self.version + "\n\n"
        return datAgent

    def update(self, agentIP, port, community, version):
        self.agentIP = agentIP
        self.port = port
        self.community = community
        self.version = version

    def sysDescr(self):
        sysDescr = consultaSNMP(self.community, self.agentIP, "1.3.6.1.2.1.1.1.0")
        return "Sistema operativo: " + sysDescr

    def sysName(self):
        sysName = consultaSNMP(self.community, self.agentIP, "1.3.6.1.2.1.1.5.0")
        return "\nNombre del dispositivo: " + sysName

    def sysContact(self):
        sysContact = consultaSNMP(self.community, self.agentIP, "1.3.6.1.2.1.1.4.0")
        return "\nContacto: " + sysContact

    def sysLocation(self):
        sysLocation = consultaSNMP(self.community, self.agentIP, "1.3.6.1.2.1.1.6.0")
        return "\nUbicacion: " + sysLocation

    def ifNumberInterfaces(self):
        ifNumber = consultaSNMP(self.community, self.agentIP, "1.3.6.1.2.1.2.1.0")
        return ifNumber

    def interfaceDescr(self, oid):
        consulta = consultaSNMP(self.community, self.agentIP, oid)
        return "\n" + consulta

    def statusInterfaces(self, oid):
        consulta = consultaSNMP(self.community, self.agentIP, oid)
        return consulta

    def consultas_agente(self):
        consultasTxt = open("infoAgentes.txt", "w")

        insertar_txt(consultasTxt, self.sysDescr())
        insertar_txt(consultasTxt, self.sysName())
        insertar_txt(consultasTxt, self.sysContact())
        insertar_txt(consultasTxt, self.sysLocation())
        insertar_txt(consultasTxt, "\nNumero de interfaces: " + self.ifNumberInterfaces() + "\n")

        for i in range(int(self.ifNumberInterfaces())):
            oidDescr = "1.3.6.1.2.1.2.2.1.2." + str(i + 1)
            oidStatus = "1.3.6.1.2.1.2.2.1.8." + str(i + 1)
            if (self.statusInterfaces(oidStatus) == "1"):
                insertar_txt(consultasTxt, self.interfaceDescr(oidDescr) + "\n\tStatus of Interface -> UP\n\n")
            elif (self.statusInterfaces(oidStatus) == "2"):
                insertar_txt(consultasTxt, self.interfaceDescr(oidDescr) + "\n\tStatus of Interface -> DOWN\n\n")
            else:
                insertar_txt(consultasTxt, self.interfaceDescr(oidDescr) + "\n\tStatus of Interface -> TESTING\n\n")

        consultasTxt.close()


def updateAgent(agentes):

    print("Direccion IP\n")
    host = input("Agente: ")

    for agente in agentes:
        if agente.ipAgent() == host:
            print("Nuevos datos del agente\n")
            datAgent = insertDatAgent()
            agente.update(**datAgent)
            break
        else:
            posicion += 1


def delateAgent(agentes):
    delAgen = input("Direccion IP: ")

    posicion = 0

    for agente in agentes:
        if agente.ipAgent() == delAgen:
            agentes.pop(posicion)
            break
        else:
            posicion += 1

    print("\nEliminado")


def insertar_txt(archivo, texto):
    archivo.write(texto)

class StyleFonts(FPDF):

    def text(self, text, x, y):
        with open(text, "rb") as xy:
            txt = xy.read().decode("latin-1")

        self.set_xy(x, y)
        self.set_text_color(0, 0, 0)
        self.set_font("Arial", '', 12)
        self.multi_cell(0, 5, txt)

    def titles(self, title, x, y):
        self.set_xy(x, y)
        self.set_font("Arial", 'B', 20)
        self.set_text_color(0, 0, 0)
        self.cell(w=210.0, h=40.0, align='C', txt=title, border=0)

    def subtitle(self, sub, x, y):
        self.set_xy(x, y)
        self.set_font("Arial", 'B', 14)
        self.set_text_color(0, 0, 0)
        self.cell(w=100.0, h=40.0, align='C', txt=sub, border=0)
    

def createReport(agentes):
    archivoTxt = open("agente.txt", "w")
    posicion = 0
    nAgente = 1

    print("Direccion IP del agente\n")
    for agente in agentes:
        print(f'{nAgente}. {agente.ipAgent()}')
        nAgente += 1

    agenteSeleccionado = input("\nAgente: ")

    for agente in agentes:
        if agente.ipAgent() == agenteSeleccionado:
            agente.consultas_agente()
            insertar_txt(archivoTxt, agente.datAgent())
            archivoTxt.close()
            break
        else:
            posicion += 1

    filePdf = StyleFonts()
    
    filePdf.add_page()
    filePdf.titles("Administración de Servicios en Red", 0.0, 0.0)
    filePdf.titles("Práctica 1", 0.0, 10.0)
    filePdf.titles("Adquisición de información utilizando SNMP", 0.0, 20.0)
    filePdf.titles("Adrián Cruz López  Grupo: 4CM13", 0.0, 30.0)
    filePdf.subtitle("Información del agente",0.0, 50)
    filePdf.text("infoAgentes.txt", 10.0, 75.0)
    filePdf.output("reportAgent_{}.pdf".format(agente.ipAgent()))


agentes = []
opt = optionsMenu()

while opt != 5:
    if opt == 1:
        createAgent(agentes)

    elif opt == 2:
        updateAgent(agentes)

    elif opt == 3:
        delateAgent(agentes)

    elif opt == 4:
        createReport(agentes)

    else:
        exit()

    opt = optionsMenu()