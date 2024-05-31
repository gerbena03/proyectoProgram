"""clase que genera objetos hortalizas a sembrar con sus caracteristicas fenologicas 
    fechas de siembra, cosecha, labores culturales según la epoca del año y según el tamaño del terreno a sembrar,
     establecido por el usuario determine un rendimiento promedio"""


import datetime
import mysql.connector
from mysql.connector import Error


try:
    conexion=mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        db="huerta"
    )

    if conexion.is_connected:
        print("Conexion exitosa")
        cursor=conexion.cursor(buffered=True)
        cursor.execute("SELECT database();") #da el nombre de la BD
        registro=cursor.fetchone()
        print("conectado a la BD:", registro)

except Error as ex:
    print("Error de conexion", ex)



def principal():
        """metodo inicio programa
        Args: eleccion(int): Menú 
        """
        temporada=int(input("Por favor seleccione la temporada de la hortaliza a trabajar : \n"
        "1. PRIMAVERA- VERANO\n"
        "2. OTOÑO- INVIERNO\n"))
        return temporada




class horticultura():

    def __init__(self, temporada) -> None:
        
        self.nombreEspecie=""
        self.familia=""
        self.temporada=temporada
        self.fechaSiembra=0
        self.fechaCosecha=0
        self.rendimiento=0
        self.variedad=0
        self.__lista= []
        self.__listaPV= {}
        self.__listaOI={}
        self.idVariedad=0


    def setVariedad(self,cambioVar):
        self.variedad=cambioVar

    def setIdVariedad(self, id):
        self.idVariedad=id

    def getPrimaveraVerano(self):
        cursor.execute("SELECT idvariedad,nombreVariedad FROM variedad WHERE estacion=1")
        conexion.commit

        for x in cursor:
            print(x)
        return ""
       

    def getOtonoInvierno(self):
        cursor.execute("SELECT idvariedad,nombreVariedad FROM variedad WHERE estacion=2")
        conexion.commit

        for x in cursor:
            print(x)
        
        return ""
    
    
    def getTemporada(self):
        return self.temporada
       
    
    def variedadHortaliza(self,param):
        """función que trae listado de variedades
            Args: eleccion(int): variedades
            """
        if param==1:
            valor=int(input(f"Seleccione la variedad a trabajar: {self.getPrimaveraVerano()}\n"))
            consulta1="SELECT nombreVariedad FROM variedad WHERE idvariedad="+str(valor)
            cursor.execute(consulta1)
            conexion.commit()
            
            for i in cursor:
                self.variedad=i
            
            self.setIdVariedad(valor)
         
            print("------------------")
            

        elif param==2:
            valor=int(input(f"Seleccione la variedad a trabajar: {self.getOtonoInvierno()}\n"))
            consulta1="SELECT nombreVariedad FROM variedad WHERE idvariedad=" +str(valor)
            cursor.execute(consulta1)
            conexion.commit()
            
            for i in cursor:
        
                self.variedad=i
            
        
            print("------------------")

    
    def menuLabores(self):
        """función que muestra menú labores
        Args: eleccion(int): Menú 2
        """
        while True:
            print("------------------")
            print("LABORES")
        
            cursor.execute("SELECT idActividad, actividades FROM actividad")
            conexion.commit()
            for i in cursor:
                print(i)
            labor=int(input("Seleccione la labor a realizar, o presione 7 para volver al menú anterior:\n"))
           
            
            if labor==1:
                print("Preparación del Suelo")
                dia=int(input("Seleccione dia: "))
                mes=int(input("Seleccione mes: "))
                agno=int(input("Seleccione año: "))
                print("Seleccione el lote a trabajar:")
                print("------------------")
                cursor.execute("SELECT idParcela, parcela FROM  parcela")
                conexion.commit()
                for x in cursor:
                    print(x)
                lote=int(input("Seleccione lote: "))
                fecha=datetime.date(agno, mes, mes)
                print(self.idVariedad)
                sql=("INSERT INTO labores(variedad, actividad, fecha, parcela) VALUES (%s,%s,%s,%s)")
                datos=(self.idVariedad, labor,fecha,lote)
                cursor.execute(sql,datos)
                conexion.commit()

                print("------------------")
            if labor==2:
                print("Siembra")
                print("------------------")
            if labor==3:
                print("Raleo")
                print("------------------")
            if labor ==4:
                print("Abono")
                print("------------------")
            if labor ==5:
                print("Cosecha")
                print("------------------")
            if labor==6:
                print("Riego")
            if labor==7:   
                self.menuDecision()                 
                #self.menu2()
                break
        
                
            
    
    
    def menuDecision(self):
        """función que muestra accion a realizar
        Args: eleccion(int): Menú 
        """
        print("ACTIVIDADES A REALIZAR PARA EL CULTIVO DE:",  self.variedad , "\n 1. Labores a realizar \n 2. Obtención de Rendimiento \n" 
        " 3. Características del cultivo \n 4. Listado de las hortalizas cargadas en el sistema\n 5. Cambiar de cultivo\n 6. SALIR")
        
    def menu2(self):
        """función que solicita al usuario
        la eleccion de una actividad
        Args: opcionMenu2(int): menu"""

        while True:
            self.menuDecision()

            opcionMenu2=int(input("Seleccione la opción deseada: "))

            if opcionMenu2==1:
                self.menuLabores()
            elif opcionMenu2==2:
                if self.temporada==1:

                    print("     Aqui se calcula el rendimiento promedio del cultivo de: ", self.variedad)
                    print("------------------")
                    
                elif self.temporada==2:
                    print("     Aquí se calcula el rendimiento promedio del cultivo de: ", self.variedad )
                    print("------------------")
                else:
                    print("lanzar excepción")


            elif opcionMenu2==3:
                print("     Características del cultivo de: ", self.variedad)
                print("------------------")
            elif opcionMenu2==4:
                print("     Variedades Otoño-Invierno", self.getOtonoInvierno())
                print("     Variedades Primavera-Verano", self.getPrimaveraVerano())
                print("------------------")
            elif opcionMenu2==5:
               
               self.variedadHortaliza(principal())
               

            elif opcionMenu2==6:
                
                print("     Gracias por utilizar la aplicación!")
                cursor.close()
                conexion.close()
                print("Se cerró la conexión con la Base de Datos")
                break
                
            
        


print("BIENVENIDO A LA HUERTA EN TUS MANOS")
huerta1=horticultura(principal())

huerta1.variedadHortaliza(huerta1.getTemporada())

huerta1.menu2()










