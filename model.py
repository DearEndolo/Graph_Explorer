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
    print(f"==== HELP {topic.upper()} ====")
    if (topic=="add"):
        print("The command add create an instance of one or multiple concept(s)")
        print("-- SYNTAX --")
        print("add <instanceName> isa <conceptNode>")
        print("add <instanceName> isa <conceptNode>, <conceptNode>")
        print("-- EXAMPLE --")
        print("add Hareng isa Poisson")
        print("add Melon - Jambon cru isa Entrée, Dessert")
    if (topic=="addAttr"):
        print("The command update the attributs of a instance")
        print("-- SYNTAX --")
        print("changeAttr <instanceName> <attributKeyName> <value> ")
        print("-- EXAMPLE --")
        print("changeAttr Hareng ph 7")
        print("changeAttr Melon circonférance 18")
    if (topic=="changeAttr"):
        print("The command update the attributs of a instance")
        print("-- SYNTAX --")
        print("changeAttr <instanceName> <attributKeyName> <value> ")
        print("-- EXAMPLE --")
        print("changeAttr Hareng ph 7")
        print("changeAttr Melon circonférance 18")
    if (topic=="all"):
        affiche_aide("add")
        affiche_aide("addAttr")
        affiche_aide("changeAttr")



def skip_spaces(mot):
    while mot[0] == " ":
        mot = mot[1:]
    while mot[len(mot)-1] == " ":
        mot = mot[0:len(mot)-2]
    return mot

def recherche(graph, liste_nom):
    res = []
    for nom in liste_nom:

        node = graph.search(nom)
        node.show()
        tab = node.getEntries()
        res.append(node)
        print(node)
        res += tab

        for elem in tab:
            print(elem)

    return res

def ajoute(graph, name, listConcepts):
    print(type(graph))
    newNode = InstanceNode(name)
    graph.addNode(newNode)
    for concept in listConcepts:
        conceptNode = graph.search(concept)
        newNode.addExit(conceptNode, relation.Relation.INSTANCE)

def ajouteAtt(graph, name, attributKeyName, value):
    noeud = graph.search(name)
    if noeud.getAttr(attributKeyName):
        print(f"The attribut {attributKeyName} already exist, the value is : {noeud.getAttr(attributKeyName)} ")
        return
    noeud.addAttr(attributKeyName, value)

def changeAttribut(graph, name, attributKeyName, value):
    noeud = graph.search(name)
    if noeud.getAttr(attributKeyName)==None:
        print(f"The attribut {attributKeyName} does not exist")
    noeud.updateAttr(attributKeyName, value)

def sauvegarde(graph):
    data = {}
    data["node"] = {}
    listNoeuds = graph.getNodeSet()
    for noeud in listNoeuds:
        # print(noeud)
        # print( f"name : {noeud.name}"
        #        f" isOriented : {noeud.isOriented} "
        #        f"previousNodes : {noeud.previousNodes} "
        #        f"nextNodes : {noeud.nextNodes}")
        temp = {
            "name": noeud.name,
            "isOriented": noeud.isOriented,
            "InstanceNode": type(noeud) == InstanceNode,
            "ConceptNode": type(noeud) == ConceptNode
        }

        data["node"][noeud.name]=temp
        print(data["node"])
        # self.isOriented = isOriented
        # # Représentation des noeud précedents en dictionnaire python (clé : noeud, valeur : poids de l'arc)
        # self.previousNodes = dict()
        # # Représentation des noeud suivants en dictionnaire python (clé : noeud, valeur : poids de l'arc)
        # self.nextNodes = dict()

    with open("data.json", "w") as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)

