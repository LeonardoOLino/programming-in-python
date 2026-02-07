variavel = 10
variavel2 = 'text'
variavel3 = True
variavel4 = 5.2

lista = [1,2,3,4,5,6 ]

##acessando listas

print(lista[2])
print(lista[0] + lista[2])

##alteraçao de valor de algu indice

lista[3] = 100
print(lista)

print(lista[1]**2)

##alterar / verificar dado da lista
##alterar - inserir dados

#append() - adiona no final da lista

lista.append(100)

#insert() - adiciona no indice que vc indicar

lista.insert(0,'test')
print (lista)

#extend() - adiciona no final oq vc quiser

lista.extend([1,2,3,4])
print(lista)

# += - add no final quantos voce quiser
lista+=(1,2,3,4)
print(lista)

#------------------------------

#remove - remove a partir do valor

lista.remove('test')
print(lista)

#pop - remove o ultimo
lista.pop()

#pop(indice) - remove o indice

lista.pop(0)
print (lista)

#del - remove a partir do indice

del lista[1]
print(lista)

#-----------------------------------

##metodos e funçoes que verificam algum dado na lista
##açoes

#menor valor
print(min(lista))

#maior valor
print(max(lista))

#comprimento da lista
print(len(lista))

#quantos itens do valor declarado
print(lista.count(3))

#ordenar a lista

lista.sort()
print (lista)

lista.sort(reverse=True)
print(lista)

#sum - somaas todos os dados

print(sum(lista))

#copy - copiar

x = lista.copy()
print(x)

#clear - limpar

#lista.clear()
print(lista)

#indice
indice = lista.index(100)

print('posicao',lista)