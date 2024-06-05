"""Clase que permite la conexión con la BD y métodos para ejecutar
consultas, con la base de datos
"""
import mysql.connector
from mysql.connector import Error

class Database:

    def __init__(self, host, port, user, password, db):
        
        try:
            self.conexion=mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                db=db
            )
            self.cursor=self.conexion.cursor()            
            print("Conexion exitosa")
            self.cursor.execute("SELECT database();") #da el nombre de la BD
            registro=self.cursor.fetchone()
            print("Conectado a la BD:", registro)

        except Error as ex:
            print("Error de conexion", ex)
            self.conexion=None
            self.cursor=None
    
    #Metodos para (INSERT, UPDATE, DELETE) datos
    def ejecutarConsultas(self, consulta, valores=None):
        self.cursor.execute(consulta, valores)
        self.conexion.commit()
    
   #Metodo para consultar SELECT y retorna resultados
    def obtenerResultados(self, consulta, valores=None):
        self.cursor.execute(consulta, valores)
        return self.cursor.fetchall()
        
    def cerrarConexion(self):
        print("     ¡Gracias por utilizar la aplicación!")
        self.cursor.close()
        self.conexion.close()
        print("Se cerró la conexión con la Base de Datos")

#db=Database("localhost", 3306,"root","root","huerta") 
#print(db)


