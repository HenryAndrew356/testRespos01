def listarPersonas(cursos):
    print("")
    print("Personas: ")
    contador=1
    for per in cursos:
        datos="{0}. {4} | {1} | {2} | {3}"
        print(datos.format(contador,per[0],per[1],per[2],per[3]))
        contador+=1
    print(" ")

def pedirDatosRegistro():
    conexion_=input("Ingrese conexion: ")
    nombreApellido_=input("Ingrese nombre/Apellido: ")
    localidad_=input("Ingrese localidad: ")
    comentario_=input("Ingrese comentario: ")

    persona=(conexion_,nombreApellido_,localidad_,comentario_)
    return persona

def pedirDatoEliminacion(personas):
    listarPersonas(personas)
    existePersona=False
    name_persona_to_eliminate=input("Ingrese el nombre de la persona a eliminar: ")
    for per in personas:
        if per[1]==name_persona_to_eliminate:
            existePersona=True
            break
    if not existePersona:
        name_persona_to_eliminate=""
    return name_persona_to_eliminate

def pedirDatosUpdate(personas):
    listarPersonas(personas)
    existePersona=False
    namePersonaToEdit=input("Ingrese el nombre de la persona a editar: ")
    for per in personas:
        if per[1]==namePersonaToEdit:
            existePersona=True
            break
    if existePersona:
        localidad_=input("Ingrese localidad a modificar: ")
        data_interesante=input("Ingrese comentario a modificar: ")
        conexion_=input("Ingrese conexion a modificar: ")
        persona=(conexion_,namePersonaToEdit,localidad_,data_interesante)
    else:
        curso=None
    print("retornando->",persona[0],persona[1],persona[2],persona[3])
    return persona