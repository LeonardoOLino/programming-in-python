##Exercício 1:
##Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

try:
    numero = int(input('Digite um numero: '))
    print (numero)
except ValueError:
    print('ERRO... digite um numero inteiro')




##Exercício 2:
##Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

try:
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite o numero: '))
    print(n1 / n2)
except ZeroDivisionError:
    print('ERRO NAO DIVISIVEL')



##Exercício 3:
##Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

lista = ['mqueen', 'marty', 'cely', 'Roger']
try:
    index = int(input('Digite um indice da lista(0 - 3): '))
    print('indice', index, ":", lista [index])

except IndexError:
    print('ERRO... local vazio')
except ValueError:
    print('ERRO.. nao tem esse indice')