# Python Prueba Técnica para Desarrollador Intermedio

### Instrucciones
- Completa cada uno de los siguientes ejercicios.
- Asegúrate de que tu código sea claro, comentado y siga buenas prácticas de programación.
- Sube tu solución a un repositorio de GitHub y comparte el enlace.

## Ejercicio 1: Generador de Números Primos

Escribe una función generadora que produzca números primos indefinidamente.

## Ejercicio 2: Analizador de Archivos CSV

Escribe una clase `CSVAnalyzer` que pueda leer y analizar archivos CSV. La clase debe tener los siguientes métodos:
- `__init__(self, filename)`: Constructor que inicializa con el nombre del archivo.
- `read_csv(self)`: Lee el archivo CSV y almacena los datos en una lista de diccionarios.
- `get_column(self, column_name)`: Devuelve una lista con todos los valores de una columna específica.
- `get_unique_values(self, column_name)`: Devuelve un conjunto con los valores únicos de una columna específica.

## Ejercicio 3: Sistema de Gestión de Tareas

Escribe una clase `TaskManager` que gestione una lista de tareas. Cada tarea debe ser un diccionario con las claves `id`, `nombre`, `descripcion` y `completada`. La clase debe tener los siguientes métodos:
- `add_task(self, nombre, descripcion)`: Añade una nueva tarea con un ID único.
- `remove_task(self, task_id)`: Elimina una tarea por su ID.
- `complete_task(self, task_id)`: Marca una tarea como completada por su ID.
- `get_all_tasks(self)`: Devuelve una lista de todas las tareas.
- `get_pending_tasks(self)`: Devuelve una lista de las tareas pendientes.

## Ejercicio 4: Decorador para Medir Tiempo de Ejecución

Escribe un decorador `@medir_tiempo` que mida y muestre el tiempo de ejecución de una función.
