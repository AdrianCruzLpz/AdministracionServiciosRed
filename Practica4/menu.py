from ejecutor import ejecutor
from ftp import enviarFTP, descargarFTP

def mostrar():
    print("\n\n\t\tSistema de Administracion de Red")
    print("\tPractica 4 - Módulo de Administración de configuración\n\t    Adrian Cruz Lopez   Grupo: 4CM13    2020630087")
    print("\nElige una opcion:")
    print("  1. Generar archivo de configuracion")
    print("  2. Enviar archivo de configuracion")
    print("  3. Descargar archivo de configuracion")
    print("  4. Salir")
    opt = int(input(">>> "))

    return opt

def menu_principal():
    opt = mostrar()
    while opt != 4:
        if opt == 1:
            ejecutor()
        elif opt == 2:
            enviarFTP()
        elif opt == 3:
            descargarFTP()
        elif opt == 4:
            exit()
        else:
            print("Opcion incorrecta")

        opt = mostrar()

if __name__ == "__main__":
    menu_principal()