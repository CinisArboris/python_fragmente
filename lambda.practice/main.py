# Ejercicio 1: Multiplicar por 2
# Escribe una función lambda que tome un número y devuelva el doble de ese número.
fLambda = lambda num : num * 2
print('Ejercicio 1 : Multiplicar por 2 (10)::', fLambda(10))
print('Ejercicio 1 : Multiplicar por 2 (11)::', fLambda(11))
print('Ejercicio 1 : Multiplicar por 2 (12)::', fLambda(12))

# Ejercicio 2: Números pares
# Escribe una función lambda que tome un número y devuelva True si es par, y False si es impar.
fLambda = lambda num : num % 2 == 0
print('Ejercicio 2 : Números pares (10)::', fLambda(10))
print('Ejercicio 2 : Números pares (11)::', fLambda(11))
print('Ejercicio 2 : Números pares (12)::', fLambda(12))

# Ejercicio 3: Potencia de un número
# Escribe una función lambda que tome dos números base y exponente, y devuelva la base elevada al exponente.
fLambda = lambda bas, exp : bas ** exp
print('Ejercicio 3 : Potencia de un número (2,4)::', fLambda(2,4))
print('Ejercicio 3 : Potencia de un número (3,2)::', fLambda(3,2))
print('Ejercicio 3 : Potencia de un número (5,3)::', fLambda(5,3))