#################### SIMULADOR DE INVESTIMENTOS ####################
import math
print("Welcome! You are in the investments simulator. Here we gonna work if simple fees. You will tell to us what is your initial investment \n and the monthly interest rate. ")
name = input("First of all, what is you name? ")
value = float(input("{}, what is the initial value that you have now and is available to invest? ".format(name)))
rate = int(input("What is the monthly interest rate? "))
realrate = 1 + (rate/100)
time = int(input("Tell me, for how much time, in mouths, do you want to let your money invested? "))
result = float(value*pow(realrate, time))
print("Ok, {}. Now we will calculate your return.".format(name))
print("Just a few minutes...")
print(f"In {0} years, investing in the beginning {1} dollars, with a monthly interest rate of {2}, you will have {result:,.2f} dollar of patrimony.".format(time, value, rate, result))