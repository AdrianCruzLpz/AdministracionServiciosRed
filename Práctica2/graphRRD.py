import sys
import rrdtool
import time

#print("Ingrese la fecha de tiempo inicial (dd.mm.yyyy 00:00:00)")
date_time = input("Ingrese la fecha de tiempo inicial (dd.mm.yyyy 00:00:00)\n" )
pattern = '%d.%m.%Y %H:%M:%S'
epoch = int(time.mktime(time.strptime(date_time, pattern)))
tiempo_actual = int(time.time())
tiempo_inicial = epoch

# ret = rrdtool.graphv( "segmentosTCP.png",
#                      "--start",str(tiempo_inicial),
#                      "--end","N",
#                      "--vertical-label=Segmentos",
#                      "--title=Segmentos TCP de un agente \n Usando SNMP y RRDtools",
#                      "DEF:sEntrada=segmentosRed.rrd:segmentosEntrada:AVERAGE",
#                      "DEF:sSalida=segmentosRed.rrd:segmentosSalida:AVERAGE",
#                       "VDEF:segEntradaLast=sEntrada,LAST",
#                       "VDEF:segEntradaFirst=sEntrada,FIRST",
#                       "VDEF:segEntradaMax=sEntrada,MAXIMUM",
#                       "VDEF:segEntradaDev=sEntrada,STDEV",
#                       "CDEF:Nivel1=sEntrada,1,LT,0,sEntrada,IF",
#                       "PRINT:segEntradaLast:%6.2lf",
#                       "PRINT:segEntradaFirst:%6.2lf",
#                      "GPRINT:segEntradaMax:%6.2lf %S segEntMAX",
#                      "GPRINT:segEntradaDev:%6.2lf %S STDEV",
#                      "LINE3:sEntrada#FF0000:Segmentros recibidos",
#                      "LINE3:sSalida#0000FF:Segmentos enviados",
#                      "AREA:Nivel1#00FF00:Segmentos recibidos sobre el nivel")
# print(ret)

ret = rrdtool.graphv( "paquetesMulticast.png",
                     "--start",str(tiempo_inicial),
                     "--end","N",
                     "--vertical-label=Segmentos",
                     "--title=Paquetes Multicast que ha enviado la interfaz \n Usando SNMP y RRDtools",
                     "DEF:sEntrada=segmentosRed.rrd:paquetesMulticast:AVERAGE",
                      "VDEF:segEntradaLast=sEntrada,LAST",
                      "VDEF:segEntradaFirst=sEntrada,FIRST",
                      "VDEF:segEntradaMax=sEntrada,MAXIMUM",
                      "VDEF:segEntradaDev=sEntrada,STDEV",
                      "CDEF:Nivel1=sEntrada,1,LT,0,sEntrada,IF",
                      "PRINT:segEntradaLast:%6.2lf",
                      "PRINT:segEntradaFirst:%6.2lf",
                     "GPRINT:segEntradaMax:%6.2lf %S segEntMAX",
                     "GPRINT:segEntradaDev:%6.2lf %S STDEV",
                     "LINE3:sEntrada#FF0000:Paquetes Multicast enviados")
# print(ret)

ret2 = rrdtool.graphv( "paquetesIp.png",
                     "--start",str(tiempo_inicial),
                     "--end","N",
                     "--vertical-label=Segmentos",
                     "--title=Paquetes ip que los protocolos locales suministraron a ip \n Usando SNMP y RRDtools",
                     "DEF:sEntrada=segmentosRed.rrd:paquetesIp:AVERAGE",
                      "VDEF:segEntradaLast=sEntrada,LAST",
                      "VDEF:segEntradaFirst=sEntrada,FIRST",
                      "VDEF:segEntradaMax=sEntrada,MAXIMUM",
                      "VDEF:segEntradaDev=sEntrada,STDEV",
                      "CDEF:Nivel1=sEntrada,1,LT,0,sEntrada,IF",
                      "PRINT:segEntradaLast:%6.2lf",
                      "PRINT:segEntradaFirst:%6.2lf",
                     "GPRINT:segEntradaMax:%6.2lf %S segEntMAX",
                     "GPRINT:segEntradaDev:%6.2lf %S STDEV",
                     "LINE3:sEntrada#9B00FF:Paquetes ip")
# print(ret2)

ret3 = rrdtool.graphv( "mensajesICMP.png",
                     "--start",str(tiempo_inicial),
                     "--end","N",
                     "--vertical-label=Segmentos",
                     "--title=Mensajes ICMP que ha recibido el agente \n Usando SNMP y RRDtools",
                     "DEF:sEntrada=segmentosRed.rrd:mensajesICMP:AVERAGE",
                      "VDEF:segEntradaLast=sEntrada,LAST",
                      "VDEF:segEntradaFirst=sEntrada,FIRST",
                      "VDEF:segEntradaMax=sEntrada,MAXIMUM",
                      "VDEF:segEntradaDev=sEntrada,STDEV",
                      "CDEF:Nivel1=sEntrada,1,LT,0,sEntrada,IF",
                      "PRINT:segEntradaLast:%6.2lf",
                      "PRINT:segEntradaFirst:%6.2lf",
                     "GPRINT:segEntradaMax:%6.2lf %S segEntMAX",
                     "GPRINT:segEntradaDev:%6.2lf %S STDEV",
                     "LINE3:sEntrada#009EFF:Mensajes ICMP recibidos")
# print(ret3)

ret4 = rrdtool.graphv( "segmentosTCP.png",
                     "--start",str(tiempo_inicial),
                     "--end","N",
                     "--vertical-label=Segmentos",
                     "--title=Segmentos TCP de un agente \n Usando SNMP y RRDtools",
                     "DEF:sEntrada=segmentosRed.rrd:segmentosTCP:AVERAGE",
                      "VDEF:segEntradaLast=sEntrada,LAST",
                      "VDEF:segEntradaFirst=sEntrada,FIRST",
                      "VDEF:segEntradaMax=sEntrada,MAXIMUM",
                      "VDEF:segEntradaDev=sEntrada,STDEV",
                      "CDEF:Nivel1=sEntrada,1,LT,0,sEntrada,IF",
                      "PRINT:segEntradaLast:%6.2lf",
                      "PRINT:segEntradaFirst:%6.2lf",
                     "GPRINT:segEntradaMax:%6.2lf %S segEntMAX",
                     "GPRINT:segEntradaDev:%6.2lf %S STDEV",
                     "LINE3:sEntrada#27FF00:Segmentros recibidos")
# print(ret4)

ret5 = rrdtool.graphv( "datagramas.png",
                     "--start",str(tiempo_inicial),
                     "--end","N",
                     "--vertical-label=Segmentos",
                     "--title=Datagramas enviados por el dispositivo \n Usando SNMP y RRDtools",
                     "DEF:sEntrada=segmentosRed.rrd:datagramas:AVERAGE",
                      "VDEF:segEntradaLast=sEntrada,LAST",
                      "VDEF:segEntradaFirst=sEntrada,FIRST",
                      "VDEF:segEntradaMax=sEntrada,MAXIMUM",
                      "VDEF:segEntradaDev=sEntrada,STDEV",
                      "CDEF:Nivel1=sEntrada,1,LT,0,sEntrada,IF",
                      "PRINT:segEntradaLast:%6.2lf",
                      "PRINT:segEntradaFirst:%6.2lf",
                     "GPRINT:segEntradaMax:%6.2lf %S segEntMAX",
                     "GPRINT:segEntradaDev:%6.2lf %S STDEV",
                     "LINE3:sEntrada#FFE800:Datagramas enviados")
# print(ret5)