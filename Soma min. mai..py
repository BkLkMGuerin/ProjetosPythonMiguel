contar_maisculas_minusculas = input("Digite seu texto: \n")
soma_mai = 0
soma_min = 0
for x in contar_maisculas_minusculas:
    if x.isupper():
        soma_mai += str.isupper(x)#Aqui vai somar somente quantas maiusculas tem no texto
    elif x.islower():
        soma_min += str.islower(x)#Aqui vai somar as minusculas
print("Você possui", soma_mai,"letras maiuscúlas no texto")
print("E", soma_min,"minúsculas")
resultado_maiusculas_minusculas = soma_min + soma_mai#esta linha vai somar os resultados que ja foram formatados em int pela soma de cima
print("No total são", resultado_maiusculas_minusculas,"letras no texto")