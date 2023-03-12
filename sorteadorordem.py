########## SORTEADOR DE ORDEM ##########
import random 
a1 = input("Digite o nome do primeiro aluno. ")
a2 = input("Digite o nome do segundo. ")
a3 = input("Do terceiro. ")
a4 = input("Do quarto agora. ")
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print("A ordem escolhida foi: {}.".format(lista))