super = float(input("Superficie inicial (m²): "))
gen = int(input("Num de generaciones (máx 50): "))
herederos = int(input("Herederos por generación: "))

if super <= 0:
    print("La superficie debe ser mayor que 0")
elif gen < 0 or gen > 50:
    print("Número de generaciones no válido")
elif herederos <= 0:
    print("El número de herederos debe ser mayor que 0")
else:
    resultado = super / (herederos ** gen)
    print("Superficie final por heredero:", resultado)
