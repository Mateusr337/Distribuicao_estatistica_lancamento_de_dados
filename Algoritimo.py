import numpy as np
import random as rand
import matplotlib.pyplot as plt

def lançamentosDados(n):
    x1 = np.array([rand.randint(1, 6) for i in range(n)])  # gerando numeros aleatórios em x1 lista n vezes.
    x2 = np.array([rand.randint(1, 6) for i in range(n)])  # gerando numeros aleatórios em x2 lista n vezes.
    y = x1 + x2  # possivelmente apenas com array's.
    return y

def média(y): #minha média
    soma = float(0)
    for i in range(len(y)):
        soma += y[i]
    return float(soma/len(y))

def desvio(m, y): #meu desvio
    soma = 0
    for i in range(len(y)):
        soma += float((y[i]-m)**2)
    d = (soma/len(y))**0.5
    return d

N=100000 #quanto maior o n maior o número de lançamentos
Y = lançamentosDados(N) #lista com os valores das somas dos dados.
média = média(Y)
desvio = desvio(média, Y)

print(f"Minha média = {média}, meu desvio = {desvio}")
print(f"Média da biblioteca numpy = {np.mean(Y)}, desvio da bibliotéca numpy = {np.std(Y)}")

cont = (np.zeros(11)) #gerando uma lista com 6 numeros iguais a zero
for i in Y:
    cont[i-2] += 1
print(f"A contagem de cada número de 2 a 12 em ordem é = {cont}")

numeros = np.arange(2,13)
plt.bar(numeros, cont)
plt.title("Lançamento De Dois Dados")
plt.xlabel("Combinção numérica")
plt.ylabel("Repetições")
plt.show()
plt.savefig('Histograma Tarefa 7', format='png')
