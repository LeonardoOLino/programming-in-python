#Criar um e-commerce
# cadastro no e-commerce

dados = {
'login':[],
'senha':[]
}

print('cadastre-se')
cad_login = input('Cadastre seu login: ')
cad_senha = input('Cadastre sua senha: ')
dados['login'].append(cad_login)
dados['senha'].append(cad_senha)

# acessar o e-commerce

print('Acesse a aplicaçao')
acesso_login = input('Digite seu login para acessar: ')
acesso_senha = input('Digite sua senha para acessar: ')

if acesso_login in dados['login'] and acesso_senha in dados['senha'] :
    print('seja bem vindo(a) ao Lino e-commerce')
else:
    print('Digitaçao de senha ou login incorreto')
    print ('Faça novamente')

# verificar a lista de produtos
# comprar um produto
# paga o produto