import time
import rrdtool
from getSNMP import consultaSNMP
from trendGraphDetection import graficar, graficar2, graficar3

rrdpath = '../RRD/'
carga_CPU = 0

def consultas():
    print('Escriba la ip del agente')
    ip_agente = input()
    datos = []
    with open('agentes.txt') as archivo:
        for lineas in archivo:
            datos.extend(lineas.split())

    numero_agentes = int(len(datos) / 3)

    indice_ip = datos.index(ip_agente)
    comunidad = datos[indice_ip + 2]

    while 1:
        carga_CPU = int(consultaSNMP(comunidad,datos[indice_ip],'1.3.6.1.2.1.25.3.3.1.2.196608'))
        #total_ram = int(consultaSNMP(comunidad,datos[indice_ip],'1.3.6.1.4.1.2021.4.5.0'))
        #free_ram = int(consultaSNMP(comunidad,datos[indice_ip],'1.3.6.1.4.1.2021.4.11.0'))
        #shared_ram = int(consultaSNMP(comunidad,datos[indice_ip],'1.3.6.1.4.1.2021.4.13.0'))
        #buff_ram = int(consultaSNMP(comunidad,datos[indice_ip],'1.3.6.1.4.1.2021.4.14.0'))
        #cache_ram = int(consultaSNMP(comunidad,datos[indice_ip],'1.3.6.1.4.1.2021.4.15.0'))
        #used_ram = free_ram + shared_ram + (buff_ram/cache_ram)
        #carga_ram = (used_ram*100)/total_ram
        #carga_traficoEntrada = int(consultaSNMP(comunidad,datos[indice_ip],'1.3.6.1.2.1.2.2.1.10.1'))
        #carga_traficoSalida = int(consultaSNMP(comunidad,datos[indice_ip],'1.3.6.1.2.1.2.2.1.16.1'))
        
        valor = "N:" + str(carga_CPU)
        print(valor)
        rrdtool.update(rrdpath+'trend.rrd', valor)
        
        """if (carga_CPU > 20 and carga_CPU < 30):
            graficar()
            time.sleep(5)"""

        """if (carga_CPU > 40 and carga_CPU < 50):
            graficar2()
            time.sleep(5)"""

        if (carga_CPU > 50):
            graficar3()
            time.sleep(5)


    if ret:
        print (rrdtool.error())
        time.sleep(300)

