rules = " Respeta a los demás. No se permiten insultos ni lenguaje ofensivo. Evita el spam. No publiques enlaces sospechosos o repetitivos. No compartas información personal. Usa los canales adecuados para cada tema. Sigue las instrucciones de los moderadores"
separated_rules = rules.lower().split(". ")
print(separated_rules)

palabra_clave = input("Ingresa una palabra clave: ")

for rule in separated_rules:
    if palabra_clave in rule:
        print(rule)
