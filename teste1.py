import random

def geradorCpf():
    cpf = []
    for i in range(11):
        cpf.append(str(random.randint(0,9)))

        if i == 2:
            cpf.append(".")
        elif i == 5:
            cpf.append(".")
        elif i == 8:
            cpf.append("-")

    cpfFinal = ''.join(cpf)
    return cpfFinal

cpf = geradorCpf()
print(cpf)