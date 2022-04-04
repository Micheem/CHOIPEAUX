# -*- coding: utf-8 -*-
'''
Description du programme
Auteurs: Loys MARIOT, Florian VERNE, Michée MANON
Numéro de version 11.1
Date de dernière révision: 11/03/2022
'''

from math import sqrt
import csv

vert = '\33[92m'
jaune = '\33[93m'
rouge = '\33[91m'
indigo = '\33[94m'
rose = '\33[95m'
noir = '\33[30m'
cyan = '\33[36m'

reset = '\033[0m'  # réinitialise la couleur
g = '\033[1m'  # gras
s = '\033[4m'  # surligner
i = '\033[3m'  # italique

continuer = 1

with open("Characters.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    characters = [{key: value for key, value in element.items()} for element in reader]

with open("Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as h:
    reader = csv.DictReader(h, delimiter=';')
    caracteristiques = [{key: value for key, value in element.items()} for element in reader]

poudlard_characters = []

for poudlard_character in caracteristiques:
    for i in characters:
        if poudlard_character['Name'] == i['Name']:
            poudlard_character.update(i)
            poudlard_characters.append(poudlard_character)


def converti(table):
    '''
    Fonction qui change les chaînes de caractères des caractéristiques en entier
    :param table: liste de dictionnaire contenant l'ensemble des élèves de poudlard
    :return: c'est la même table que celle en paramètre sauf que ses descripteurs de caractéristiques sont maintenant des entiers
    '''
    for dico in table:
        for keys in ['Courage', 'Ambition', 'Intelligence', 'Good']:
            dico[keys] = int(dico[keys])
    return table


converti(poudlard_characters)

# début du programme
def distance(eleve1, eleve2):
    '''
    Fonction calculant la distance entre 2 élèves en fonction de leurs caractéristiques
    On utilise ici la distance euclidienne
    :param eleve1: dictionnaire contenant des caractéristiques
    :param eleve2: pareil que l'élève 1
    :return: (entier) la distance entre 2 élèves
    '''
    return sqrt((eleve1['Courage'] - eleve2['Courage']) ** 2
                + (eleve1['Ambition'] - eleve2['Ambition']) ** 2
                + (eleve1['Intelligence'] - eleve2['Intelligence']) ** 2
                + (eleve1['Good'] - eleve2['Good']) ** 2)


def kkpv(table, eleve, k):
    '''
    Fonction ajoutant un descripteur à chaque eleve(dictionnaire) dans la table poudlard
    :param table: liste de dictionnaire contenant l'entierté des élèves
    :param eleve: un dico contenant élève et ses caractéristiques
    :return: table: liste de dictionnaire contenant désormais un nouveau descripteurs, la distance
    '''
    for eleves in table:
        eleves['Distance'] = round(distance(eleve, eleves), 2)

    voisins = sorted(table, key=lambda x: x['Distance'])


    return voisins[:k]

def affichages_voisins(table, eleve, k):
    for dico in kkpv(table, eleve, k):
        house = dico['House']
        nom = dico['Name']
        return f"L'élève {nom} de la maison {house}"    

def maison(table, eleve_cible, k):
    '''
    Fonction déterminant quelle maison serait la mieux adapté à un élève en fonction des kppv
    :param table: (liste de dictionnaire)table contenant les élèves de poudlard avec lesquelles on va comparer notre élève selon le nombre de voisin
    :param eleve_cible: (dictionnaire) élève auquel on veut trouver la maison
    :param k: (entier) nombre de voisins
    :return: sa_maison, une chaine de caractère contenant la maison la mieux adapté pour l'élève
    '''

    redondance_g = 0
    redondance_h = 0
    redondance_r = 0
    redondance_s = 0

    for dico in kkpv(table, eleve_cible, k):
        house = dico['House']

        if house == 'Gryffindor':
            redondance_g += 1

        elif house == 'Hufflepuff':
            redondance_h += 1

        elif house == 'Slytherin':
            redondance_s += 1

        else:
            redondance_r += 1

    liste_redondance = [redondance_s, redondance_g, redondance_h, redondance_r]
    liste_redondance.sort(reverse=True)

    if liste_redondance[0] == redondance_g:
        sa_maison = 'Gryffindor'

    elif liste_redondance[0] == redondance_h:
        sa_maison = 'Hufflepuff'

    elif liste_redondance[0] == redondance_s:
        sa_maison = 'Slytherin'

    elif liste_redondance[0] == redondance_r:
        sa_maison = 'Ravenclaw'
    return sa_maison