class Cliente:

    def __init__(self, nombre, documento, correo):
        try:
            if nombre == "":
                raise ValueError("El nombre no puede estar vacío")

            if documento == "":
                raise ValueError("El documento no puede estar vacío")

            if "@" not in correo:
                raise ValueError("Correo inválido")

            self.nombre = nombre
            self.documento = documento
            self.correo = correo

        except ValueError as error:
            with open("log.txt", "a") as archivo:
                archivo.write(str(error) + "\n")
            print(error)
