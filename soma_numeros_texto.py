texto = input("Digite seu texto: \n")
soma_digitos = 0
quant = 0
for x in texto:
    if x.isdigit():
        soma_digitos += int(x) #Ele vai somar os numeros separados no texto
        quant += 1 #Somente um contador para saber quantos números tem no texto
print("a soma dos números no texto foram de", soma_digitos)
print("a quantidade de números no texto são de :", quant)




