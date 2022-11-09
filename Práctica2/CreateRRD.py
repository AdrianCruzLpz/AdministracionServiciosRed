#!/usr/bin/env python
import rrdtool
ret = rrdtool.create("segmentosRed.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:paquetesMulticast:COUNTER:120:U:U",
                     "DS:paquetesIp:COUNTER:120:U:U",
                     "DS:mensajesICMP:COUNTER:120:U:U",
                     "DS:segmentosTCP:COUNTER:120:U:U",
                     "DS:datagramas:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:6:500",
                     "RRA:AVERAGE:0.5:1:1000")
if ret:
    print (rrdtool.error())