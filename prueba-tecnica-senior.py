from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

libros = []
id_counter = 1

def obtener_libro(libro_id):
	return next((libro for libro in libros if libro['id'] == libro_id), None)

class Libro(Resource):
    def get(self, libro_id):
        libro = obtener_libro(libro_id)
        if libro:
            return libro, 200
        return {'message': 'Libro no encontrado'}, 404

    def put(self, libro_id):
        parser = reqparse.RequestParser()
        parser.add_argument('título', type=str, required=True, help='Título no puede estar vacío')
        parser.add_argument('autor', type=str, required=True, help='Autor no puede estar vacío')
        parser.add_argument('año', type=int, required=True, help='Año no puede estar vacío')
        data = parser.parse_args()
        
        libro = obtener_libro(libro_id)
        if libro:
            libro.update(data)
            return libro, 200
        
        return {'message': 'Libro no encontrado'}, 404

    def delete(self, libro_id):
        global libros
        libros = [libro for libro in libros if libro['id'] != libro_id]
        return '', 204

class LibroList(Resource):
    def get(self):
        return libros, 200
    
    def post(self):
        global id_counter
        parser = reqparse.RequestParser()
        parser.add_argument('título', type=str, required=True, help='Título no puede estar vacío')
        parser.add_argument('autor', type=str, required=True, help='Autor no puede estar vacío')
        parser.add_argument('año', type=int, required=True, help='Año no puede estar vacío')
        data = parser.parse_args()

        libro = {
        	'id': id_counter,
        	'título': data['título'],
        	'autor': data['autor'],
        	'año': data['año']
    	}
        libros.append(libro)
        id_counter += 1
        return libro, 201

api.add_resource(LibroList, '/libros')
api.add_resource(Libro, '/libros/<int:libro_id>')

if __name__ == '__main__':
	app.run(debug=True)

#Ejercicio 2


#### Optimización

#1. **Consulta 1:**
"""
   CREATE INDEX idx_customer_id_order_date ON orders (customer_id, order_date);
   SELECT * FROM orders WHERE customer_id = 1 ORDER BY order_date;
"""

#  **Explicación:** Creación de un índice compuesto en `customer_id` y `order_date` para acelerar la búsqueda y ordenación de las órdenes de un cliente específico.

#2. **Consulta 2:**
"""
   CREATE INDEX idx_price ON products (price);
   SELECT * FROM products WHERE price > 100;
"""

#  **Explicación:** Creación de un índice en la columna `price` para acelerar la búsqueda de productos con precio mayor a 100.

#3. **Consulta 3:**
"""
   CREATE INDEX idx_department_salary ON employees (department_id, salary);
   SELECT * FROM employees WHERE department_id = 2 AND salary > 50000;
"""

#   **Explicación:** Creación de un índice compuesto en `department_id` y `salary` para acelerar la búsqueda de empleados en un departamento específico con un salario mayor a 50,000.


### Ejercicio 3: Procesamiento de Datos con Pandas

#### Código de Ejemplo

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv('dataset.csv')

# Limpieza básica
df.dropna(inplace=True)
df['columna_numerica'] = pd.to_numeric(df['columna_numerica'], errors='coerce')

# Estadísticas descriptivas
estadisticas = df.describe()
print(estadisticas)

# Visualizaciones
plt.figure(figsize=(10, 6))
sns.histplot(df['columna_numerica'], kde=True)
plt.title('Histograma de columna_numerica')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x=df['columna_numerica'])
plt.title('Boxplot de columna_numerica')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='categoria', y='columna_numerica', data=df)
plt.title('Gráfico de barras de columna_numerica por categoria')
plt.show()

### Ejercicio 4: Algoritmo de Machine Learning

#### Código de Ejemplo

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Cargar datos
iris = load_iris()
X, y = iris.data, iris.target

# Preprocesamiento
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# División de datos
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Entrenamiento del modelo
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predicciones
y_pred = clf.predict(X_test)

# Evaluación
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))