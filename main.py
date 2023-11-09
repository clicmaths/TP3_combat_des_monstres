#variable
import random

point_vie = "20"
question = "5"
while question != "4" or point_vie > "0":
    force_adversaire = random.randint(1, 5) + random.randint(1, 6)
    score_de = random.randint(1, 6) + random.randint(1, 6)
    numero_combat = 0
    question = input("niveau de monstre " + str(force_adversaire) +
                     "\n1.Combattre cet adversaire"
                     "\n2.Contourner cet adversaire et aller ouvrir une autre porte"
                     "\n3.Afficher les règles du jeu"
                     "\n4.Quitter la partie\n")


    if question=="1":
        point_vie = "20"
        victoire = 0
        defaite = 0
        victoires_consecutives = 0
        combat_statut = ""
        print( "Force de l’adversaire : "+str(force_adversaire)+
              "\nNiveau de vie de l’usager : "+str(point_vie)+
              "\nDernier combat : "+str(combat_statut)+
              "\nNuméro combat : "+str(numero_combat)+
              "\nNombre de victoires consécutives : "+str(victoires_consecutives)+
              "\nLancer du dé: " +str(score_de))
        if score_de > force_adversaire:
            victoire =+ 1
            victoires_consecutives =+ 1
            combat_statut = "victoire"
            print("",victoire,"victoire\n"
                  "",defaite,"défaite\n"
                  "",victoires_consecutives,"victoires consécutives\n")
            numero_combat = numero_combat=+1
        else:
            defaite =+ 1
            victoires_consecutives = 0
            combat_statut = "défaite"
            point_vie = point_vie =- force_adversaire
            print("", victoire, "victoire\n"
                  "", defaite, "défaite\n"
                  "", victoires_consecutives, "victoires consécutives\n")
            numero_combat = numero_combat = +1
            point_vie =- point_vie - force_adversaire
    elif question=="2":
        print("1")
    elif question=="3":
        print( " L’idée est la suivante : Le but de la partie est d’accumuler le plus possible de victoires."
               "\nElles s’additionnent en vainquant des monstres."
               "\nUn personnage circule dans un couloir (le monde), à chaque extrémité du couloir il y a une porte."
               "\nChacune de ces portes mène à une salle (le niveau)."
               "\nDans chaque salle, il y a un monstre et chaque monstre a un niveau de difficulté qui lui est propre."  
               "\nAvant d’incorporer du graphisme au jeu, le combat se fera avec un lancer de dés."
               "\nPour gagner des p oints de vie, l’usager doit avoir un total aux dés supérieur à la force du monstre."
               "\nL’usager peut tomber face à face avec un monstre trop effrayant."
               "\nDans ce cas, l’usager peut contourner le monstre et aller ouvrir une autre porte.  Cette manœuvre coûte 1 point de vie."
               "\nL’usager perd le combat si son total aux dés est inférieur (ou égal) à la force du monstre."
               "\nDans ce cas l’usager perdra autant de points de vie que la force du monstre affronté."
               "\nL’usager commence la partie avec un pactole de points de vie.\n")

    elif question=="4":
        exit()
