

try:
    f = open('arquivo.txt')
except FileNotFoundError:
    print('Arquivo não existe.')
else:
    print(f.read())
    f.close()
finally:
    print('o finally sempre vai ser executado, com ou sem erro.')