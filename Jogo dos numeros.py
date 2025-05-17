import random
while True:#Loop de verificação idade
    print("Bem-vindo(a) ao jogo dos números")
    nome = input("Qual o seu nome?")
    print(
    "As regras são simples", nome,"\nvocê começa apostando algum valor e escolhe um número de 1 a 10, \n"
                                  "se acertar o número em cheio, ganha o dobro do dinheiro apostado\n"
                                  "se acertar por 1 número de diferença(tanto para menos quanto para mais)\n"
                                  "ganha o valor apostado mais 50%"
)
    print("Antes de tudo é necessário verificar sua idade")
    idade = int(input("Quantos anos você tem? :"))
    if idade < 18:
        print("De acordo com a Lei 14.790/2023, \n"
              "é proibido a participação de menores em apostas")
        continue
    elif idade >= 18:
        print("Certo vamos começar o jogo!")
        break
aposta = int(input("Qual o valor da sua aposta?: \n"))
chute = int(input("Qual número você vai apostar?: \n"))
numero = random.randint(1,10)
if chute == numero:
    aposta = aposta*2
    print("O número sorteado foi: ",numero)
    print("Parabéns,",nome,"você acertou em cheio e ganhou ",aposta,"!")
elif chute == numero +1 or chute == numero -1:
    aposta = aposta + aposta/2
    print("O número sorteado foi: ", numero)
    print("Parabéns,",nome,"você acertou com a diferença de um número e ganhou: ",aposta,"!")
else:
    print("Você errou!, aposte novamente para tentar ganhar um dinheiro de volta")
























































































