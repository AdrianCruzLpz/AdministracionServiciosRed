import time
import rrdtool
from getSNMP import consultaSNMP

print('Escriba la ip del agente')
ip_agente = input()
datos = []
ip = []
comunidad = []

with open('agentes.txt') as archivo:
    for lineas in archivo:
        datos.extend(lineas.split())

numero_agentes = int(len(datos)/3)

indice_ip = datos.index(ip_agente)
comunidad = datos[indice_ip + 2]

while 1:

    paquetes_multicast_env = int(
        consultaSNMP(comunidad,datos[indice_ip],
                     '1.3.6.1.2.1.2.2.1.17.1'))
    paquetes_ip = int(
        consultaSNMP(comunidad,datos[indice_ip],
                     '1.3.6.1.2.1.4.10.0'))
    mensajes_icmp = int(
        consultaSNMP(comunidad,datos[indice_ip],
                     '1.3.6.1.2.1.5.1.0'))
    segmentos_retransmitidos = int(
        consultaSNMP(comunidad,datos[indice_ip],
                     '1.3.6.1.2.1.6.12.0'))
    datagramas_env = int(
        consultaSNMP(comunidad,datos[indice_ip],
                     '1.3.6.1.2.1.7.4.0'))
    valor = "N:" + str(paquetes_multicast_env) + ':' + str(paquetes_ip) + ':' + str(mensajes_icmp) + ':' + str(segmentos_retransmitidos) + ':' + str(datagramas_env)
    print (valor)
    rrdtool.update('segmentosRed.rrd', valor)
    # rrdtool.dump('traficoRED.rrd','traficoRED.xml')
    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)