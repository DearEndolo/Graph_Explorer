import mistecache
from GraphExplorer import *
from sys import *
import re as regex
import json

from GraphExplorer.conceptNode import ConceptNode
from GraphExplorer.instanceNode import InstanceNode

from TypeEnum import *

def creerMistecache():
    """CONSTANTE ATTRIBUTS"""


    """Fonction qui créer puis retourne le graphe de Mistecache"""

    nourriture = ConceptNode("Nourritures")
    recette = ConceptNode("Recettes")
    entree = ConceptNode("Entrées")
    plat = ConceptNode("Plats")
    dessert = ConceptNode("Dessert")
    ingredient = ConceptNode("Ingrédients")
    vegetal = ConceptNode("Végétal")
    animal = ConceptNode("Animal")
    viande = ConceptNode("Viande")
    poisson = ConceptNode("Poisson")


    poisson.addExit(animal,Relation.ISA)
    viande.addExit(animal,Relation.ISA)
    animal.addExit(ingredient,Relation.AKO)
    vegetal.addExit(ingredient,Relation.AKO)
    ingredient.addExit(nourriture,Relation.AKO)
    ingredient.addExit(recette,Relation.PARTOF)
    entree.addExit(recette,Relation.AKO)
    plat.addExit(recette,Relation.AKO)
    dessert.addExit(recette,Relation.AKO)
    recette.addExit(nourriture,Relation.AKO)


    ensemble = [nourriture,recette,entree,plat,dessert,ingredient,vegetal,animal,viande,poisson]
    mistecache = Graph(ensemble)
    return mistecache



def affiche_aide(topic):
    """Affiche l'aide en fonction du topic"""
    if (topic=="add"):
        print(f"==== HELP {topic.upper()} ====")
        print("The command add create an instance of one or multiple concept(s)")
        print("-- SYNTAX --")
        print("add <instanceName> isa <conceptNode>")
        print("add <instanceName> isa <conceptNode>, <conceptNode>")
        print("-- EXAMPLE --")
        print("add Hareng isa Poisson")
        print("add Melon - Jambon cru isa Entrée, Dessert")
    elif (topic=="addAttr"):
        print(f"==== HELP {topic.upper()} ====")
        print("The command update the attributs of a instance")
        print("-- SYNTAX --")
        print("changeAttr <instanceName> <attributKeyName> <value> ")
        print("-- EXAMPLE --")
        print("changeAttr Hareng ph 7")
        print("changeAttr Melon circonférance 18")
    elif (topic=="changeAttr"):
        print(f"==== HELP {topic.upper()} ====")
        print("The command update the attributs of a instance")
        print("-- SYNTAX --")
        print("changeAttr <instanceName> <attributKeyName> <value> ")
        print("-- EXAMPLE --")
        print("changeAttr Hareng ph 7")
        print("changeAttr Melon circonférance 18")
    elif (topic=="all"):
        print(f"==== HELP {topic.upper()} ====")
        affiche_aide("add")
        affiche_aide("addAttr")
        affiche_aide("changeAttr")
    else:
        print("------- ERROR -------")
        print("Cette commande n'existe pas.")
        print("---------------------")




def skip_spaces(mot):
    while mot[0] == " ":
        mot = mot[1:]
    while mot[len(mot)-1] == " ":
        mot = mot[0:len(mot)-2]
    return mot



def recherche(graph, liste_nom):
    res = list()
    for nom in liste_nom:

        node = graph.search(nom)
        if(node == None):
            print(f"Le noeud {name} n'existe pas")
        else:
            node.show()
            tab = node.getEntries()
            res.append(node)
            print(node)
            res += tab

            for elem in tab:
                print(elem)
    return res



def ajoute(graph, name, listConcepts):
    newNode = InstanceNode(name)
    graph.addNode(newNode)
    for concept in listConcepts:
        conceptNode = graph.search(concept)
        if(conceptNode == None):
            print(f"Le noeud {conceptNode} n'existe pas")
        else:
            newNode.addExit(conceptNode, relation.Relation.INSTANCE)



def ajouteAttr(graph, name, attributKeyName, value):
    noeud = graph.search(name)
    if(noeud == None):
        print(f"Le noeud {name} n'existe pas")
        return
    if noeud.getAttr(attributKeyName):
        print(f"L'attribut {attributKeyName} exise déjà, sa valeur est : {noeud.getAttr(attributKeyName)} ")
        return
    noeud.addAttr(attributKeyName, value)



def changeAttribut(graph, name, attributKeyName, value):
    noeud = graph.search(name)
    if(noeud == None):
        print(f"Le noeud {name} n'existe pas")
        return
    if noeud.getAttr(attributKeyName)==None:
        print(f"L'attribut {attributKeyName} n'existe pas")
    noeud.updateAttr(attributKeyName, value)



def sauvegarde():
    data = {}
    graph.search("Nourritures")

    with open("data.json", "w") as outfile:
        json.dump(data, outfile)



def displayNode(graph, name):
    node = graph.search(name)
    if(node==None):
        print(f"Le noeud {name} n'existe pas")
        return
    else:
        node.show()



def deleteNode(graph, name):
    noeud = graph.search(name)
    if(node==None):
        print(f"Le noeud {name} n'existe pas")
        return
    if(type(noeud) == InstanceNode):
        graph.deleteNode(noeud)
    else:
        print("------------- ERROR -------------")
        print("Ce noeud n'est pas une instance et ne peut donc pas être supprimé.")
        print("---------------------------------")

def affiche_commandes():
    print("Pour avoir de l'aide tapez :")
    print("------------------")
    print("help all")
    print("------------------")
    print("La liste des commandes possibles sont :")

    print("------------------")
    print("help")
    print("------------------")
    print("")

    print("------------------")
    print("add")
    print("------------------")
    print("")

    print("------------------")
    print("delete")
    print("------------------")
    print("")

    print("------------------")
    print("addAttr")
    print("------------------")
    print("")

    print("------------------")
    print("changeAttr")
    print("------------------")
    print("")

    print("------------------")
    print("search")
    print("------------------")
    print("")

    print("------------------")
    print("display")
    print("------------------")
    print("")

    print("------------------")
    print("finish")
    print("------------------")
    print("")

    print("Vous pouvez consulter l'aide d'une commande en faisant :")

    print("------------------")
    print("help <command>")
    print("------------------")
    print("")