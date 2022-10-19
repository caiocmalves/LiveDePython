from numbers import Number
from typing import Union, Any, List, Text, Sequence, Dict

Somavel = Union[Number, str, list]


def soma(x: Somavel, y: Somavel) -> Somavel:
    return x + y


def identidade(val: Any) -> Any:
    return val


def meu_sum(l: List[Number]) -> Number:
    return sum(l)


def cadastro_usuario(nome: str, idade: int, gostos: List[str]) -> Dict[str, Union[str, int, List[str]]]:
    return {'nome': nome, 'idade': idade, 'gostos': gostos}


def meu_min(seq: Sequence):
    return min(seq)


def converter_para_reais(valor: Text):
    ...
    
