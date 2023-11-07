#Definindo função de multiplicar
from math import pow, pi

def multiplicar(x, y):
    multi = x * y
    return multi

def ehpar(x):
    if (x % 2) == 0:
        return True
    else:
        return False


def ehprimo(x):
    for k in range (2, x):
        if x % k == 0:
            return False
    return True

def esferavolume(raio):
    volume = 4/3 * pi * pow(raio, 3)
    return volume

def converte_time(hora, minuto, segundo):
    return (hora * 3600 + minuto * 60 + segundo)



