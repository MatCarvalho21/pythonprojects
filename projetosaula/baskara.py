########## RESOLUÇÃO DE EQUAÇÃO DO SEGUNDO GRAU ########## 
print("Vamos começar!! Informe os coeficientes da sua equação. Caso não forem números inteiros, coloque um ponto para iniciar as casas decimais.")
a = input("Qual o seu coeficiente a? ")
b = input("Qual o seu segundo coeficiente? O b. ")
c = input("Qual o seu último coeficiente? ")

y = (b^2) - (4*a*c)
y2 = y^(1/2)

if y2>0:
    x1 = round(((-b + y2)/2*a), 2)
    x2 = round(((-b - y2)/2*a), 2)
    print(f"As suas raízes são: {x1:,.2f} e {x2:,.2f}")
else: 
    print("A sua equação não possui raízes reais. Confira os valores.")
