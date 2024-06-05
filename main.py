from database import Database
from huertaValoracion2 import Horticultura

"""Programa para gestionar la BD e iniciar objetos
de la clase huertaValoracion2"""


def main():

    def principal():
        """metodo inicio programa
        Args: eleccion(int): Menú 
        """
        print("BIENVENIDO A LA HUERTA EN TUS MANOS")
        temporada=int(input("Por favor seleccione el n° de la temporada de la hortaliza a trabajar : \n"
        "1. PRIMAVERA- VERANO\n"
        "2. OTOÑO- INVIERNO\n"))
        return temporada
    
    db=Database("localhost", 3306,"root","root","huerta")  
    huerta1=Horticultura(principal(),db)
    huerta1.variedadHortaliza(huerta1.getTemporada())
    huerta1.menu2()
    


if __name__=="__main__":
    main()

    
    
