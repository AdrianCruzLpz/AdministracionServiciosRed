def parametros_agente():
    print('ingrese ip')
    ip = input()
    print('ingrese puerto (161)')
    puerto = input()
    print('ingrese comunidad')
    comunidad = input()
    print('ingrese versión SNMP')
    version = input()
    agregar_agente(ip, puerto, comunidad, version)

def agregar_agente(ip, puerto, comunidad, version):
    f = open('./agentes.txt', 'a')
    f.write(ip)
    f.write('\n')
    f.write(puerto)
    f.write('\n')
    f.write(comunidad)
    f.write('\n')
    f.write(version)
    f.write('\n\n')
    f.close()

def modificar_agente():
    datos_agente = []
    print('Escriba la ip del agente a modificar')
    ipm = input()

    with open("agentes.txt") as archivo:
        for lineas in archivo:
           datos_agente.extend(lineas.split())

    posicion = datos_agente.index(ipm)
    aux = int(posicion/4)
    print(aux)
    posicion_comunidad = posicion + aux + 2
    posicion_version = posicion + aux + 3

    print('¿Qué dato desea modificar?')
    print('1. IP')
    print('2. Comunidad')
    print('3. Version SNMP')
    opcion = input()

    if opcion == '1':
        print('Escriba la nueva IP')
        nueva_ip = input()

        with open("agentes.txt", "rt") as file:
            x = file.read()

        with open("agentes.txt", "wt") as file:
            x = x.replace(ipm, nueva_ip)
            file.write(x)

    elif opcion == '2':
        print('Escriba la nueva comunidad')
        nueva_comunidad = input()
        with open('agentes.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
            print(data)
        data[posicion_comunidad] = nueva_comunidad + '\n'
        with open('agentes.txt', 'w', encoding='utf-8') as file:
            file.writelines(data)

    elif opcion == '3':
        print('Escriba la versión deseada')
        nueva_version = input()
        with open('agentes.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()

        data[posicion_version] = nueva_version + '\n'
        with open('agentes.txt', 'w', encoding='utf-8') as file:
            file.writelines(data)

def eliminar_agente():
    datos_agente = []
    print('Escriba la ip del agente a eliminar')
    ipm = input()

    with open("agentes.txt") as archivo:
        for lineas in archivo:
           datos_agente.extend(lineas.split())

    posicion = datos_agente.index(ipm)
    aux = int(posicion/4)
    print(aux)
    posicion_ip = posicion + aux
    posicion_puerto = posicion + aux + 1
    posicion_comunidad = posicion + aux + 2
    posicion_version = posicion + aux + 3
    posicion_salto = posicion + aux + 4

    with open('agentes.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    data[posicion_ip] = ''
    data[posicion_puerto] = ''
    data[posicion_comunidad] = ''
    data[posicion_version] = ''
    data[posicion_salto] = ''
    with open('agentes.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)