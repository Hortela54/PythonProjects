import forca
import adivinhacao
print("###############################")
print("#######Escolha o seu jogo######")
print("###############################")

print("(1)Forca (2) Adivinhação")

jogo = int(input("Qual jogo?\n"))

if(jogo == 1):
    adivinhacao.jogar()
elif(jogo == 2):
    forca.jogar()
