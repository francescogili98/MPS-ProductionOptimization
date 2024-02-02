# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint in the code line below to debug your script.
# Press Ctrl+F8 to toggle the breakpoint.
from math import ceil, floor
from random import randint

n = int(input("Inserire numero di modelli:\n"))  # n scelta
T = 12  # T 12 mesi, 1 anno
A = 0.06  # A fisso 0.06
forecast = [randint(15, 125) for i in range(0, n)]  # forecast 15-125
kore = [randint(50, 200) for i in range(0, n)]  # kore 50-200
V = [int(round((forecast[i] / T), 0)) for i in range(0, n)]  # v forecast/T round
Rn = [ceil(V[i] * kore[i] *(1+A) / 85) for i in range(0, n)]  # Rn V*Kore/152 round up
R = ceil(sum(Rn)*.75)  # R sum Rn*0.85-0.95 round down * (randint(85, 95) / 100)

f = open("Dati-" + str(n) +".dat", "w")
f.write("!Questo file di prova è stato gentilmente offerto da un generatore casuale\n")
f.write("n:\t\t" + str(n) + "\n")  # n scelta
f.write("T:\t\t" + str(T) + "\n")  # T 12 mesi, 1 anno
f.write("R:\t\t" + str(R) + "\n")  # R sum Rn*0.85-0.95 round down
f.write("A:\t\t" + str(A) + "\n")  # A fisso 0.06
f.write("forecast:\t[")  # forecast 10-200
for i in range(0, n): f.write(str(forecast[i]) + "\t")
f.write("]\n")
f.write("kore:\t\t[")  # kore 75-225
for i in range(0, n): f.write(str(kore[i]) + "\t")
f.write("]\n")
f.write("V:\t\t[")  # v forecast/T *1-1.25 round
for i in range(0, n): f.write(str(V[i]) + "\t")
f.write("]\n")
f.write("Rn:\t\t[")  # Rn V*Kore/150 round up
for i in range(0, n): f.write(str(Rn[i]) + "\t")
f.write("]\n")
f.write("Giorni:\t\t[16\t19\t23\t20\t22\t19\t21\t8\t22\t21\t21\t16]\n")  # Giorni fisso
f.close()
