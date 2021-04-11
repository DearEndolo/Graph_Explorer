from model import *

def main():
    """Procédure principale"""
    fini = False
    mistecache = creerMistecache()
    print("Bienvenue sur Mistecache ! Comment allez vous ? :D")
    while not(fini):
        print("Que voulez vous voir ?")
        msg = input("")
        help = regex.match(r"^help (.*)$", msg)
        if(help):
            affiche_aide(help.group(1))
        ajoute = regex.match(r"^add (.*) isa (.*)$",msg)
        if(ajoute):
            name = ajoute.group(1)
            concepts = ajoute.group(2).split(",")
            list_concepts = list()
            for concept in concepts:
                concept = skip_spaces(concept)
                list_concepts.append(concept)
            ajoute(mistecache,name, list_concepts)

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
        supprimeNoeud = regex.match(r"^supprime (.*)$", msg)
        if(supprimeNoeud):
            nomInstance = supprimeNoeud.group(1)
            noeud = search(mistecache,nomInstance)
            deleteNode(noeud)



if __name__ == "__main__":
    # execute only if run as a script
    main()
