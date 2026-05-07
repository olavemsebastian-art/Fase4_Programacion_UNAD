class Reserva:
    def __init__(self, cliente, servicio, tiempo):
        self.cliente = cliente
        self.servicio = servicio
        self.tiempo = tiempo

    def procesar_reserva(self):
        # Usamos el método calcular_costo que definiste en Servicio
        total = self.servicio.calcular_costo()
        
        print("\n" + "="*40)
        print("         RECIBO DE RESERVA")
        print("="*40)
        print(f"CLIENTE:    {self.cliente.nombre}")
        print(f"DOCUMENTO:  {self.cliente.documento}")
        print(f"SERVICIO:   {self.servicio.describir_servicio()}")
        print("-" * 40)
        print(f"TOTAL A PAGAR: ${total:,.0f}")
        print("="*40 + "\n")