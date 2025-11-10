def valorDoMeio (a,b,c):
    if (a>b and a<c) or (a<b and a>c):
        return a
    elif (b>a and b<c) or (b<a and b>c):
        return b
    else:
        return c

print (" Digite 3 valores: ")
v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valort: "))
v3 = float(input("Digite o terceiro valor: "))

meio = valorDoMeio(v1,v2,v3)
print (" O valor do meio é: ", meio)