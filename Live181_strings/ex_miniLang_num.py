#Conversão de bases
print(f'{16:b}') #binário
print(f'{16:o}') #octal
print(f'{16:d}') #decimal
print(f'{16:x}') #hexadecimal
print(f'{16:X}') #hexadecimal maiúsculo


from math import pi

print(f'{pi:.2f}')
print(f'{pi:.2e}')
print(f'{pi:.2%}')
print()

#juntando
print('{:-^10.4f}'.format(pi))


#datas e horas
from datetime import datetime

print(f'{datetime.now():%d-%m-%y %H:%M:%S}')
print(f'{datetime.now():%c}')