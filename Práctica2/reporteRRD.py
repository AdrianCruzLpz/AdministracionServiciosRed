from datetime import datetime

def createReport():
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from getSNMP import consultaSNMP
    import time

    ip_agente = input('Direccion IP del agente a generar reporte: \n')
    datos = []

    exec(open("graphRRD.py").read())

    w, h = letter
    c = canvas.Canvas("ReportAgent_{}.pdf".format(ip_agente), pagesize=letter)
    interlineado = 50

    text = c.beginText(0, h - interlineado + 25)

    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(w/2, h - interlineado,"Administración de Servicios en Red")
    c.drawCentredString(w/2, h - (interlineado+25), "Práctica 2")
    c.drawCentredString(w/2, h - (interlineado+45), "Administración de contabilidad")
    c.drawCentredString(w/2, h - (interlineado+70), "Cruz López Adrián      Grupo: 4CM13")

    c.drawText(text)

    with open('agentes.txt') as archivo:
        for lineas in archivo:
            datos.extend(lineas.split())

    numero_agentes = int(len(datos) / 3)

    indice_ip = datos.index(ip_agente)
    comunidad = datos[indice_ip + 2]

    info = ['1.3.6.1.2.1.1.5.0', '1.3.6.1.2.1.1.4.0', '1.3.6.1.2.1.4.2.0', '1.3.6.1.2.1.2.2.1.10.1', '1.3.6.1.2.1.2.2.1.16.1', '1.3.6.1.2.1.1.3.0', '1.3.6.1.2.1.2.2.1.11.1','1.3.6.1.2.1.2.2.1.17.1']

    name_user = consultaSNMP(comunidad,datos[indice_ip],info[1])
    # print(name_user)
    delay = consultaSNMP(comunidad,datos[indice_ip],info[2])
    # print(delay)
    input_octets = consultaSNMP(comunidad,datos[indice_ip],info[3])
    # print(input_octets)
    output_octets = consultaSNMP(comunidad,datos[indice_ip],info[4])
    # print(output_octets)
    sesion_time = consultaSNMP(comunidad,datos[indice_ip],info[5])
    # print(sesion_time)
    input_paquets = consultaSNMP(comunidad,datos[indice_ip],info[6])
    # print(input_paquets)
    output_paquets = consultaSNMP(comunidad,datos[indice_ip],info[7])
    # print(output_paquets)

    text = c.beginText(50, h - (interlineado+100))
    text.setFont("Times-Roman", 12)
    text.textLines("version: 1" + "\n" +
                   "device: server3" + "\n" +
                   "description: Accouting Server 3" + "\n" +
                   "date: " + str(datetime.now()) + "\n" +
                   "default protocol: Radius" + "\n\n" +
                   "rdate: " + str(datetime.now()) + "\n" +
                   "#NAS-Ip address: " + "\n" + "4:" + datos[indice_ip] + "\n" +
                   "#NAS-Port-Type:" + "\n" + "5:61:2" + "\n" +
                   "#NAS-User-name: " + "\n" + "1:" + name_user + "\n" +
                   "#Acct-Status-Type:40:1" + "\n" +
                   "#Acct-Delay-Time:" + "\n" + "41:"  + delay + "\n" +
                   "#Acct-Input-Octets:" + "\n" + "42:"  + input_octets + "\n" +
                   "#Acct-Output-Octets:" + "\n" + "43:" + output_octets + "\n" +
                   "#Acct-Session-Id:" + "\n" + "44:185")

    c.drawText(text)
    c.showPage()

    c.drawImage('paquetesMulticast.png', 185, 0, 240, 135)
    c.drawImage('paquetesIp.png', 185, 150, 240, 135)
    c.drawImage('mensajesICMP.png', 185, 300, 240, 135)
    c.drawImage('segmentosTCP.png', 185, 450, 240, 135)
    c.drawImage('datagramas.png', 185, 600, 240, 135)
    c.showPage()
    c.save()
