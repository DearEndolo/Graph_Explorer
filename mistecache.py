from model import *
from Fenetre import *

def main():
    """Procédure principale"""
    fini = False
    mistecache = creerMistecache()
    print(type(mistecache))
    # fenetre = Fenetre()
    print("Bienvenue sur Mistecache ! Comment allez vous ? :D")
    while not(fini):
        print("Que voulez vous voir ?")
        msg = input("")
        help = regex.match(r"^help (.*)$", msg)
        if(help):
            affiche_aide(help.group(1))
        ajouteregex = regex.match(r"^add (.*) isa (.*)$", msg)
        if(ajouteregex):
            name = ajouteregex.group(1)
            concepts = ajouteregex.group(2).split(",")
            list_concepts = list()
            for concept in concepts:
                concept = skip_spaces(concept)
                list_concepts.append(concept)
            print(type(mistecache))
            ajoute(mistecache, name, list_concepts)

        #nomInstance ->nomAttr -> valeur
        ajouteAtt = regex.match(r"^addAttribut (.*) (.*) (.*)$", msg)
        if(ajouteAtt):
            name = ajouteAtt.group(1)
            attributKeyName = ajouteAtt.group(2)
            value = ajouteAtt.group(3)
            ajouteAtt(name, attributKeyName, value)

        #nomInstance -> nomAttr -> nouvelle valeur
        changeAttr = regex.match(r"^changeAttr (.*) (.*) (.*)$", msg)
        if(changeAttr):
            nomInstance = changeAttr.group(1)
            nomAttr = changeAttr.group(2)
            valeur = changeAttr.group(3)
            changeAttribut(nomInstance, nomAttr, valeur)

        #nomInstance -> suppression
        supprimeNoeud = regex.match(r"^delete (.*)$", msg)
        if(supprimeNoeud):
            nomInstance = supprimeNoeud.group(1)
            noeud = mistecache.search(nomInstance)
            if(type(noeud) == InstanceNode):
                mistecache.deleteNode(noeud)
            else:
                print("")
                print("------------- ERROR -------------")
                print("Ce noeud n'est pas une instance et ne peut donc pas être supprimé.")
                print("---------------------------------")
                print("")


if __name__ == "__main__":
    # execute only if run as a script
    main()
