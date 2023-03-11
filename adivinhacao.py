print('********** BEM VINDO AO JOGO DA ADIVINHAÇÃO **********')
resultado = 5
tentativas = 3

while(tentativas > 0):
    chute=int(input("Qual o seu primeiro palpite? Lembre-se, é um número de 1 a 10. "))
    if(chute == resultado):
        print("Parabéns!! Você acertou!!")
    else:
        print('Ops, não foi dessa vez...')
        if(chute > resultado):
            print("O número é menor que o seu palpite")
        else:
            print('O número é maior que o seu palpite')
        tentativas2 = tentativas - 1
        chutee=int(input('Tente novamente. Qual o seu segundo chute? '))
        if(chutee == resultado):
            print('Agora sim! Parabéns! Já tava ficando aflito...')
        else:
            if(chutee > resultado):
                print('É um número menor, idiota!')
            else:
                print('É um número maior, idiota!')
            tentativas3 = tentativas2 - 1
            chuteee=int(input("Já estou perdendo a paciência! Chuta logo a porra do número certo!!"))
            if(chuteee == resultado):
                print("Finalmente, até uma porta teria acertado...")
            else:
                print("O número certo era:", resultado)
print("Porém você não teve capacidade para descobrir. Sugiro que volte para a escola.")
