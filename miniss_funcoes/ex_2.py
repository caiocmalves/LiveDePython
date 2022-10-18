"""Des|empacotamento de argumentos"""

#def meu_sum(*args, **kwargs):
def meu_sum(*grupo_pos, **grupo_nom):
    """Empacotamento"""
    print(grupo_pos, grupo_nom)
    print(type(grupo_pos), type(grupo_nom))
    return grupo_pos, grupo_nom



lista = [-1, 2, 3, 4, -10]

def meu_min(a, b, c, d, *args):
    return min((a, b, c, d, *args))

#meu_min(*lista)

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

def meu_max(a=0, b=0, c=0, d=0):
    return max((a, b, c, d))

# meu_max(**dicionario)

l = [1,2,3]
d = {'d': 4,'e': 5}

def meu_mix(a, b, c, d=0, e=0):
    return a, b, c, d ,e 

meu_mix(*l, **d)