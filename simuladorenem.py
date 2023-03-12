#################### SIMULADOR DE MÉDIA ENEM ####################
print("Bem vindo ao simulador de notas do Enem. Por favor, insira as suas notas abaixo.")
n = float(input("Qual foi a sua nota em CIÊNCIAS DA NATUREZA? "))
m = float(input("Qual foi a sua nota em MATEMÁTICA? " ))
l = float(input("Qual foi a sua nota em LINGUAGENS? "))
h = float(input("Qual foi a sua nota em CIÊNCIAS HUMANAS? "))
r = float(input("Qual foi a sua nota na REDAÇÃO? "))
print("Ótimo! Agora insira o nome da universidade desejada e depois os pesos que ela atribui para cada área do conhecimento.")
u = input("Qual universidade você pretende ingressar? ")
q = input("Ela, realmente, atribui pesos diferentes para diferentes áreas do conhecimento? Responda 1, para SIM. E 2, para NÃO. "
          if (q=1):
          n1 = float(input("Qual o peso que a {} dá para CIÊNCIAS DA NATUREZA? ".format(u)))
          m1 = float(input("Qual o peso que a {} dá para MATEMÁTICA? ".format(u)))
          l1 = float(input("Qual o peso que a {} dá para LINGUAGENS? ".format(u)))
          h1 = float(input("Qual o peso que a {} dá para CIÊNCIAS HUMANAS? ".format(u)))
          r1 = float(input("Qual o peso que a {} dá para REDAÇÃO? ".format(u)))
          resultado = ((n*n1) + (m*m1) + (l*l1) + (h*h1) + (r*r1))/(n1+m1+l1+h1+r1)
          print(f"Bem, com os valores fornecidos acima, a sua média ponderada das notas do Enem para esse curso é {resultado:,.2f}.")
          else:
          n2 = 1
          m2 = 1
          l2 = 1
          h2 = 1 
          r2 = 1
          resultado2 = (n + m + l + h + r)/(5)
          print(f"Bem, com os valores fornecidos acima, a sua média ponderada das notas do Enem para esse curso é {resultado2:,.2f}.")
