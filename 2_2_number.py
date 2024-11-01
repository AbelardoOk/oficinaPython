# Tipos Numéricos

num1 = 10
num2 = 9.9
num3 = 2j

print(type(num1))
# Saída: <class 'int'>
print(type(num2))
# Saída: <class 'float'>
print(type(num3))
# Saída: <class 'complex'>

print("\n")

# Randomizando números!
import random

# Gera um número aleatório entre 0 e 10!
print(random.randint(0,10))

print("\n")

# Conversão de tipos
num4 = 10
num4 = float(num4)

print(type(num4))
# Saída: <class 'float'>
print(num4)
# Saída: 10.0

print("\n")

# Operações aritméticas
print(10 + 9) #Soma
print(9 - 8) #Subtração
print(-9 * -9) # Multiplicação
print(10 / 3) # Divisão
print(10 // 3) # Parte inteira da divisão
print(10**2)  #Exponenciação
print(10 % 2) #Resto da divisão