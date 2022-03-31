'''Ex7
Escriu un programa en python que per un número et
mostri la els resultats de la seva taula de multiplicar
(només de l’1 al 10), tal que si introdueixo 5, se’m mostra:
Taula del 5
5x1=5
5x2=10...'''
inputUsuari = 0
while int(inputUsuari) > 10 or int(inputUsuari) < 1:
    print("Digues un numero del 1 al 10")
    inputUsuari = input()
    if int(inputUsuari) > 10 or int(inputUsuari) < 1:
        print("Numero erroni")
for i  in range(1, 11):
    resultat = int(i)*int(inputUsuari)
    print(str(i) + " * " + str(inputUsuari) + "=" + str(resultat))
    resultat = 0

#pau

print("Write a number to show the multiplication table of it: ")

userNumber = ''
while not isinstance(userNumber, int):
    try:
        userNumber = input()
        userNumber = int(userNumber)
    except ValueError:
        print("This is not a number. Write a number")

for i in range(1, 11):
    print(str(userNumber) + "x" + str(i) + " = " + str(userNumber * i))