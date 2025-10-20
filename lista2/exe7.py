VA = float(input(" Qual sua velocidade: "))
VM = float(input(" Qual o limite de velocidade: "))
excesso = (VA - VM)

if (excesso <= 0):
    print (" Sem multa ")
elif (excesso <= 10):
    print(" Multa de R$ 50,00 ")
elif (excesso <= 30):
    print(" Multa de R$ 100,00 ")
else: print(" Multa de R$ 200,00")