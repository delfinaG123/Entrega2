titles = [
"Speedrun de Super Mario en tiempo récord",
"Charla sobre desarrollo de videojuegos",
"Jugando al nuevo FPS del momento con amigos",
"Música en vivo: improvisaciones al piano"
]   

# Crear diccionario con la cantidad de palabras en cada título
cant_palabras = {i: len(i.split()) for i in titles}

# Encontrar el título con más palabras
max_title = max(cant_palabras, key=cant_palabras.get)

print(max_title)
    



