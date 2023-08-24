print("Nombre de las entidades del modulo math")

import math
  
for name in dir(math):
  print(name, end="\t")

print()
print("Prueba de algunas funciones del modulo math")
print("Funciones trigonometricas")
from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

print("Funciones de exponenciacion")

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

print("funciones generales")

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

#modulo random

print("funcion random")

from random import random

for i in range(5):
    print(random())

print("funcion seed")

from random import random, seed

seed(0)

for i in range(5):
    print(random())
    
print("funciones randrange y randint")

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

print("Ejemplo 2")

from random import randint

for i in range(10):
    print(randint(1, 10), end=',')

print()
print("funciones choice y sample")

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

#modulo platform

print("funcion platform")

from platform import platform
 
print(platform())
print(platform(1))
print(platform(0, 1))

print("funcion machine")

from platform import machine

print(machine())

print("funcion processor")

from platform import processor
 
print(processor())

print("funcion system")

from platform import system
 
print(system())

print("funcion version")

from platform import version
 
print(version())

print("funciones python_implementation y python_version_tuple")

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)

print("pregunta 1")

import math
result = math.e == math.exp(1)
print(result)

print("pregunta 4")

import platform
print(len(platform.python_version_tuple()))