import string 
import random


def password(longitud) -> str:
    
    letras = string.ascii_letters
    numeros = string.digits
    signos = string.punctuation
    caracteres = letras + numeros + signos 
    
    password = "".join( random.choices(caracteres, k=longitud))
    
    return password