"""função como bjetos de primeira classe"""

from typing import Callable, Dict
from numbers import Number

func = lambda: 'resultado da função'


#com funções anonimas
calc: Dict[str, Callable]= {
    'soma': lambda x, y: x + y,
    'sub': lambda x, y: x - y, 
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x / y
}
# calc['mult'](4,4)

#com funcoes normais
def soma(x: Number, y: Number) -> Number:
    """Soma dois números."""
    return x + y


def sub(x: Number, y: Number) -> Number:
    """Subtrai dois números."""
    return x - y


def mult(x: Number, y: Number) -> Number:
    """Multiplica dois números."""
    return x * y


def div(x: Number, y: Number) -> Number:
    """Divide dois números."""
    return x / y


calc_nomeado = {
    'soma': soma,
    'sub': sub,
    'mult': mult,
    'div': div,
}
#calc_nomeado['soma'](1,1)


somas = [
    lambda x: x + 0,
    lambda x: x + 1,
    lambda x: x + 2
]
#somas[0](1)


def soma_1(x: Number) -> Number:
    """Soma 1 a qualquer x de entrada."""
    return x + 1


