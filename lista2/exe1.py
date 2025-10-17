SM = int(input(" Digite o sálario mensal: "))
PR = int(input(" Digite o percentual de reajuste: "))
calculo = (SM * PR / 100)

NV = (SM + calculo)

print(" Seu novo salario é: ", NV)