s = "hola soy una cadena de texto"

for letra in s:
    if letra == "a" or letra == "e":
        letra = "x"

print(s)


#letra no es "s", es solo una copia de un caracter de s

d = 0

for a in range(-3,2): #cada vez resta 1
    for b in range(0,4):
        for c in range(8,4,-1):
            d += 1


print(d)