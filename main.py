from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria, registrar_error, DatoInvalidoError
from reserva import Reserva

def ejecutar_simulacion():
    print("SISTEMA DE GESTIÓN SOFTWARE FJ - EJECUTANDO...\n")

    # Lista de 10 pruebas
    pruebas = [
        ["S", "Alejandra", "1061", "aleja@mail.com", "Sala Juntas", 50000, 3, 25], # OK
        ["E", "Carlos", "2020", "carlos@mail.com", "Laptop", 15000, 2, "HP"],     # OK
        ["A", "Lucia", "3030", "lucia@mail.com", "Python", 40000, 1, "Ing. Juan"],# OK
        ["S", "", "4040", "error@mail.com", "Sala B", 10000, 2, 5],               # ERROR (Nombre vacío)
        ["E", "Pedro", "ABC", "p@mail.com", "Proyector", 5000, 1, "Epson"],        # ERROR (Doc no numérico)
        ["A", "Marta", "5050", "marta_mail.com", "Marketing", 20000, 3, "Dra. Rosa"],# ERROR (Correo mal)
        ["S", "Sofi", "6060", "s@mail.com", "Sala C", -100, 2, 10],               # ERROR (Precio negativo)
        ["E", "Andres", "7070", "a@mail.com", "Camara", 10000, 0, "Sony"],         # ERROR (Tiempo 0)
        ["S", "Diego", "8080", "d@mail.com", "Auditorio", 120000, 4, 60],         # OK
        ["A", "Elena", "9090", "e@mail.com", "Finanzas", 35000, 2, "CPA Ruiz"]    # OK
    ]

    exitos = 0
    errores = 0

    for i, p in enumerate(pruebas, 1):
        try:
            print(f"Operación #{i}:")
            # En tu clase Cliente las excepciones son ValueError
            # En tu clase Servicio son DatoInvalidoError
            
            cli = Cliente(p[1], p[2], p[3])
            # Si el cliente falla, el try saltará al except
            
            if p[0] == "S":
                serv = ReservaSala(p[4], p[5], p[6], p[7])
            elif p[0] == "E":
                serv = AlquilerEquipo(p[4], p[5], p[6], p[7])
            else:
                serv = Asesoria(p[4], p[5], p[6], p[7])
            
            res = Reserva(cli, serv, p[6])
            res.procesar_reserva()
            exitos += 1

        except Exception as e:
            registrar_error(str(e))
            print(f"❌ Error capturado: {e}\n" + "-"*30)
            errores += 1

    print(f"\nRESUMEN FINAL:")
    print(f"✅ Exitosas: {exitos}")
    print(f"❌ Errores: {errores}")

if __name__ == "__main__":
    ejecutar_simulacion()