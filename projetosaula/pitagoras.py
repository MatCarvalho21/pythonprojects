########## PYHON DO PITAGORAS ##########
import math 
c1 = float(input("Coloque o valor do primeiro cateto. "))
c2 = float(input("Agora, coloque o valor do segundo cateto. "))
h = (c1)**(2)+(c2)**(2)
hr = math.sqrt(h)
print(f"O valor da hipotenusa do triâñgulo informado é {hr:,.2f}. ")