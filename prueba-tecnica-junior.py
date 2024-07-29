#Solución para el Ejercicio 1
def numeros_pares(numeros):
	"""
	Devuelve una lista de números pares de la lista de entrada.
    
	:param numeros: List[int] - Lista de números enteros
	:return: List[int] - Lista de números pares
	"""
	pares = [num for num in numeros if num % 2 == 0]
	return pares

# Prueba
lista_numeros = [1, 2, 3, 4, 5, 6]
print(numeros_pares(lista_numeros))  # Salida esperada: [2, 4, 6]

#Solución para el Ejercicio 2
def contador_palabras(texto):
	"""
	Cuenta la cantidad de veces que aparece cada palabra en un texto.
    
	:param texto: str - Cadena de texto
	:return: Dict[str, int] - Diccionario con las palabras y sus respectivas cantidades
	"""
	palabras = texto.split()
	contador = {}
	for palabra in palabras:
		palabra = palabra.lower().strip(".,!?")
		if palabra in contador:
			contador[palabra] += 1
		else:
			contador[palabra] = 1
	return contador

# Prueba
print(contador_palabras("Hola mundo! Hola a todos. Mundo mundo!"))  
# Salida esperada: {'hola': 2, 'mundo': 3, 'a': 1, 'todos': 1}

#Solución para el Ejercicio 3

def leer_archivo(nombre_archivo):
	"""
	Lee un archivo de texto y devuelve su contenido.
    
	:param nombre_archivo: str - Nombre del archivo a leer
	:return: str - Contenido del archivo
	"""
	with open(nombre_archivo, 'r') as archivo:
		contenido = archivo.read()
	return contenido

def escribir_archivo(nombre_archivo, contenido):
	"""
	Escribe una cadena de texto en un archivo.
    
	:param nombre_archivo: str - Nombre del archivo a escribir
	:param contenido: str - Contenido a escribir en el archivo
	"""
	with open(nombre_archivo, 'w') as archivo:
		archivo.write(contenido)

# Prueba
escribir_archivo('archivo_prueba.txt', 'Hola, este es un archivo de prueba.')
print(leer_archivo('archivo_prueba.txt'))  
# Salida esperada: 'Hola, este es un archivo de prueba.'

#Solución para el Ejercicio 4
class Persona:
	def __init__(self, nombre, edad, email):
		self.nombre = nombre
		self.edad = edad
		self.email = email
    
	def es_mayor_de_edad(self):
		return self.edad >= 18
    
	def __str__(self):
		return f"Nombre: {self.nombre}, Edad: {self.edad}, Email: {self.email}"

# Prueba
persona = Persona("Juan Pérez", 15, "juan.perez@example.com")
print(persona)  # Salida esperada: "Nombre: Juan Pérez, Edad: 25, Email: juan.perez@example.com"
print(persona.es_mayor_de_edad())  # Salida esperada: True
print(persona.__str__())
