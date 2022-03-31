'''Ex9
Escriu un programa en python que crei una base de dades postgreSQL
'''
import psycopg2

#Establim la conexio
conn = psycopg2.connect(
   database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#Instancia un cursor
cursor = conn.cursor()

#Query per a base de dades
sql = '''CREATE database mydb''';

#Creem la base de dades
cursor.execute(sql)
print("Database created successfully........")

#Tanquem la conexio
conn.close()