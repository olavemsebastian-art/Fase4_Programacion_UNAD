class Cliente:
    def __init__(self, nombre, documento, correo):
        # 1. Validaciones: Si algo está mal, lanzamos el error de inmediato
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")

        if not documento or documento.strip() == "":
            raise ValueError("El documento no puede estar vacío")

        if "@" not in correo:
            raise ValueError("Correo inválido")

        # 2. Asignación: Solo se llega aquí si los datos son correctos
        self.nombre = nombre
        self.documento = documento
        self.correo = correo
