#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
##                                                                           ## 
##                              Author: Rouemis                              ##
##                             Date: 02/04/2022                              ##
##                                Time: 23:33                                ##
##                         GEN321 - Électrotechnique                         ##
##                    Cours - Réseau triphasé déséquilibré                   ##
##                       Université du Québec à Rimouski                     ##
##                                                                           ##
###############################################################################

import cmath
import math

# Liste des fonctions

def con_rect_pol() :
    # Conversion rectangulaire -> polaire
    print("Veuillez entrer les valeurs de votre vecteur : ")
    x = float(input("x = "))
    y = float(input("y = "))
    nb_complexe = complex(x,y)
    print("\n")
    print("Votre vecteur polaire a une amplitude de : ",round(abs(nb_complexe),2),"\net un angle de : ",round(math.degrees(cmath.phase(nb_complexe)),2))

def con_pol_rect() :
    # Conversion polaire -> rectangulaire
    print("Veuillez entrer votre vecteur polaire : ")
    r = float(input("r = "))
    t = float(input("t = "))
    print("\n")
    nb_complexe = complex(round(r*math.cos(math.radians(t)),2),round(r*math.sin(math.radians(t)),2))
    print("Votre vecteur est : ", nb_complexe)

def op_add() :
    # Addition de deux vecteurs
    print("Veuillez entrer votre premier vecteur : ")
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    print("\n")
    print("Veuillez entrer votre deuxième vecteur : ")
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    print("\n")
    nb_complexe1 = complex(x1,y1)
    nb_complexe2 = complex(x2,y2)
    nb_complexe3 = nb_complexe1 + nb_complexe2
    print("Votre vecteur additionné est : ", nb_complexe3)

def op_sub() :
    # Soustraction de deux vecteurs
    print("Veuillez entrer votre premier vecteur : ")
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    print("\n")
    print("Veuillez entrer votre deuxième vecteur : ")
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    print("\n")
    nb_complexe1 = complex(x1,y1)
    nb_complexe2 = complex(x2,y2)
    nb_complexe3 = nb_complexe1 - nb_complexe2
    print("Votre vecteur soustraction est : ", nb_complexe3)

def op_mult() :
    # Multiplication de deux vecteurs
    print("Veuillez entrer votre premier vecteur : ")
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    print("\n")
    print("Veuillez entrer votre deuxième vecteur : ")
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    print("\n")
    nb_complexe1 = complex(x1,y1)
    nb_complexe2 = complex(x2,y2)
    nb_complexe3 = nb_complexe1 * nb_complexe2
    print("Votre vecteur multiplication est : ", nb_complexe3)

def op_div() :
    # Division de deux vecteurs
    print("Veuillez entrer votre premier vecteur : ")
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    print("\n")
    print("Veuillez entrer votre deuxième vecteur : ")
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    print("\n")
    nb_complexe1 = complex(x1,y1)
    nb_complexe2 = complex(x2,y2)
    nb_complexe3 = nb_complexe1 / nb_complexe2
    print("Votre vecteur division est : ", nb_complexe3)

def op_index() :
    # Choisir l'opération
    print("Veuillez choisir l'opération que vous souhaitez effectuer : ")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

    while True :
        choix = int(input("Votre choix : "))
        if choix == 1 :
            op_add()
            break
        elif choix == 2 :
            op_sub()
            break
        elif choix == 3 :
            op_mult()
            break
        elif choix == 4 :
            op_div()
            break
        elif choix == 5 :
            break
        else :
            print("Veuillez entrer un chiffre entre 1 et 5")
            print("\n\n")

def Fortescue_inv() :
    # Calcul de la matrice de Fortescue inverse
    print("Veuillez entrer vos 3 vecteurs : ")

    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    x3 = float(input("x3 = "))
    y3 = float(input("y3 = "))

    C1 = complex(x1,y1)
    C2 = complex(x2,y2)
    C3 = complex(x3,y3)

    print("\n")
    print("Vecteur 1 : ", C1)
    print("Vecteur 2 : ", C2)
    print("Vecteur 3 : ", C3)
    print("\n")

    a = complex(-1/2, math.sqrt(3)/2)
    a2 = complex(-1/2, -math.sqrt(3)/2)

    Sol1 = (1/3)*(1*C1 + 1*C2 + 1*C3)
    Sol2 = (1/3)*(1*C1 + a*C2 + a2*C3)
    Sol3 = (1/3)*(1*C1 + a2*C2 + a*C3)

    print("Sol1 : ", Sol1)
    print("Sol2 : ", Sol2)
    print("Sol3 : ", Sol3)


# Page d'accueil

print("Hello la zon !!! \n")


while True:

    choix = input("Veuillez choisir une option : \n\n 1 - Conversion rectangulaire -> polaire \n 2 - Conversion polaire -> rectangulaire \n 3 - Opération de complexes \n 4 - Transformer de Fortescue (inverse) \n 5 - Quitter \n\n Votre choix : ")
    print("\n")

    # selection de l'option

    if choix == "1" :
        # Conversion rectangulaire -> polaire
        print("Conversion rectangulaire -> polaire")
        print("\n")
        con_rect_pol()
        break

    elif choix == "2" :
        # Conversion polaire -> rectangulaire
        print("Conversion polaire -> rectangulaire")
        print("\n")
        con_pol_rect()
        break

    elif choix == "3" :
        # Opération de complexes
        print("Opération de complexes")
        print("\n")
        op_index()
        break

    elif choix == "4" :
        # Transformer de Fortescue (inverse)
        print("Transformer de Fortescue (inverse)")
        print("\n")
        Fortescue_inv()
        break

    elif choix == "5" :
        # Quitter
        print("Au revoir")
        exit()

    else :
        # Erreur
        print("Veuillez entrer un chiffre entre 1 et 5")
        print("\n\n")

print("\n\n")
print("Au revoir les sos !")
print("Ton Rouemis préféré <3")