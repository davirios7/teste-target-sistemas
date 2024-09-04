string = input("Informe uma string: ")

def inverter_string(s):
    string_invertida = ""
    for s in string:
        string_invertida = s + string_invertida
    return string_invertida

resultado = inverter_string(string)
print(resultado)

# Ou simplesmente:
print(string[::-1])