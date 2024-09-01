import string 
import random


def password() -> str:
    
    longitud = int(input("Ingresa el tamaño de la contraseña: "))               # ingresa un numero entero
    caracteres =  string.ascii_letters + string.digits + string.punctuation      # una variable con todos los caracteres
    password = "".join( random.choices(caracteres, k=longitud))
    return password


     
print(password())