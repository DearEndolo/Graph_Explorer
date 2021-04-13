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

    rel = Relation()

    poisson.addExit(animal,rel.get("isa"))
    viande.addExit(animal,rel.get("isa"))
    animal.addExit(ingredient,rel.get("ako"))
    vegetal.addExit(ingredient,rel.get("ako"))
    ingredient.addExit(nourriture,rel.get("ako"))
    ingredient.addExit(recette,rel.get("part_of"))
    entree.addExit(recette,rel.get("ako"))
    plat.addExit(recette,rel.get("ako"))
    dessert.addExit(recette,rel.get("ako"))
    recette.addExit(nourriture,rel.get("ako"))

    nourriture.addAttr("Description", "MIAM MIAM :^)")

    ensemble = [nourriture,recette,entree,plat,dessert,ingredient,vegetal,animal,viande,poisson]
    mistecache = Graph(ensemble)
    mistecache.relation = rel

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
            print(f"Le noeud {node.name} n'existe pas")
        else:
            node.show(graph)
            tab = node.getEntries()
            res.append(node)
            res += tab

            for elem in tab:
                elem.show(graph)
    return res



def ajoute(graph, name, listConcepts):
    newNode = InstanceNode(name)
    graph.addNode(newNode)
    for concept in listConcepts:
        conceptNode = graph.search(concept)
        if(conceptNode == None):
            print(f"Le noeud {conceptNode} n'existe pas")
        else:
            print(graph.getRelation("isa"))
            newNode.addExit(conceptNode, graph.getRelation("isa"))
            print(newNode.getWeight(conceptNode))



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


def sauvegarde(graph, nomFichier="data.json"):

    data = {}
    listNoeuds = graph.getNodeSet()
    rel = Relation()
    for noeud in listNoeuds:


        temp = {
            "name": noeud.name,
            "isOriented": noeud.isOriented,
            "InstanceNode": type(noeud) == InstanceNode,
            "ConceptNode": type(noeud) == ConceptNode,
            "attribut" : noeud.getAllAttr()
        }
        temp["previousNodes"] = {}
        temp["nextNodes"]= {}
        for noeudPrec in noeud.previousNodes:
            temp["previousNodes"][noeudPrec.name]=rel.getNameByValue(noeud.getWeight(noeudPrec))

        for noeudSuiv in noeud.nextNodes:
            temp["nextNodes"][noeudSuiv.name]=rel.getNameByValue(noeud.getWeight(noeudSuiv))

        data[noeud.name]=temp

    with open(nomFichier, "w") as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)

def chargerSauvegarde(nomFichier="data.json"):
    nomNouvNoeud=""
    ensemble=[]
    rel = Relation()
    with open(nomFichier) as json_file:
        data = json.load(json_file)
        for node in data:
            for Key in data[node]:
                if Key=="name":
                    nomNouvNoeud = data[node][Key]
                if Key == "InstanceNode" and data[node][Key]:
                    NouveauNoeud = InstanceNode(nomNouvNoeud)
                    ensemble.append(NouveauNoeud)
                if Key == "ConceptNode" and data[node][Key]:
                    NouveauNoeud = ConceptNode(nomNouvNoeud)
                    ensemble.append(NouveauNoeud)
                if Key == "attribut" and data[node][Key] and isinstance(data[node][Key], dict):
                    for attribut in data[node][Key]:
                        NouveauNoeud.addAttr(attribut, data[node][Key][attribut])

        NouveauGraph=Graph(ensemble)

        for node in data:
            for Key in data[node]:
                if Key == "previousNodes" and isinstance(data[node][Key], dict) and not (not (data[node][Key])):

                    for entree in data[node][Key]:

                        NouveauGraph.search(node).addEntry(NouveauGraph.search(entree), rel.get(data[node][Key][entree]))


                if Key == "nextNodes" and isinstance(data[node][Key], dict) and not (not (data[node][Key])):

                    for sortie in data[node][Key]:

                        NouveauGraph.search(node).addExit(NouveauGraph.search(sortie), rel.get(data[node][Key][sortie]))


def displayNode(graph, name):
    node = graph.search(name)
    if(node==None):
        print(f"Le noeud {name} n'existe pas")
        return
    else:
        node.show(graph)


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


def link(graph, name1, rel, name2):
    node1 = graph.search(name1)
    if(node1==None):
        print(f"Le noeud {name1} n'existe pas")
        return
    if(type(node1) != InstanceNode):
        print(f"Le noeud {name1} n'est pas une instance'")
        return

    node2 = graph.search(name2)
    if(node2==None):
        print(f"Le noeud {name2} n'existe pas")
        return
    if(type(node2) != InstanceNode):
        print(f"Le noeud {name2} n'est pas une instance'")
        return
    if(graph.getRelation(rel) == None or graph.getRelation(rel) != graph.getRelation("isa")):
        node1.addExit(node2,graph.fetchRelation(rel))
    else:
        print("Ce lien ne peut être utilisé qu'entre une instance et un concept.")

def fromNodeToNode(graph,name1,name2):
    node1 = graph.search(name1)
    if(node1==None):
        print(f"Le noeud {name1} n'existe pas")
        return

    node2 = graph.search(name2)
    if(node2==None):
        print(f"Le noeud {name2} n'existe pas")
        return

    newGraph = graph.fromNodeToNode(node1,node2)
    if(newGraph != None):
        tab = newGraph.deep_traversal(node1)
        for i in range(len(tab)-1,-1,-1):
            for elem in tab[i]:
                elem.show(graph)
        return tab
    else:
        print("Aucun chemin n'a été trouvé.")

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
