
from abc import ABC, abstractmethod
from datetime import datetime

# --- EXCEPCIONES PERSONALIZADAS ---
class softwareFJError(Exception):
    pass

class DatoInvalidoError(softwareFJError):
    pass

# --- FUNCIÓN PARA GUARDAR ERRORES (LOGS) ---
def registrar_error(mensaje):
    try:
        with open("log.txt", "a") as archivo:
            # %H:%M:%S para que la hora salga bien (24h)
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo.write(f"[{fecha}] ERROR: {mensaje}\n")
    except Exception:
        print("No se puede escribir en el archivo log")

# --- CLASE ABSTRACTA (MADRE) ---
class Servicio(ABC): 
    def __init__(self, nombre, precio_base):
        if not nombre or nombre.strip() == "":
            raise DatoInvalidoError("El nombre del servicio no puede estar vacío")
        if precio_base <= 0:
            raise DatoInvalidoError("El precio base debe ser mayor a 0")
        
        # Atributos privados (Encapsulamiento)
        self.__nombre = nombre
        self.__precio_base = precio_base

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precio_base(self):
        return self.__precio_base
    
    @abstractmethod
    def calcular_costo(self, descuento=0):
        pass
    
    @abstractmethod
    def describir_servicio(self):
        pass

# --- CLASES HIJAS (HERENCIA Y POLIMORFISMO) ---

# 1. RESERVA DE SALA
class ReservaSala(Servicio):
    def __init__(self, nombre, precio_base, horas, capacidad):
        super().__init__(nombre, precio_base)
        if horas <= 0:
            raise DatoInvalidoError("El tiempo en horas debe ser positivo")
        self.__horas = horas
        self.__capacidad = capacidad

    def calcular_costo(self, descuento=0):
        # Polimorfismo: Si la capacidad es mayor a 20, recargo del 10%
        total = self.precio_base * self.__horas
        if self.__capacidad > 20:
            total *= 1.10
        return total - (total * descuento)
    
    def describir_servicio(self):
        return f"SALA: {self.nombre} para {self.__capacidad} pers. ({self.__horas} hrs)"

# 2. ALQUILER DE EQUIPO
class AlquilerEquipo(Servicio):
    def __init__(self, nombre, precio_base, dias, marca):
        # Corregido: se agregaron los paréntesis () en super()
        super().__init__(nombre, precio_base)
        if dias <= 0:
            raise DatoInvalidoError("El tiempo en días debe ser positivo")
        self.__dias = dias
        self.__marca = marca

    def calcular_costo(self, descuento=0):
        # Polimorfismo: Alquiler simple por días
        total = self.precio_base * self.__dias
        return total - (total * descuento)
    
    def describir_servicio(self):
        return f"EQUIPO: {self.nombre} - Marca: {self.__marca} ({self.__dias} días)"

# 3. ASESORÍA ESPECIALIZADA
class Asesoria(Servicio):
    def __init__(self, nombre, precio_base, horas, especialista):
        # Corregido: se agregaron los paréntesis () en super()
        super().__init__(nombre, precio_base)
        if horas <= 0:
            raise DatoInvalidoError("Las horas de asesoría deben ser positivas")
        self.__horas = horas
        self.__especialista = especialista

    def calcular_costo(self, descuento=0):
        # Polimorfismo: Las asesorías tienen un cargo administrativo fijo de $5.000
        total = (self.precio_base * self.__horas) + 5000
        return total - (total * descuento)
    
    def describir_servicio(self):
        return f"ASESORÍA: {self.nombre} con {self.__especialista} ({self.__horas} hrs)"

