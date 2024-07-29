### Ejercicio 1: Generador de Números Primos

def generador_primos():
	"""
	Generador infinito de números primos.
    
	Yields:
    	int: El siguiente número primo.
	"""
	def es_primo(n):
		if n < 2:
			return False
		for i in range(2, int(n**0.5) + 1):
			if n % i == 0:
				return False
		return True

	num = 2
	while True:
		if es_primo(num):
			yield num
		num += 1

# Prueba
gen = generador_primos()
for _ in range(10):
	print(next(gen))  # Salida esperada: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

### Ejercicio 2: Analizador de Archivos CSV

import csv

class CSVAnalyzer:
	def __init__(self, filename):
		self.filename = filename
		self.data = []
    
	def read_csv(self):
		with open(self.filename, mode='r') as file:
			csv_reader = csv.DictReader(file)
			self.data = [row for row in csv_reader]
    
	def get_column(self, column_name):
		return [row[column_name] for row in self.data if column_name in row]
    
	def get_unique_values(self, column_name):
		return set(self.get_column(column_name))

# Prueba
csv_analyzer = CSVAnalyzer('archivo_prueba.csv')
csv_analyzer.read_csv()
print(csv_analyzer.get_column('Nombre'))  # Salida esperada: Lista de nombres de la columna 'Nombre'
print(csv_analyzer.get_unique_values('Edad'))  # Salida esperada: Conjunto de edades únicas de la columna 'Edad'

### Ejercicio 3: Sistema de Gestión de Tareas


class TaskManager:
	def __init__(self):
		self.tasks = []
		self.next_id = 1
    
	def add_task(self, nombre, descripcion):
		task = {
        	'id': self.next_id,
        	'nombre': nombre,
        	'descripcion': descripcion,
        	'completada': False
    	}
		self.tasks.append(task)
		self.next_id += 1
    
	def remove_task(self, task_id):
		self.tasks = [task for task in self.tasks if task['id'] != task_id]
    
	def complete_task(self, task_id):
		for task in self.tasks:
			if task['id'] == task_id:
				task['completada'] = True
    
	def get_all_tasks(self):
		return self.tasks
    
	def get_pending_tasks(self):
		return [task for task in self.tasks if not task['completada']]

# Prueba
manager = TaskManager()
manager.add_task('Tarea 1', 'Descripción de la tarea 1')
manager.add_task('Tarea 2', 'Descripción de la tarea 2')
print(manager.get_all_tasks())  
# Salida esperada: Lista con las dos tareas añadidas
manager.complete_task(1)
print(manager.get_pending_tasks())  
# Salida esperada: Lista con la tarea 2
manager.remove_task(2)
print(manager.get_all_tasks())  
# Salida esperada: Lista con la tarea 1


### Ejercicio 4: Decorador para Medir Tiempo de Ejecución


import time

def medir_tiempo(func):
	"""
	Decorador que mide el tiempo de ejecución de una función.
    
	Args:
    	func (callable): La función a medir.
    
	Returns:
    	callable: La función decorada con medición de tiempo.
	"""
	def wrapper(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		end_time = time.time()
		elapsed_time = end_time - start_time
		print(f"Tiempo de ejecución de {func.__name__}: {elapsed_time:.4f} segundos")
		return result
	return wrapper

# Prueba
@medir_tiempo
def prueba():
	for _ in range(1000000):
		pass

prueba()
# Salida esperada: Tiempo de ejecución de prueba: X.XXXX segundos
