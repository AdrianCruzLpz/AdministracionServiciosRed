from main import telnetRCP1, telnetRCP2

def ejecutor():
    print("IP del router\n")
    ip = input()
    
    print("Desea generar el archivo de configuración de otro router? S/N")
    opc = input()

    if(opc == "n"):
        telnetRCP1(ip)
    
    else:
        print("IP del router\n")
        ipAux = input()
        telnetRCP2(ip, ipAux)
