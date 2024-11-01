frutas = ['abacaxi', 'banana', 'maçã']

print(frutas)
# Saída: ['abacaxi', 'banana', 'maçã']

# Acessando dados

print(frutas[1])
# Saída: ['banana']

# Matrizes
lista = [['Pessoa1', 'Pessoa2', 'Pessoa3'], [1, 2, 3]]

print(lista[0][1])
# Saída: Pessoa2

print("\n")

#Métodos

listaLinguagens = ['python', 'javascript']
listaNum = [40, 38, 120, 87, 2, 17, 38]

# Append => Adicionar um dado ao final da lista
lista.append('java')

# Insert => Adicionar um novo dado de acordo com o índice
lista.insert(1, 'c')

# Remove => Remover um dado de acordo com o índice
lista.remove(1)

# Sort => Ordena a lista de forma crescente
listaNum.sort()

# Reverse => Inverte a lista
listaNum.reverse()

# Count => Número de vezes que um dado aparece na lista
print(listaNum.count(38))

