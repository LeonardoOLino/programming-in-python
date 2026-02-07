#exercicios

# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.
numero = int(input('digite um numero: '))
if numero >= 1:
  print ('numero positivo')
if numero == 0:
  print('Numero é zero')
if numero < 0:
  print('numero negativo')

# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.
idade = int(input('digite sua idade: '))
if idade >= 16:
  print("Faz o L")
else:
  print('bebezinho da mamae')

# 3*

# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.
par = list(range (2,21,2))
impar = list(range(1,21,2))

variavel = 20

if variavel % 2 == 0:
  print('numero é par')
else:
  print ('numero impar')



# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.
numero1 = float(input('Digite a primeira medida: '))
numero2 = float(input('Digite a segunda medida: '))
numero3 = float(input('Digite a terceira medida: '))

if numero1 == numero2 == numero3 == numero1:
  print('Isso é um triangulo equilatero')
elif numero1 != numero2 != numero3 != numero1:
 print('isso é um triangulo escaleni')
else:
  print('Isso é um triangulo isoceles')


# 5*

# Determine se um número é múltiplo de 5 e 7.
  
n = int(input('nº: '))

if n % 5 == 0 and n % 7 == 0:
   print(' multiplo')
else:
    print('nao multiplo')

# 6*

# Verifique se um número é positivo e maior que 10
n = int(input('Digite numero: '))

if n > 0 and n > 10:
 print('Posiivo e maior que 10!')
elif n > 0 and n < 10:
 print('positivo e menor que 10')
else:
 print('negativo e menor')
# 7*

# Verifique se um número é divisível por 3 ou 5.

n = int(input('nº'))

if n % 3  or n % 5:
  print('e divisivel')
else: 
 print('nao divisivel')