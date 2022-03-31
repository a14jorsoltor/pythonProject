'''Ex5
Escriu una funció de python que crei el tag HTML per una paraula donada,
tal que si introduim afegir_tags(‘b’,’Formació Python’) l’output serà
<b>Formació Python </b> (que seria posar-ho en negreta)'''

def afegir_tags(tag, frase):
     return "<" + tag + ">" + frase + "</" + tag + ">"


input(afegir_tags("b", "formacio pyton"))
