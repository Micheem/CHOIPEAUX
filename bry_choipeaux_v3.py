from choipeaux_magique_pourlapartie2 import *
from browser import document as doc, html
import csv

doc <= html.H1("Bienvenue sur notre quesionnaire")
doc <= html.IMG(src="choipeaux.png", id="img")

with open("question18.csv", mode='r', encoding='utf-8') as g:
    reader = csv.DictReader(g, delimiter=',')
    questions = [{key: value for key, value in element.items()} for element in reader]

new_dico = {}

for question in questions:
    iteme = question.items()
    for (cle, valeur) in iteme:
        couple = valeur.split("/")

        dico = {}
        dico[couple[0]] = [int(i) for i in couple[1].split(',')]

        if cle not in new_dico.keys():
            new_dico[cle] = dico

        else :
            new_dico[cle].update(dico)



liste_qst = list(new_dico.keys())



user = {'Courage': 7  , 'Ambition': 7 , 'Intelligence': 7, 'Good': 7}
liste_ajustement = [0, 0, 0, 0]

nb_qstn = 1  #
nm_qstn = 0  # le numéro de la question a la quelle on est rendue
def click(event):
    global nb_qstn  
    global nm_qstn
    global liste_ajustement
    nb_qstn += 1
    nm_qstn += 1 
    if nm_qstn < len(liste_qst):
        #valeur = event.target.value
        text_btn = event.target.text        
        affichage_question(new_dico, liste_qst, nm_qstn)
        ajustement = new_dico[liste_qst[nm_qstn-1]][text_btn]
        liste_ajustement = [ajustement[i] + liste_ajustement[i] for i in range(4)]
        print("liste_ajustement = ", liste_ajustement)
        doc['result'].style.display ='none'
    else:
        user = {'Courage': liste_ajustement[0]  , 'Ambition': liste_ajustement[1] , 'Intelligence': liste_ajustement[2], 'Good': liste_ajustement[3]}
        print("user = ", user)
        print(maison(poudlard_characters, user, k=7))

def resultat(event):
        
    user = {'Courage': 7 + courage , 'Ambition': 7 + ambition, 'Intelligence': 7 + intelligence, 'Good': 7 + good}
    doc <= html.H3(f"La maison attribué à cet élève est {maison(poudlard_characters, user, k=7)}")


doc <= html.B('Question', id="texte_qst")
doc <= html.P(html.BUTTON('Reponse', id= "rep1", value=0))
doc <= html.P(html.BUTTON('Reponse', id= "rep2", value=1))
doc <= html.P(html.BUTTON('Reponse', id= "rep3", value=2))
doc <= html.H2(html.BUTTON('Résultat', id= "result"))

doc['result'].style.display ='none'
doc['result'].bind('click',resultat)
doc['rep1'].bind('click', click)
doc['rep2'].bind('click', click)
doc['rep3'].bind('click', click)

def affichage_question(dico_qtsn ,liste_qstn, n_qstn):
    question = liste_qstn[n_qstn]
    liste_reponse = list(dico_qtsn[question].keys())
    doc["texte_qst"].textContent = question
    doc["rep1"].textContent = liste_reponse[0]
    doc["rep2"].textContent = liste_reponse[1]
    doc["rep3"].textContent = liste_reponse[2]

affichage_question(new_dico, liste_qst, nm_qstn)
