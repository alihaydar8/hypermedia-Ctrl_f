import os
import glob
import mysql.connector

def remplire_liste_dossier(liste_element):
    nombre_element = 0;
    for filename in glob.glob('../fichier/*.txt'):
        with open(os.path.join(os.getcwd(), filename), 'r',encoding='utf-8') as f: 
            for line in f :
                for elementss in line.split() :
                    for elements in elementss.split("’"):
                        for element in elements.split("'"):
                            element = element.replace('!','')
                            element = element.replace(':','')
                            element = element.replace('(','')
                            element = element.replace(')','')
                            element = element.replace('?','')
                            element = element.replace(',','')
                            if(len(element)>2) :
                                liste_element.append((element,filename.replace("../fichier\\",""),1))
                            nombre_element = nombre_element +1
            f.close()
    return nombre_element

def remplire_liste_fichier(liste_vide,fichier_vide_nom):
    fichier_vide = open(fichier_vide_nom, "r",encoding='utf-8')
    for line in fichier_vide:
        for element_vide in line.split() :
            liste_vide.append(element_vide)

def filter_liste(liste_element,liste_vide):
    for element_vide in liste_vide :
        for element in liste_element:
            if element[0].lower() == element_vide :
                liste_element.remove(element)

def  display_liste(liste_element):
    for element in liste_element :
        print (element) 

def occurrences_lsite (liste_element):
    occ_liste = []
    for elemnet in liste_element :
       occ_liste.append((elemnet[0],elemnet[1],liste_element.count(elemnet)))
    occ_liste = list(set(occ_liste))
    return occ_liste

def database_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="hypermedia",
        password="hypermedia",
        database="hypermedia"
        )
    mydb.cursor().execute("drop table if exists search")
    mydb.cursor().execute("CREATE TABLE IF NOT EXISTS search (id int PRIMARY KEY  COMMENT '',nom VARCHAR(255) COMMENT '',fichier VARCHAR(255) COMMENT '',occ int(4) DEFAULT NULL) DEFAULT CHARSET UTF8 COMMENT '' ")
    mydb.commit()
    return mydb

def database_delete(mydb):
    mydb.cursor().execute("Delete from search")
    mydb.commit()

def database_liste(liste_element,mydb):
    id= 1
    for element in liste_element :
        mydb.cursor().execute("INSERT INTO search (id,nom, fichier,occ) VALUES (%s,%s,%s,%s)",(id,element[0],element[1],element[2]))
        id = id +1
    mydb.commit()

def main():
    
    liste_element = []
    liste_vide = []
    fichier_vide_nom ="../fichier/vide/fichier_vide.txt"
#--------------- Partie netoyer les données----- 
    nombre_element = remplire_liste_dossier(liste_element)
    remplire_liste_fichier(liste_vide,fichier_vide_nom)
    filter_liste(liste_element,liste_vide)
    liste_element = occurrences_lsite(liste_element)

#--------------- Partie Database----------------
    mydb = database_connection()
    database_liste(liste_element,mydb)
    # database_delete(mydb)

#--------------- Partie statistique-------------     
    # print("les mots vide à retirer ")
    # display_liste(liste_vide)
    # print("les mots présent dans la base de donnée ")
    # display_liste(liste_element)
    print("nombre de mots dans les fichiers : ",nombre_element)
    print("nombre de mots dans la base de donnée : ",len(liste_element))
    print("pourcentage de réduction : ",100 *len(liste_element)/nombre_element,"%")
    print("sachant que mes fichiers ont différents thèmes(décommenter ligne 91 pour voire la qualité des mots sauvegardes dans la bases")

    mydb.close()


if __name__ == '__main__' :
    main()
