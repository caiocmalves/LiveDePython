while True:
    try:
        nome = input('Digite seu nome: ')
        print(f'Olá {nome}')
        0/0
    #except :   #uma exceção genérica
    except KeyboardInterrupt:
        print('\nTudo bem, já entendi, você não quer brincar')
        exit()
    except ZeroDivisionError:
        print('Voce não sabe que não pode dividir por 0?')
        
"""
Usar somente o except, torna uma função genérica, ou seja, qualquer exceção será tratada igualmente.
Usando diretamente uma exceção, o exception vai tratar somente da exceção especificada.
"""
