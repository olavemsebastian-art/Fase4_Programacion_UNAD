
from abc import ABC, abstractmethod
from datetime import datetime

#EXCEPCIONES PERSONALIZADAS
class softwareFJError(Exception):
    pass
class DatoInvalidoError(softwareFJError):
    pass

#FUNCION PARA GUARDAR ERRORES --log--
def registrar_error(mensaje):
    try:
       with open("log.txt","a")as archivo:
        fecha=datetime.now().strftime("%Y-%m-%d %h:%M:%S")
        archivo.write(f"[{fecha}]ERROR:{mensaje}\n")
    except Exception:
        print("No se puede escribir en el archivo log")
        
#CLASE ABASTRACTA 

class Servicio(ABC): 
    def __init__(self, nombre, precio_base):
        if not nombre or nombre.strip() =="":
            raise DatoInvalidoError("Servicio no puede estar vacio")
        if precio_base<= 0:
            raise DatoInvalidoError("precio base debe ser mayor a 0")
        
#ENCAPSULAMIETNO      

        self.nombre=nombre
        self.precio_base=precio_base
    
#METODOS PARA QUE OTRAS CLASES PUEDAN LEER NOMBRE Y PRECIO

    @property
    def nomnbre(self):
        return self.__nombre
    
    @property
    def precio_base(self):
        return self.__precio_base
    
    @abstractmethod
    def calcular_costo(self):
        pass
    
    @abstractmethod
    def describir_servicio(self):
        pass
    
    #CLASES HIJAS CON HERENCIA Y POLIMORFISMO
    #RESERVA
    
class ReservaSala(Servicio):
        def __init__(self, nombre, precio_base,horas):
            super().__init__(nombre, precio_base)
            if horas<=0:
                raise DatoInvalidoError("El tiempo en horas deber estar en positivo")
            self.__horas=horas
            
    #SOBRECARGA-- PERMITE CALCULAR CON O SIN DESCUENTO        
        def calcular_costo(self, descuento=0):
            total=self.precio_base*self.__horas
            return total-(total*descuento)
        
        def describir_servicio(self):
            return f"Reserva de sala por-{self.nombre} ({self.__horas} horas)"
        
    #ALQUILER DE EQUIPO
    
class AlquilerEquipo(Servicio):
        
        def __init__ (self,nombre,precio_base,dias):
            super().__init(nombre,precio_base)
            if dias<=0:
                raise DatoInvalidoError("el tiempo en dias debe ser positivo")
            self.__dias=dias
        
        def calcular_costo(self, descuento=0):
            total=self.precio_base*self.__dias
            return total-(total*descuento)
        
        
        def describir_serivicio(self):
            return f"servicio:Alquiler de equipo-{self.nombre}({self.__dias}dias)"
        
   #ASESORIA
   
class Asesoria(Servicio):
        
        def __init__(self,nombre,precio_base, horas, especialista):
            super().__init(nombre, precio_base)
            if horas<=0:
                raise DatoInvalidoError("las horas de asesoria deben ser positivas")
            self.__horas=horas
            self.__especialista=especialista
            
        def calcular_costo(self, descuento=0):
            total=self.precio_base*self.__horas
            return total -(total*descuento)
        
        def describir_servicio(self):
            return f"Servicio:Asesoria Especializada con {self.__especialista}({self.__horas}horas)"
        
