'''Ex8
Escriu un programa en python que llisti
els directoris i els arxius per separat d’una ruta especificada
'''
import glob
# All files and directories ending with .txt and that don't begin with a dot:
print(glob.glob("D:\CosesClase/*/"))
# All files and directories ending with .txt with depth of 2 folders, ignoring names beginning with a dot:
print(glob.glob("D:\CosesClase/*.*"))