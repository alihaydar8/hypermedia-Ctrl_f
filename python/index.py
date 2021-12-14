import os
import glob
import mysql.connector

def remplire_liste_dossier(liste_element):
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
                                liste_element.append((element,filename.replace("..",""),1))
            f.close()

def remplire_liste_fichier(liste_vide,fichier_vide_nom):
    fichier_vide = open(fichier_vide_nom, "r",encoding='utf-8')
    for line in fichier_vide:
        for element_vide in line.split() :
            liste_vide.append(element_vide)

def filter_liste(liste_element,liste_vide):
    for element in liste_element:
        for element_vide in liste_vide :
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
    return mydb

def database_delete(mydb):
    mydb.cursor().execute("Delete from Cr_f")
    mydb.commit()

def database_liste(liste_element,mydb):
    id= 0
    for element in liste_element :
        mydb.cursor().execute("INSERT INTO Cr_f (id,nom, fichier,occ) VALUES (%s,%s,%s,%s)",(id,element[0],element[1],element[2]))
        id = id +1
    mydb.commit()
    

def main():

    liste_element = []
    liste_vide = []
    fichier_vide_nom ="../fichier/vide/fichier_vide.txt"
    remplire_liste_dossier(liste_element)
    remplire_liste_fichier(liste_vide,fichier_vide_nom)
    filter_liste(liste_element,liste_vide)
    liste_element = occurrences_lsite(liste_element)
    display_liste(liste_vide)
    mydb = database_connection()
    database_liste(liste_element,mydb)
    # database_delete(mydb)

    mydb.close()


if __name__ == '__main__' :
    main()
