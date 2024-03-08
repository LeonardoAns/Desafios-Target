def reverse(palavra):
    str_reverse = ""
    for i in range(len(palavra ) -1, -1, -1):
        str_reverse += palavra[i]
    return str_reverse

palavra = str(input("Digite uma palavra ou frase\n"))
print(reverse(palavra))