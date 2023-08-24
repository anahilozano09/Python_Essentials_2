#importando el modulo math y usandolo

import math
print(math.sin(math.pi/2))

#otro ejemplo

print("Otro ejemplo")

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))

#haciendo el import solo de ciertas entidades
print("Reescribiendo el código")

from math import sin, pi

print(sin(pi/2))

print("Otro ejemplo")

from math import sin, pi

print(sin(pi / 2))

pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))

#realizando lo mismo que el codigo anterior pero de manera inversa

print("Forma inversa")

pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))

from math import sin, pi

print(sin(pi / 2))

#usando alias

print("usando alias para el modulo")

import math as m
    
print(m.sin(m.pi/2))
 
#importacion selectiva usando alias

print("importacion selectiva")

from math import pi as PI, sin as sine
  
print(sine(PI/2))