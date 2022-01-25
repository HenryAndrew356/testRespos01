from DB.conexion import DAO
import funciones

def menuPrincipal():
    continuar=True
    while(continuar):
        correctOption=False
        while(not correctOption):
            print("╔═══════════════════╗")
            print("║   Menu Principal  ║")
            print("║  1 - View Data    ║")
            print("║  2 - Register     ║")
            print("║  3 - Update Data  ║")
            print("║  4 - Delete       ║")
            print("║  5 - Exit         ║")
            print("╚═══════════════════╝")
            opcion=int(input("Seleccione una opcion: "))
            print("")

            if opcion<1 or opcion>5:
                print("Opcion Incorrecta, ingrese nuevamente...")

            elif opcion==5:
                continuar=False
                print("!Gracias por usar este sistema¡")
                break
            else:
                correctOption=True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    # Instanciacion de la clase DAO
    dao=DAO()

    if opcion==1:
        #Listado de Personas
        try:
            personas=dao.listarPersonas()
            if len(personas)>0:
                funciones.listarPersonas(personas)
            else:
                print("No se enconfsdfsdtraron personas ...")
        except:
            print("Ocurrio un error...")

    elif opcion==2:
        persona=funciones.pedirDatosRegistro()

        try:
            dao.registrarPersona(persona)
        except:
            print("Ocurrio un error ...")
    elif opcion==3:
        try:
            personas=dao.listarPersonas()
            if len(personas)>0:
                persona=funciones.pedirDatosUpdate(personas)
                print("-->",persona,"<--")
                if not(persona==""):
                    dao.uppdateDataPersona(persona)
                else:
                    print("No ingreso al if de Update persona.")
            else:
                print("No se encontro la persona para hacer el update")
        except:
            print("Ocurrio un error en la OPCION 3")
    elif opcion==4:
        try:
            personas=dao.listarPersonas()
            if len(personas)>0:
                namePersonaToEliminate=funciones.pedirDatoEliminacion(personas)
                if not(namePersonaToEliminate==""):
                    dao.eliminarPersona(namePersonaToEliminate)
                else:
                    print("El nombre ingresado es incorrecto.\n")
            else:
                print("No se encontraron personas ...")
        except:
            print("Ocurrio un error en la eliminacion")
    else:
        print("Opcion no valida ... ")
    
    print("Utd selecciono --> \n",opcion)

menuPrincipal()