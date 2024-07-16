#EJERCICIO 6

#The sum of the squares of the first ten natural numbers is,
#  1**2 + 2**2 + ... + 10**2 = 385.

suma_cuadrados = sum(x**2 for x in range(1, 11))
print(suma_cuadrados)

#The square of the sum of the first ten natural numbers is,
#  (1 + 2 + ... + 10)**2 = 55**2 = 385.

cuadrado_de_la_suma = pow(sum(x for x in range(1, 11)),2)
print(cuadrado_de_la_suma)

#Hence the difference between the sum of the squares of the first ten natural numbers 
# and the square of the sum is 3025 - 385 = 2640.
diferencia = cuadrado_de_la_suma - suma_cuadrados

print(suma_cuadrados)  # Salida esperada: 3025
print(cuadrado_de_la_suma)  # Salida esperada: 385
print(diferencia)  # Salida esperada: 2640

print("---------------------------------------------------------------")

#Find the difference between the sum of the squares of the first one hundred natural numbers 
# and the square of the sum.
suma_cuadrados2 = sum(x**2 for x in range(1, 101))#101 para que tome hasta el 100
cuadrado_de_la_suma2 = pow(sum(x for x in range(1, 101)), 2)
diferencia2 = cuadrado_de_la_suma2 - suma_cuadrados2

print(f"La suma de los cuadrados de los primeros cien números naturales es: {suma_cuadrados2}")
print(f"El cuadrado de la suma de los primeros cien números naturales es: {cuadrado_de_la_suma2}")
print(f"La diferencia entre el cuadrado de la suma y la suma de los cuadrados es: {diferencia2}")

# suma_cuadrados2 Salida esperada: 338350
# cuadrado_de_la_suma2 Salida esperada: 25502500
# diferencia2 Salida esperada: 25164150