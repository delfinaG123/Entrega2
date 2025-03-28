
import re

valid = False

def valido(valid, new_user):
    
    valid = len(new_user)>4 and bool(re.search(r"\d", new_user)) and bool(re.search(r"[A-Z]", new_user)) and bool(re.fullmatch(r"[A-Za-z0-9]+", new_user))
    
    return valid

while not valid:

    new_user = input("""Ingresa un id valido: "

    Requisitos:               
    # Al menos 5 caracteres.
    # Contiene al menos un número.
    # Contiene al menos una letra mayúscula.
    # Solo puede contener letras y números.                
                 
    Usuario:
                      """)

    valid = valido(valid,new_user)

    if valid:
        print("Usuario validado")
    else:
        print("Intenta otra opcion, revisa los requisitos")