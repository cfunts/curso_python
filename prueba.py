#EJERCICIO 6
"""#The sum of the squares of the first ten natural numbers is,
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

#print(suma_cuadrados)  # Salida esperada: 3025
#print(cuadrado_de_la_suma)  # Salida esperada: 385
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
"""

#EJERCICIO 7 - Encontrar el n-ésimo primo
"""    Puntos Importantes del Ejercicio:

    Definición del Problema: Encontrar el 10,001er número primo.
    Secuencia de Primos Iniciales: Los primeros seis primos son 2,3,5,7,11 y 13. 13 es el sexto primo
    Enfoque de Solución: Utilizar un método eficiente para generar números primos, 
    como el Criba de Eratóstenes o un método iterativo con verificaciones de divisibilidad.

    Explicación del Código

    Función es_primo(n): Verifica si un número es primo.
        Descarta números menores o iguales a 1.
        Comprueba divisibilidad por 2 y 3.
        Utiliza un bucle para verificar divisibilidad hasta la raíz cuadrada del número.

    Función find_nth_prime(n): Encuentra el n-ésimo primo.
        Inicializa un contador y un número.
        Incrementa el número y verifica si es primo.
        Incrementa el contador si se encuentra un primo.
        Retorna el n-ésimo primo.
    

def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def encuentra_enesimo_primo(n):
    contador = 0
    numero = 1
    while contador < n:
        numero += 1
        if es_primo(numero):
            contador += 1
    return numero

primo_10001 = encuentra_enesimo_primo(10001)
print(f"El 10,001er número primo es: {primo_10001}")

primo_6 = encuentra_enesimo_primo(6)
print(f"El sexto número primo es: {primo_6}")
"""

#EJERCICIO 8 - El número de 1000 dígitos como una sola cadena
"""def encuentraElMaxProducto(numero, digitos_adyacentes):
    # Convertir la cadena en una lista de enteros
    digitos = [int(char) for char in numero]
    
    max_producto = 0
    
    # Iterar sobre todos los posibles segmentos de `digitos_adyacentes` dígitos
    for i in range(len(digitos) - digitos_adyacentes + 1):
        # Obtener los `digitos_adyacentes` dígitos actuales
        segmento = digitos[i:i + digitos_adyacentes]
        # Calcular el producto de estos `adjacent_digits` dígitos
        producto = 1
        for digito in segmento:
            producto *= digito
        # Actualizar el máximo producto si es necesario
        if producto > max_producto:
            max_producto = producto
    
    return max_producto

# El número de 1000 dígitos como una sola cadena
numero = (
    "73167176531330624919225119674426574742355349194934"
    "96983520312774506326239578318016984801869478851843"
    "85861560789112949495459501737958331952853208805511"
    "12540698747158523863050715693290963295227443043557"
    "66896648950445244523161731856403098711121722383113"
    "62229893423380308135336276614282806444486645238749"
    "30358907296290491560440772390713810515859307960866"
    "70172427121883998797908792274921901699720888093776"
    "65727333001053367881220235421809751254540594752243"
    "52584907711670556013604839586446706324415722155397"
    "53697817977846174064955149290862569321978468622482"
    "83972241375657056057490261407972968652414535100474"
    "82166370484403199890008895243450658541227588666881"
    "16427171479924442928230863465674813919123162824586"
    "17866458359124566529476545682848912883142607690042"
    "24219022671055626321111109370544217506941658960408"
    "07198403850962455444362981230987879927244284909188"
    "84580156166097919133875499200524063689912560717606"
    "05886116467109405077541002256983155200055935729725"
    "71636269561882670428252483600823257530420752963450"
)

# Buscar el mayor producto de 13 dígitos adyacentes
maxProducto = encuentraElMaxProducto(numero, 13)
print(maxProducto)


maxProducto1 = encuentraElMaxProducto(numero, 4)
print(maxProducto1)"""

#EJERCICIO 9 - 