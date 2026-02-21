##Acesso a conta com condicionais

dados = {
'login':[],
'senha':[]
}

print('cadastre-se')
cad_login = input('Cadastre seu login: ')
cad_senha = input('Cadastre sua senha: ')
dados['login'].append(cad_login)
dados['senha'].append(cad_senha)


tentativas = 0

while tentativas < 3:
    acesso_login = input('login: ')
    acesso_senha = input('senha: ')
    


    if acesso_login in dados['login'] and acesso_senha in dados['senha'] :
        print('seja bem vindo(a) a atulizaçoes de alunos')
        

        ###- Inserir notas (se Senha correta)
        ###- Fazer a média
        dados = {
        'alunos' : [],
        'notas' : []
    }
        cad_aluno = input('Digite o nome do meliante: ')
        cad_nota1 = float(input('Digie a nota do meliante: '))
        cad_nota2 = float(input('Digie a nota do meliante: '))
        cad_nota3 = float(input('Digie a nota do meliante: '))
        dados['alunos'].append(cad_aluno)
        dados['notas'].extend([cad_nota1, cad_nota2, cad_nota3])
        media = sum(dados['notas'])/len(dados['notas'])
        print('a media do vagabundo', dados['alunos'], 'é', media)




    ###- Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)
    else:
        print('Digitaçao de senha ou login incorreto')
        print ('Faça novamente')
        tentativas += 1
        print(f'voce ainda tem {3 - tentativas} tentativa(s).\n')

    if tentativas == 3:
        print('Voce excedeu o limite de tentativas acesso negado')



input('Digite enter para sair: ')
# input(’Digite enter para sair’)