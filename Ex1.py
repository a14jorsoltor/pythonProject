'''
Ex1
Escriu un programa en python que conti la quantitat de números parells
en una llista introduïda per l’usuari. Tal que si la llista introduïda és:
2,5,4,9,3,7,5,3 l’output hauria de ser 2.
'''
llista = []
llista2 = []
cont = 0
while True:
    print("Write a number")
    numero = int(input())
    if numero < 0:
        break
    else:
        llista.append(int(numero))
for i in range(len(llista)):
    if llista[i] % 2 == 0:
        cont += 1
        llista2.append(llista[i])
print("Els parells son: " + str(llista2) + " i hi ha: " + str(cont) + " parells")
