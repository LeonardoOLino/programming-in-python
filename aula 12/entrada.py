def receber_notas():
    notas = []
    qtd = int(input('quantos alunos deseja cadastrar? '))

    for i in range(qtd):
        while True:
            try:
                nota = float(input(f'Digite a nota do aluno {i+1}: '))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print('Nota invalida! Digite entre 0 e 10')
            except ValueError:
                print ('Digite um numero valido. ')

    return notas