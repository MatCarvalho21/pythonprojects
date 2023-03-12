########## CONVERSOR DE NÚMERO INTEIRO ##########
import math
n = float(input("Digite um valor qualquer. Se for um valor com casas decimais, represente por ponto e não vírgula. "))
nr = math.trunc(n)
print("O arredondamento do seu valor {} resultou em {}. ".format(n, nr))
