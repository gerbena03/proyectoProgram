
import datetime
from database import Database
from datetime import date
"""clase que genera objetos hortalizas a sembrar con sus caracteristicas fenologicas 
    fechas de siembra, cosecha, labores culturales según la epoca del año y según el tamaño del terreno a sembrar,
     establecido por el usuario determine un rendimiento promedio"""

def principal():
        """metodo inicio programa
        Args: eleccion(int): Menú 
        """
        print("BIENVENIDO A LA HUERTA EN TUS MANOS")
        temporada=int(input("Por favor seleccione el N° de la temporada de la hortaliza a trabajar : \n"
        "1. PRIMAVERA- VERANO\n"
        "2. OTOÑO- INVIERNO\n"))
        return temporada


class Horticultura():

    def __init__(self, temporada, db) -> None:
        
        self.nombreEspecie=""
        self.familia=""
        self.temporada=temporada
        self.fechaSiembra=0
        self.fechaCosecha=0
        self.rendimiento=0
        self.variedad=0
        self.idVariedad=0
        self.db=db

    
    def setVariedad(self,cambioVar):
        self.variedad=cambioVar
        

    def setIdVariedad(self, id):
        self.idVariedad=id

    def getPrimaveraVerano(self):
        sql="SELECT idvariedad,nombreVariedad FROM variedad WHERE estacion=1"        
        resultados=self.db.obtenerResultados(sql)
        
        if resultados:
            print("------------------")
            print("Variedades Primavera-Verano")
            print("------------------")
            for variedades in resultados:
                print(variedades[0], variedades[1])
        else:
            print("No hay resultados de variedades en la base de datos")
        return ""
       

    def getOtonoInvierno(self):
        sql=("SELECT idvariedad,nombreVariedad FROM variedad WHERE estacion=2")
        resultados=self.db.obtenerResultados(sql)
        
        if resultados:
            print("------------------")
            print("Variedades Otoño-Invierno")
            print("------------------")
            for variedades in resultados:
                print(variedades[0], variedades[1])
        else:
            print("No hay resultados de variedades en la base de datos")
        return ""
        
    
    
    def getTemporada(self):
        return self.temporada
       
    
    def variedadHortaliza(self,param):
        """función que trae listado de variedades
            Args: eleccion(int): variedades
            """

        if param==1:
            valor=int(input(f"Seleccione el n° de la variedad a trabajar: {self.getPrimaveraVerano()}\n"))
            sql="SELECT nombreVariedad FROM variedad WHERE idvariedad="+str(valor)
            valores=self.db.obtenerResultados(sql)
            
            if valores:            
                   for i in valores:
                    self.variedad=i
            self.setIdVariedad(valor)        
            print("------------------")
            

        elif param==2:
            valor=int(input(f"Seleccione el n° la variedad a trabajar: {self.getOtonoInvierno()}\n"))
            sql="SELECT nombreVariedad FROM variedad WHERE idvariedad="+str(valor)
            valores=self.db.obtenerResultados(sql)
            
            if valores:            
                   for i in valores:
                    self.variedad=i
            self.setIdVariedad(valor)        
            print("------------------")

    
    def menuLabores(self):
        """función que muestra menú labores
        Args: eleccion(int): Menú 2
        """

        def solicitudFecha():
            print("Cargue la fecha para la labor a realizar:\n")
            dia=int(input("Dia(dd): "))
            mes=int(input("Mes(mm): "))
            agno=int(input("Año(yyyy)): "))
            fecha=datetime.date(agno, mes, dia)
            
            return fecha

        def solicitudParcela():
            print("------------------")
            print("LOTE A TRABAJAR:")
            print("------------------")
            sql=("SELECT idParcela, parcela FROM  parcela")
            valores=self.db.obtenerResultados(sql)
            for parcela in valores:
                    print(parcela[0], parcela[1])
            lote=int(input("Seleccione lote: "))
            
            return lote

        def consultaSQL():
            sql=("INSERT INTO labores(variedad, actividad, fecha, parcela) VALUES (%s,%s,%s,%s)")
            datos=(self.idVariedad, labor,solicitudFecha(),solicitudParcela())
            self.db.ejecutarConsultas(sql,datos)
            
                   
        while True:
            print("------------------")
            print("LABORES")
            print("------------------")
        
            sql=("SELECT idActividad, actividades FROM actividad")
            valores=self.db.obtenerResultados(sql)
            if valores:
                for labores in valores:
                    print(labores[0], labores[1])
            else:
                print("No hay resultados de actividades en la base de datos")
            
            
            labor=int(input("Seleccione el n° de la labor a realizar, o presione 7 para volver al menú anterior:\n"))
           
            
            if labor==1:
                print("Preparación del Suelo")                             
                print("------------------")
                consultaSQL()               
                print("Datos cargados con éxito")
            if labor==2:
                print("Siembra")
                print("------------------")
                consultaSQL()
                print("Datos cargados con éxito")
            if labor==3:
                print("Raleo")
                print("------------------")
                consultaSQL()
                print("Datos cargados con éxito")
            if labor ==4:
                print("Abono")
                print("------------------")
                consultaSQL()
                print("Datos cargados con éxito")
            if labor ==5:
                print("Cosecha")
                print("------------------")
                consultaSQL()
                print("Datos cargados con éxito")
            if labor==6:
                print("Riego")
                consultaSQL()
                print("Datos cargados con éxito")
            if labor==7:   
                break
        
  
    def menuDecision(self):
        """función que muestra accion a realizar
        Args: eleccion(int): Menú 
        """
        print("------------------")
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
                print("     Aqui se calcula el rendimiento promedio del cultivo de: ", self.variedad)
                print("------------------")
            elif opcionMenu2==3:
                print("     Características del cultivo de: ", self.variedad)
                sql=("""SELECT variedad.nombreVariedad, familia.familia, variedad.resistenciaHeladas, 
                estacion.estacion, variedad.produccionXMcuadKG
                FROM variedad, familia, estacion
                WHERE variedad.familia = familia.idfamilia
                AND	variedad.estacion = estacion.idEstacion
                AND variedad.idvariedad="""+str(self.idVariedad))
                valores=Database.ejecutarConsultas(sql)
                print("--------------------------------------------------------------")  
                print("  Variedad  Familia   ResistHelada  Estacion    ProducXMCuadKg")
                print("--------------------------------------------------------------")                
                for i in valores:
                    print(i)
                print("------------------")
                print("Labores realizadas en el cultivo de :", self.variedad )
                print("--------------------------------------------------------------") 
                sql=("""SELECT actividad.actividades, labores.fecha, parcela.parcela
                FROM actividad, labores, parcela
                WHERE actividad.idActividad=labores.actividad AND labores.parcela=parcela.idParcela 
                AND labores.variedad=""" +str(self.idVariedad)) +"""ORDER BY labores.fecha DESC"""
                valores=Database.ejecutarConsultas(sql)
                if valores.rowcount==0:
                    print("La variedad no tiene labores realizadas")
                else:
                    for i in valores:
                        print(i)
                print("--------------------------------------------------------------") 
            elif opcionMenu2==4:
                self.getOtonoInvierno()
                self.getPrimaveraVerano()
                print("------------------")
            elif opcionMenu2==5:              
               self.variedadHortaliza(principal())
            elif opcionMenu2==6:
                self.db.cerrarConexion()              
                break
                
            








