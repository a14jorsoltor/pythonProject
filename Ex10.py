'''Ex10
Escriu un programa en python que permeti llegir en format llista un arxiu
CSV introduit.'''
import csv

with open("ex10.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)