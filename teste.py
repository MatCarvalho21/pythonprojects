Báskara 
a = input("Qual o seu coeficiente a? ")
b = input("Qual o seu segundo coeficiente? O b. ")
c = input("Qual o seu último coeficiente? ")

y = (b^2) - (4*a*c)
y2 = y^(1/2)

if y2>0:
    x1 = round(((-b + y2)/2*a), 2)
    x2 = round(((-b - y2)/2*a), 2)
    print("As suas raízes são:", y, y2)
else: 
    print("A sua equação não possui raízes reais.")
