#numerando, pode-se alterar e/ou repetir
email = '''
        Olá, {0}.
        
        Gostariamos de dizer que {0}, foi premiado na promoção {1}.
        ''' 

print(email.format('Eduardo', 'Caminhão do Faustão'))


#nomeando
print('{nome} {sobrenome}'.format(nome='Caio', sobrenome='Carvalho'))

#por dicionario
pessoa = {
    'nome': 'Caio',
    'idade': 29,
    'apelido': 'indio'
}

s = 'Oi {nome}, vi que tem {idade} anos e seu apelido é {apelido}'


#**pessoa = nome=pessoa['nome'], idade=pessoa['idade'], apelido=pessoa['apelido']
print(s.format(**pessoa))


nome = 'caio'

print('{}'.format(nome.upper()))


#fstring chamando posições de uma lista
