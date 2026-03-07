#main.py

import meu_modulo as ml


for i in range(3):
    aleatorio = ml.atividade_1(5,11)
    print(aleatorio)


## 3 atividade

numero = ml.atividade_1(10, 31)
print(numero)

## 4 atividade

for u in range(10, 0, -1):
    print(u)

print('Fogo!')

## 5 atividade

s_numero = int(input('Insira um  numero inteiro positivo: '))
soma = 0 

for a in range (2, s_numero + 1, 2):
    soma += a

print(' a soma de todos os numeros pares é:', soma)