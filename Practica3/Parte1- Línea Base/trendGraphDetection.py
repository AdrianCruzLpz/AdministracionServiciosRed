import sys
import rrdtool
from  Notify import send_alert_attached
import time

rrdpath = '../RRD/'
imgpath = '../IMG/'

ultima_lectura_procesador = int(rrdtool.last(rrdpath+"trend.rrd"))
tiempo_final_procesador = ultima_lectura_procesador
tiempo_inicial_procesador = tiempo_final_procesador - 600


def graficar():

    ret = rrdtool.graphv( imgpath+"deteccionProcesador.png",
                     "--start",str(tiempo_inicial_procesador),
                     "--end",str(tiempo_final_procesador),
                     "--vertical-label=CPU load",
                    '--lower-limit', '0',
                    '--upper-limit', '100',
                    "--title=Carga del CPU del agente Usando SNMP y RRDtools \n Detección de umbrales",
                    "DEF:cargaCPU="+rrdpath+"trend.rrd:CPUload:AVERAGE",
                     "VDEF:cargaMAX=cargaCPU,MAXIMUM",
                     "VDEF:cargaMIN=cargaCPU,MINIMUM",
                     "VDEF:cargaSTDEV=cargaCPU,STDEV",
                     "VDEF:cargaLAST=cargaCPU,LAST",
                 #   "CDEF:cargaEscalada=cargaCPU,8,*",
                     "CDEF:umbral20=cargaCPU,30,LT,0,cargaCPU,IF",
                     "AREA:cargaCPU#00FF00:Carga del CPU",
                     "AREA:umbral20#FF9F00:Carga CPU mayor que 30",
                     "HRULE:20#FF0000:Umbral 30 - 5%",

                     "CDEF:umbral30=cargaCPU,40,LT,0,cargaCPU,IF",
                     "AREA:cargaCPU#00FF00:Carga del CPU",
                     "AREA:umbral30#FF9F00:Carga CPU mayor que 40",
                     "HRULE:30#FF0000:Umbral 40 - 5%",

                     "CDEF:umbral40=cargaCPU,50,LT,0,cargaCPU,IF",
                     "AREA:cargaCPU#00FF00:Carga del CPU",
                     "AREA:umbral40#FF9F00:Carga CPU mayor que 50",
                     "HRULE:40#FF0000:Umbral 50 - 5%",
                     "PRINT:cargaLAST:%6.2lf",
                     "GPRINT:cargaMIN:%6.2lf %SMIN",
                     "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                     "GPRINT:cargaLAST:%6.2lf %SLAST" )
    #print (ret)
    ultimo_valor_procesador=float(ret['print[0]'])

    #print("Sobrepasa Umbral línea base")    
    #send_alert_attached("Sobrepasa Umbral línea base")

def graficar2():

    ret = rrdtool.graphv( imgpath+"deteccionProcesador.png",
                     "--start",str(tiempo_inicial_procesador),
                     "--end",str(tiempo_final_procesador),
                     "--vertical-label=CPU load",
                    '--lower-limit', '0',
                    '--upper-limit', '100',
                    "--title=Carga del CPU del agente Usando SNMP y RRDtools \n Detección de umbrales",
                    "DEF:cargaCPU="+rrdpath+"trend.rrd:CPUload:AVERAGE",
                     "VDEF:cargaMAX=cargaCPU,MAXIMUM",
                     "VDEF:cargaMIN=cargaCPU,MINIMUM",
                     "VDEF:cargaSTDEV=cargaCPU,STDEV",
                     "VDEF:cargaLAST=cargaCPU,LAST",
                 #   "CDEF:cargaEscalada=cargaCPU,8,*",
                     "CDEF:umbral20=cargaCPU,20,LT,0,cargaCPU,IF",
                     "AREA:cargaCPU#00FF00:Carga del CPU",
                     "AREA:umbral20#FF9F00:Carga CPU mayor que 20",
                     "HRULE:20#FF0000:Umbral 10 - 5%",
  
                     "CDEF:umbral30=cargaCPU,30,LT,0,cargaCPU,IF",
                     "AREA:umbral30#FF9F00:Carga CPU mayor que 30",
                     "HRULE:30#FF0000:Umbral 10 - 5%",

                     "CDEF:umbral40=cargaCPU,40,LT,0,cargaCPU,IF",
                     "AREA:umbral40#FF9F00:Carga CPU mayor que 40",
                     "HRULE:40#FF0000:Umbral 10 - 5%",

                     "PRINT:cargaLAST:%6.2lf",
                     "GPRINT:cargaMIN:%6.2lf %SMIN",
                     "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                     "GPRINT:cargaLAST:%6.2lf %SLAST" )
    #print (ret)
    ultimo_valor_procesador=float(ret['print[0]'])

    #print("Sobrepasa Umbral línea base")    
    #send_alert_attached("Sobrepasa segundo Umbral")

def graficar3():

    ret = rrdtool.graphv( imgpath+"deteccionProcesador.png",
                     "--start",str(tiempo_inicial_procesador),
                     "--end",str(tiempo_final_procesador),
                     "--vertical-label=CPU load",
                    '--lower-limit', '0',
                    '--upper-limit', '100',
                    "--title=Carga del CPU del agente Usando SNMP y RRDtools \n Detección de umbrales",
                    "DEF:cargaCPU="+rrdpath+"trend.rrd:CPUload:AVERAGE",
                     "VDEF:cargaMAX=cargaCPU,MAXIMUM",
                     "VDEF:cargaMIN=cargaCPU,MINIMUM",
                     "VDEF:cargaSTDEV=cargaCPU,STDEV",
                     "VDEF:cargaLAST=cargaCPU,LAST",
                 #   "CDEF:cargaEscalada=cargaCPU,8,*",
                     "CDEF:umbral20=cargaCPU,20,LT,0,cargaCPU,IF",
                     "AREA:cargaCPU#00FF00:Carga del CPU",
                     "AREA:umbral20#FF9F00:Carga CPU mayor que 20",
                     "HRULE:20#FF0000:Umbral 20 - 5%",

                     "CDEF:umbral30=cargaCPU,30,LT,0,cargaCPU,IF",
                     "AREA:cargaCPU#00FF00:Carga del CPU",
                     "AREA:umbral30#FF9F00:Carga CPU mayor que 30",
                     "HRULE:30#FF0000:Umbral 30 - 5%",

                     "CDEF:umbral40=cargaCPU,40,LT,0,cargaCPU,IF",
                     "AREA:cargaCPU#00FF00:Carga del CPU",
                     "AREA:umbral40#FF9F00:Carga CPU mayor que 40",
                     "HRULE:40#FF0000:Umbral 40 - 5%",
                     "PRINT:cargaLAST:%6.2lf",
                     "GPRINT:cargaMIN:%6.2lf %SMIN",
                     "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                     "GPRINT:cargaLAST:%6.2lf %SLAST" )
    #print (ret)
    ultimo_valor_procesador=float(ret['print[0]'])

    print("Sobrepasa Umbral línea base")    
    send_alert_attached("Sobrepasa tercer Umbral línea base")