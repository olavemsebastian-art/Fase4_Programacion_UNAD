from datetime import datetime
from servicio import Servicio, DatoInvalidoError, registrar_error
from cliente import Cliente

class ReservaError(Exception):
    pass

class Reserva:

    def __init__(self, cliente, servicio, duracion):
        try:
            if not isinstance(cliente, Cliente):
                raise ReservaError("Cliente inválido")

            if not isinstance(servicio, Servicio):
                raise ReservaError("Servicio inválido")

            if duracion <= 0:
                raise ReservaError("Duración debe ser mayor a 0")

            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion
            self.estado = "pendiente"
            self.fecha = datetime.now()

        except Exception as e:
            registrar_error(str(e))
            raise

    def confirmar(self):
        try:
            if self.estado != "pendiente":
                raise ReservaError("La reserva no se puede confirmar")

            self.estado = "confirmada"
            print("✅ Reserva confirmada")

        except Exception as e:
            registrar_error(str(e))
            print(e)

    def cancelar(self):
        try:
            if self.estado == "cancelada":
                raise ReservaError("La reserva ya está cancelada")

            self.estado = "cancelada"
            print("❌ Reserva cancelada")

        except Exception as e:
            registrar_error(str(e))
            print(e)

    def calcular_total(self):
        try:
            total = self.servicio.calcular_costo()
            return total

        except Exception as e:
            registrar_error(str(e))
            print(e)

    def mostrar_reserva(self):
        try:
            print("----- RESERVA -----")
            print(f"Cliente: {self.cliente.nombre}")
            print(f"Servicio: {self.servicio.describir_servicio()}")
            print(f"Estado: {self.estado}")
            print(f"Fecha: {self.fecha}")
            print(f"Total: {self.calcular_total()}")

        except Exception as e:
            registrar_error(str(e))
            print(e)
