from CrudAgentes import createAgent, updateAgent, deleteAgent
from reporteRRD import createReport
from ejecutor import ejecutor

def mostrar():
    print("\n\n\t\tSistema de Administracion de Red")
    print("\t    Practica 2 - Administración de contabilidad\n\t Adrian Cruz Lopez     Grupo: 4CM13      2020630087")
    print("\nElige una opcion:")
    print("  1. Agregar dispositivo")
    print("  2. Modificar informacion del dispositivo")
    print("  3. Eliminar dispositivo")
    print("  4. Crear y actualizar base de datos")
    print("  5. Generar reporte")
    print("  6. Salir")
    opt = int(input(">>> "))

    return opt

def menu_principal():
    opt = mostrar()
    while opt != 6:
        if opt == 1:
            createAgent()
        elif opt == 2:
            updateAgent()
        elif opt == 3:
            deleteAgent()
        elif opt == 4:
            ejecutor()
            #mostrar()
        elif opt == 5:
            createReport()
        elif opt == 6:
            exit()
        else:
            print("Opcion incorrecta")

        opt = mostrar()



if __name__ == "__main__":
    menu_principal()
