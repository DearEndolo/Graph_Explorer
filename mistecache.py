from model import *
from Fenetre import *

def main():
    """Procédure principale"""
    fini = False
    mistecache = creerMistecache()
    
    # fenetre = Fenetre(mistecache)
    print("Bienvenue sur Mistecache ! Comment allez vous ? :D")
    affiche_commandes()
    sauvegarde(mistecache)
    # print(mistecache.path_in_width(mistecache.search("Nourritures")))

    while not(fini):
        print("Que voulez vous voir ?")
        msg = input("")

        print("")

        #commande
        helpMsg = regex.match(r"^help (.*)$", msg)
        if(helpMsg):
            affiche_aide(help.group(1))


        #nomInstance -> nomParents
        ajouteregex = regex.match(r"^add (.*) isa (.*)$", msg)
        if(ajouteregex):
            name = ajouteregex.group(1)
            concepts = ajouteregex.group(2).split(",")
            list_concepts = list()
            for concept in concepts:
                concept = skip_spaces(concept)
                list_concepts.append(concept)
            ajoute(mistecache, name, list_concepts)


        #nomInstance ->nomAttr -> valeur
        ajouteAtt = regex.match(r"^addAttr (.*) (.*) (.*)$", msg)
        if(ajouteAtt):
            name = ajouteAtt.group(1)
            attributKeyName = ajouteAtt.group(2)
            value = ajouteAtt.group(3)
            ajouteAttr(mistecache, name, attributKeyName, value)


        #nomInstance -> nomAttr -> nouvelle valeur
        changeAttr = regex.match(r"^changeAttr (.*) (.*) (.*)$", msg)
        if(changeAttr):
            nomInstance = changeAttr.group(1)
            nomAttr = changeAttr.group(2)
            valeur = changeAttr.group(3)
            changeAttribut(mistecache, nomInstance, nomAttr, valeur)


        #nomInstance
        supprimeNoeud = regex.match(r"^delete (.*)$", msg)
        if(supprimeNoeud):
            nomInstance = supprimeNoeud.group(1)
            deleteNode(mistecache, nomInstance)


        afficheNode = regex.match(r"^display (.*)", msg)
        if(afficheNode):
            nomInstance = afficheNode.group(1)
            displayNode(mistecache, nomInstance)


        searchNode = regex.match(r"^search (.*)$")
        if(searchNode):
            concepts = ajouteregex.group(2).split(",")
            list_concepts = list()
            for concept in concepts:
                concept = skip_spaces(concept)
                list_concepts.append(concept)
            recherche(mistecache, list_concepts)


        if(msg == "finish"):
            print("Au revoir ! :D")
            fini = True

        print("")


if __name__ == "__main__":
    # execute only if run as a script
    main()
