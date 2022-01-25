import mysql.connector
from mysql.connector import Error

#Creando la Clase DAO ( Data Access Object )
class DAO():
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='data_base_prove02'                
            )
        except Error as ex:
            print("Error al intentar la conexion: {0}".format(ex))
    
    def listarPersonas(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM cliente ORDER BY nombreApellido ASC")
                resultados=cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))

    # self <-- referencia a la propia clase
    def registrarPersona(self,persona):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="INSERT INTO cliente(conexion,nombreApellido,Localidad,dataInteresante) VALUES ('{0}','{1}','{2}','{3}')"
                cursor.execute(sql.format(persona[0],persona[1],persona[2],persona[3]))
                self.conexion.commit()
                print("-->Persona Registrada<--")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))

    
    def eliminarPersona(self,nombre_persona_eliminar):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="DELETE FROM cliente WHERE nombreApellido='{0}'"
                cursor.execute(sql.format(nombre_persona_eliminar))
                self.conexion.commit()
                print("-->Persona Eliminada<--")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))

    def uppdateDataPersona(self,persona):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="UPDATE cliente SET conexion='{0}',Localidad='{2}',dataInteresante='{3}' WHERE nombreApellido='{1}'"
                cursor.execute(sql.format(persona[0],persona[1],persona[2],persona[3]))
                self.conexion.commit()
                print("-->Data Actulizada<--")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))