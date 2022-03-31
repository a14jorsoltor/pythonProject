'''Ex2
Escriu un programa en python que vagi eliminant i imprimint per pantalla
el 5è
 número d’una llista donada. Ex: 8,1,5,7,6,3,4,4,4,3
iteració1: 6
iteració2: 3
iteració3: 4
iteració4: 4...'''

llista = [8, 1, 5, 7, 6, 3, 4, 4, 4, 3]
while len(llista) >= 5:
    print("Iteracio: " + str(llista.pop(4)))
input()