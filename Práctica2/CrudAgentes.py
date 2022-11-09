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

def updateAgent():
    datos_agente = []
    #print('Escriba la ip del agente a modificar')
    #ipm = input("Direccion IP del agente a modificar: ")
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