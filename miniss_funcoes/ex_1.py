"""funcoes anonimas"""

anon = lambda : 'Oi'
anonima = lambda param: param + 2
anonima_plus = lambda param1, param2: param1 + param2


### FUNÇÕES TRADICIONAIS
def soma_posicional(x,y):
    """X e Y são parametros posicionais"""
    return x + y

def soma_nomeados(x=7, y=7):
    """X e Y são parametros nomeados
        Na falta de x ou y, o valor 7 será usado (default)
    """
    return x + y

def soma_explicitamente_nomeados(*, x=7, y=7):
    """Nessa situação, ele exige que o parâmetro seja nomeado
    """
    return x + y

def soma_explicitamente_nomeados2(x=7, *, y=7):
    """Nessa situação, ele exige que um argumento seja nomeado
        No caso, todos após o *
    """
    return x + y