produto = input("Digte o proudto: ")
preco = float (input(f"Digite o preço de {produto}: "))

dwhile true:
    quant = int(input(f"Digite a quantidade de {produto}"))
    if quant <= 50:
        break
total = preco * quant
if quant <=20:
    desconto = total * 0.02
else:
    desconto = total * 0.05
pagar = total - desconto
print (f"pagar R$: {pagar:.2f} por {produto}")
