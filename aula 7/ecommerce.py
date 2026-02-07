print('- Lino´s Store -')
print('***' *20)

ecommerce = {
'Livros': 100,
'tablets': 3000,
'fone':200

}

carrinho = {
'produtos': [],
'valores': []

}

produto1 = input('produto: ')
produto2 = input('produto: ')

carrinho['produtos'].append(produto1)
carrinho['produtos'].append(produto2)
carrinho['valores'].append(ecommerce[produto1])
carrinho['valores'].append(ecommerce[produto2])

soma = sum(carrinho['valores'])
print('Total= R$',soma)

forma_pagamento = ['pix', 'cc', 'cd']
escolhe_forma = input('Digite a forma de pagamento!: ')
indice = forma_pagamento.index(escolhe_forma)
print ('Forma de pagamento: ', forma_pagamento[indice])
print ('otimo dia')