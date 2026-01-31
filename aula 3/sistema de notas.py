print('SISTEMA DE NOTAS')
print('....' * 8)
nome_aluno = input('Nome do aluno:')

n1_port = float(input('Nota Portugues: '))
n2_mat = float(input('Nota Matematica: '))
n3_ing = float(input('Nota Ingles: '))

media = (n1_port + n2_mat + n3_ing)/3

print('SITUAÇAO DO ALUNO: ')
aprovado = media > 7
reprovado = media< 5
recuperacao = media >=5 and media <7
print(nome_aluno, 'Aprovado?', aprovado)
print(nome_aluno,'Reprovado?', reprovado)
print(nome_aluno,'Recuperaçao?', recuperacao)
