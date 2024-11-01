text1 = 'Olá Mundo';
text2 = "Great: o melhor grupo de alunos do IFMS"
text3 = """Nossa, bem grande essa string..."""

# Como realizar Concatenação?

text4 = "Python" + " é " + 'legal ' * 3 
print(text4)
# Saida: "Python é legal legal legal"

print('\n')

# Strings como Listas
py = "python"

print(py[1])
# Saída: 'y'
print(py[1:4])
# Saída: 'yth'
print(py[3:])
# Saída: 'hon'

print('\n')

# Métodos internos
text5 = "ifms mais que uma escola!"

print(len(text5))
# Saída: 25
print(text5.count("m"))
# Saída: 3
print(text5.count("m", 3,25))
# Saída: 2
print(py.upper())
# Saída: 'PYTHON'
print(py.lower())
# Saída: 'python'

print('\n')

text6 = "cueca123"
text7 = "cueca123%#"
text8 = "Brasil"

print(text6.isalnum())
# Saída: True
print(text7.isalnum())
# Saída: False
print(text8.replace("s","z"))
# Saída: Brazil
print(text8.split("as"))
# Saída: ['Br', 'il']