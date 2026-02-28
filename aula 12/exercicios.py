from colorama import Fore, Back, Style

# Exercícios com funções:
# variáveis locais, globais e parâmetros
# 1
# CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.

def comparar():
    n1 = float(input('Digite o numero: '))
    if n1 % 2 == 0:
        print("Numero é par")
    else:
        print('Numero é impar')
comparar ()

# 2
# CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.

def mult():
    n1 = float(input('Digite o numero: '))
    n2 = float(input('Digite o numero: '))
    n3 = float(input('Digite o numero: '))
    print(n1 * n2 * n3)
mult ()

# 3
# CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.

def elevado():
    n1 = float(input('Digite um numero para ser elevado a 2: '))
    print(n1 ** 2)
elevado()

# 4
# CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO DIGITAR, 18 ANOS.

def idade():
    idade1 = int(input('Digite sua idade: '))
    if idade1 > 18:
        print('Maior de idade')
    elif idade1 < 18:
        print('Menor de idade')
    else:
        print( Fore.RED + "PARABENSSS VOCE TA NO PONTO DE BALA" + Style.RESET_ALL)

idade()

# 5
# DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.
def ano():
    ano_nascimento = int(input('Digite o ano que vc nasceu: '))
    ano_atual = int(input("Digite o ano em que vc esta: "))
    print('Voce tem: ', ano_atual - ano_nascimento)

ano()

# 6
# DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.

def copa():
    pais = input('Qual pais vc acha que ganhou a copa america 1999: ')
    if pais == 'Brasil':
        print(Fore.GREEN + 'A seleçao n°1 '+ Style.RESET_ALL)
    else:
        print(Fore.RED + 'ISSO NEM É SELEÇAO' + Style.RESET_ALL)
copa()

# 7
# DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.

# 1 - Função - cumprimentar o cliente

def boas_vindas():
    nome = input('Digite seu nome: ')
    print('Seja bem vindo(a)', nome, 'ao nosso restaurante web')

boas_vindas()

# 2 - Função - restaurante
def restaurante():
    pratos = {

        "arroz e feijao": 30.00,
        'macarronada': 50.00,
        'strogonoff': 70.00

    }

    for prato, preco in pratos.items():
        print(f'{prato} - R$ {preco:.2f}')

    escolha = input('Digite o prato da sua escolha: ').lower()
    if escolha in pratos:
        print(f'Voce escolheu {escolha}, total a pagar: R$ {pratos[escolha]:.2f}')
    else:
        print('Prato n encontrado')
restaurante()

# 3 - Sugestão utilize listas e loops 