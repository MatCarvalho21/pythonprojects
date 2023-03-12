########## TRIGONOMETRIA ##########
import math
r = float(input("Coloque o valor do seu ângulo em graus. "))
f = (math.pi/2)/90
a = r*f
t = math.tan(a)
s = math.sin(a)
c = math.cos(a)
if (t <= 10000):
    print(f"O valor do seno do ângulo {0} é {s:,.2f}, do cosseno é {c:,.2f} e da tangente é {t:,.2f}. ".format(a))
else:
    print(f"O valor do seno do ângulo {0} é {s:,.2f}, do cosseno é {c:,.2f} e da tangente é muito próxima do infinito. ".format(a))