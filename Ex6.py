'''Ex6
Escriu un programa en python que afegeixi un nou caràcter introduït per
l’usuari al final d’un array. Ha de demanar a l’usuari que introdueixi l’array
original i després quin caràcter vol afegir-hi.
'''
llista1 = ["hola", "jordi"]
llista2 = []
i = 0
semafor = False
while not semafor:
    while i != len(llista1):
        print("Digues valor " + str(i+1) + " de la llista 1")
        llista2.append(input())
        if llista2[i] == llista1[i]:
            i+=1
        else:
            print("El valor no era igual")
    if llista1 == llista2:
        semafor = True
        i = 0
    else:
        semafor = False
        i = 0
if semafor:
    semafor= False
    print("Posa un nou valor")
    llista1.append(input())

print(llista1)

##programa pau
charList = ['a', 'b', 'c']
userList = charList
print("Write a character to add it to the list: ")
userChar = input()
userList.append(userChar)

print("Character added!")
print("List before: " + str(charList) + ". List after: " + str(userList))