from guizero import *

from GraphExplorer import Graph, Node
from .Vectors import *
from .Couleurs import *

class Fenetre(App):
    HEIGHT = 500
    WIDTH = 1000

    CANVAS_HEIGHT = 600
    CANVAS_WIDTH = 600

    def __init__(self, model: Graph):
        super().__init__()
        self._initWidgets()
        self.model = model # On va pointer vers l'obj de graph ici
        self.noeudsPos = {}    # { un noeud : Vector2D } pour dessiner les noeuds sur le canvas

        # On affiche l'application
        self.updateCanvas()
        self.display()


    def _initWidgets(self):
        self.title = "Mistec' Hachée"
        self.height = self.HEIGHT
        self.width = self.WIDTH
        self.when_closed = self.quitter

        # Les options de la barre de menu
        self.menuBar = MenuBar(self,
                               toplevel=["Options"],  # les onglets ["File", "Edit", "..."]
                               options=[
                                   # onglet Option :
                                   [["Quitter", self.quitter], ["Update", self.updateCanvas]]
                               ])

        # Les Layouts
        layoutGauche = Box(self, align="left", border=True)
        layoutDroit = Box(self, align="right", height="fill", width="fill", border=True)

        # le canvas ou on va dessiner notre graph
        self.canvas = Drawing(layoutGauche, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT)
        self.canvas.height = self.CANVAS_HEIGHT
        self.canvas.width = self.CANVAS_WIDTH

        # Les labels
        self.labelNbInstances = Text(layoutDroit, "il y a XX instances ()", align="top")
        self.labelNbConcept = Text(layoutDroit, "il y a XX concepts ()", align="top")

        # Ajouter ---
        layBtnAjoute = Box(layoutDroit, align="top", width="fill", border=True)
        Text(layBtnAjoute, "Ajouter un noeud dans le graph.", align="top")

        layBtnAjouteNoeud = Box(layBtnAjoute, align="left")
        Text(layBtnAjouteNoeud, "Nom :", size=8, align="top")
        self.ajouteTextBox = TextBox(layBtnAjouteNoeud, width=30, align="top")
        self.ajouteCombo = Combo(layBtnAjouteNoeud, width=30, options=[], align="top")
        self.ajouteBtn = PushButton(layBtnAjoute, command=None, text="Ajouter", align="right")

        # Supprimer
        laySuppr = Box(layoutDroit, align="top", width="fill", border=True)
        Text(laySuppr, "Retirer un noeud dans le graph :", align="top")
        self.supprCombo = Combo(laySuppr, width=30, options=[], align="left")
        self.supprBtn = PushButton(laySuppr, command=None, text="Retirer", align="right")

        # aj attr
        layAttrBtnAjoute = Box(layoutDroit, align="top", width="fill", border=True)
        Text(layAttrBtnAjoute, "Ajouter une relation :", align="top")

        layAttrAjoute = Box(layAttrBtnAjoute, align="left")
        self.attrAjouteTypeCombo =Combo(layAttrAjoute, width=30, options=["ISa", "Ako"], align="top")
        self.attrAjouteComboDe = Combo(layAttrAjoute, width=10, options=[], align="left")
        Text(layAttrAjoute, "-->", align="left")
        self.attrAjouteComboVers = Combo(layAttrAjoute, width=10, options=[], align="left")
        self.attrAjouteBtn = PushButton(layAttrBtnAjoute, command=None, text="Ajouter", align="right")

        # suppr attr
        layAttrBtnSuppr = Box(layoutDroit, align="top", width="fill", border=True)
        Text(layAttrBtnSuppr, "Retire une relation :", align="top")

        layAttrSuppr = Box(layAttrBtnSuppr, align="left")
        self.attrSupprComboDe = Combo(layAttrSuppr, width=10, options=[], align="left")
        Text(layAttrSuppr, "<- x ->", align="left")
        self.attrSupprComboVers = Combo(layAttrSuppr, width=10, options=[], align="left")
        self.attrSupprBtn = PushButton(layAttrBtnSuppr, command=None, text="Rerirer", align="right")


        # Recherche
        layRech = Box(layoutDroit, align="top", width="fill", border=True)
        Text(layRech, "Recherche :", align="top")
        self.rechTextBox = TextBox(layRech, width=60, align="top")
        self.rechBtn = PushButton(layRech, command=None, text="Chercher", align="top")


    def updateCanvas(self):
        """Met a jour le visuel du canvas"""
        self.canvas.clear()
        self.canvas.rectangle(0, 0, self.CANVAS_WIDTH, self.CANVAS_HEIGHT, color=Couleurs.BLANC)


    def dessinePoint(self, noeud: Node, pos: Vector2D, taille: int= 50, coul: Couleurs = Couleurs.DEFAUT):
        taille = taille / 2
        self.canvas.oval(pos.getX() -taille, pos.getY() -taille, pos.getX() +taille, pos.getY() +taille, color=coul)
        self.canvas.text(pos.getX() -taille, pos.getY() -taille + 10, text=noeud.name, size=int(taille/2))


    def dessineLigne(self, de: Vector2D, vers: Vector2D, txt=None, taille: int= 2, coul: Couleurs = Couleurs.DEFAUT):
        self.canvas.line( de.getX(), de.getY(), vers.getX(), vers.getY(), width=taille, color=coul )


    def quitter(self):
        """ Est appelée quand on ferme la fentre."""
        # print("Quitter")
        self.destroy()

# ========================
# Getter & setters

    def setModel(self, graph: Graph):
        self.model = graph
        self.updateCanvas()