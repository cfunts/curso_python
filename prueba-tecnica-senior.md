# Python Prueba Técnica para Desarrollador Senior 

### Instrucciones
- Completa cada uno de los siguientes ejercicios.
- Asegúrate de que tu código sea claro, comentado y siga buenas prácticas de programación.
- Sube tu solución a un repositorio de GitHub y comparte el enlace.

---

## Ejercicio 1: API RESTful con Flask

Desarrolla una API RESTful usando Flask para gestionar un sistema de biblioteca. La API debe tener las siguientes características:
- Endpoints para CRUD (Crear, Leer, Actualizar, Eliminar) de libros.
- Cada libro debe tener los siguientes campos: `id`, `título`, `autor`, `año`.
- Implementa validación de datos para asegurar que los datos de los libros sean válidos.

### Requisitos
1. Instala Flask y Flask-RESTful.
2. Crea un archivo `app.py` que contenga la implementación de la API.
3. Usa una estructura de directorios adecuada para el proyecto.

## Ejercicio 2: Optimizador de Consultas SQL

Optimiza las siguientes consultas SQL. Explica las optimizaciones realizadas y justifica por qué son necesarias. Supón que trabajas con una base de datos PostgreSQL.

#### Consultas a Optimizar

1. sql
   SELECT * FROM orders WHERE customer_id = 1 ORDER BY order_date;


1. sql
   SELECT * FROM products WHERE price > 100;
   
3. sql
   SELECT * FROM employees WHERE department_id = 2 AND salary > 50000;

## Ejercicio 3: Procesamiento de Datos con Pandas

Descarga un conjunto de datos desde [Kaggle](https://www.kaggle.com/) y realiza el siguiente análisis utilizando Pandas:
- Carga el conjunto de datos.
- Realiza una limpieza básica de datos (manejo de valores nulos, corrección de tipos de datos, etc.).
- Calcula estadísticas descriptivas (media, mediana, moda, desviación estándar) para las columnas numéricas.
- Genera visualizaciones básicas (gráficos de barras, histograma, boxplot) para analizar la distribución de los datos.

## Ejercicio 4: Algoritmo de Machine Learning

Desarrolla un modelo de clasificación usando Scikit-Learn. Utiliza el conjunto de datos Iris para entrenar y evaluar el modelo. El modelo debe incluir:
- Preprocesamiento de datos.
- División del conjunto de datos en entrenamiento y prueba.
- Entrenamiento de un modelo de clasificación (por ejemplo, k-NN, SVM, Random Forest).
- Evaluación del modelo usando métricas apropiadas (precisión, recall, F1-score).
