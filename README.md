# Sistema Integral de Gestión de Clientes, Servicios y Reservas

## Descripción General

El presente proyecto fue desarrollado para la Fase 4 del curso Programación de la Universidad Nacional Abierta y a Distancia (UNAD). El sistema simula la gestión de clientes, servicios y reservas para la empresa Software FJ, utilizando Programación Orientada a Objetos en Python sin emplear bases de datos.

La aplicación fue diseñada aplicando conceptos de abstracción, encapsulación, herencia y polimorfismo, además de incorporar manejo avanzado de excepciones para garantizar estabilidad y control de errores durante la ejecución del sistema.

---

# Objetivos del Proyecto

- Implementar un sistema orientado a objetos funcional.
- Gestionar clientes, servicios y reservas.
- Aplicar excepciones personalizadas y validaciones.
- Registrar errores y eventos en archivos log.
- Fortalecer el trabajo colaborativo mediante GitHub.

---

# Estructura del Proyecto

## cliente.py

Contiene la clase Cliente, encargada de registrar y validar la información de los usuarios del sistema.

### Funcionalidades:
- Validación de nombre.
- Validación de documento.
- Validación de correo electrónico.
- Registro de errores en log.txt mediante excepciones.

---

## servicio.py

Archivo principal de servicios del sistema.

### Incluye:

### Clase abstracta Servicio
Define los métodos obligatorios:
- calcular_costo()
- describir_servicio()

### Excepciones personalizadas
- softwareFJError
- DatoInvalidoError

### Función registrar_error()
Permite guardar errores en el archivo log.txt con fecha y hora.

---

# Clases derivadas

## ReservaSala
Gestiona reservas de salas según cantidad de horas.

### Funcionalidades:
- Cálculo de costos.
- Validación de horas.
- Aplicación de descuentos.

---

## AlquilerEquipo
Permite administrar alquileres de equipos tecnológicos.

### Funcionalidades:
- Cálculo por días.
- Validaciones de tiempo.
- Manejo de excepciones.

---

## Asesoria
Gestiona asesorías especializadas.

### Funcionalidades:
- Registro de especialista.
- Cálculo por horas.
- Validación de parámetros.

---

## reserva.py

Administra el proceso de reservas.

### Funcionalidades:
- Confirmar reservas.
- Cancelar reservas.
- Calcular costos.
- Validar duración.
- Relacionar clientes con servicios.
- Registrar errores automáticamente.

---

## log.txt

Archivo encargado de almacenar:
- errores del sistema
- eventos relevantes
- excepciones detectadas

---

# Conceptos Aplicados

Durante el desarrollo del sistema se implementaron:

- Programación Orientada a Objetos
- Herencia
- Polimorfismo
- Encapsulación
- Abstracción
- Manejo avanzado de excepciones
- Uso de clases abstractas
- Registro de logs
- Validación de datos

---

# Manejo de Excepciones

El sistema incorpora:

```python
try:
except:
else:
finally:
