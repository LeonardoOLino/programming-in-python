###***1: Verificando se o número é par ou ímpar***

numero = int(input('numero: '))

match numero:
    case numero if numero % 2 == 0:
        print('Par')
    case _:
        print('impar')


###***2: Verificando se um número é positivo, negativo ou zero***
num = int(input('numero: '))

match num:
    case num if num > 0:
        print('positivo')
    case num if num < 0:
        print('negativo')
    case _:
        print('é zero')

###***3: Verificando se uma string é vazia ou não***

string = input('Digite: ')

match string:
    case '':
        print('string vazia')
    case _:
        print('string n vazia')

###***4: Verificando se um número é maior, menor ou igual a 10***

num2 = int(input('numero: '))

match num2:
    case num2 if num2 > 10:
        print('é maior')
    case num2 if num2 < 10:
        print('é menor')
    case _:
        print('é 10')

###***5: Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)***


idade = int(input('sua idade: '))

match idade:
    case idade if idade <= 12:
        print('voce é criança')
    case idade if idade <= 17:
        print('voce é adolecente')
    case idade if idade <= 35:
        print('voce é jovem')
    case idade if idade <=64:
        print('voce é adulto')
    case _:
        print('voce é idoso')









