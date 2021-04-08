from GraphExplorer import ConceptNode, InstanceNode, Graph
import sys
import re as regex


def creerMistecache():
    """CONSTANTE ATTRIBUTS"""

    attributsNourri = {"nom":"","origine":""}
    """Fonction qui créer puis retourne le graphe de Mistecache"""
    nourriture = ConceptNode("Nourritures",)
    recette = ConceptNode("Recettes")
    entree = ConceptNode("Entrées")
    plat = ConceptNode("Plats")
    dessert = ConceptNode("Dessert")
    ingredient = ConceptNode("Ingrédients")
    vegetal = ConceptNode("Végétal")
    animal = ConceptNode("Animal")
    viande = ConceptNode("Viande")
    poisson = ConceptNode("Poisson")



    poisson.addExit(animal)
    viande.addExit(animal)
    




def affiche_aide(topic):
    print(f"---- HELP {topic.upper()} ----")
    match topic:
        case "add":
            print("The command add create an instance of one or multiple concept(s)")
            print("-- SYNTAX --")
            print("add <instanceName> isa <conceptNode>")
            print("add <instanceName> isa <conceptNode>, <conceptNode>")
            print("-- EXAMPLE --")
            print("add Hareng isa Poisson")


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
        ajoute = regex.match(r"add (.*) (.*) (.*)",msg)



















if __name__ == "__main__":
    # execute only if run as a script
    main()
