from guizero import *

from GraphExplorer import Graph
from .Vectors import *
from .Couleurs import *

class Fenetre(App):
    HEIGHT = 500
    WIDTH = 900

    CANVAS_HEIGHT = 450
    CANVAS_WIDTH = 450

    def __init__(self):
        super().__init__()
        self._initWidgets()
        self.model = None # On va pointer vers l'obj de graph ici
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
                                   [["Quitter", self.quitter]]
                               ])

        # Les Layouts
        layoutGauche = Box(self, align="left", height="fill", width="fill", border=True)
        layoutDroit = Box(self, align="right", height="fill", width=int(self.WIDTH / 3), border=True)

        # le canvas ou on va dessiner notre graph
        self.canvas = Drawing(layoutGauche)
        self.canvas.height = self.CANVAS_HEIGHT
        self.canvas.width = self.CANVAS_WIDTH

        # Les labels
        self.labelNbInstances = Text(layoutDroit, "il y a XX instances ()", align="top")
        self.labelNbConcept = Text(layoutDroit, "il y a XX concepts ()", align="top")


    def updateCanvas(self):
        """Met a jour le visuel du canvas"""
        self.canvas.clear()
        self.canvas.rectangle(0, 0, self.CANVAS_WIDTH, self.CANVAS_HEIGHT, color=Couleurs.BLANC)
        # Test
        # self.dessinePoint(None, Vector2D(50, 50), coul=Couleurs.ROUGE)
        # self.dessineLigne(Vector2D.ZERO(), Vector2D(80, 80), coul= Couleurs.BLEU)


    def dessinePoint(self, noeud, pos: Vector2D, taille: int= 50, coul: Couleurs = Couleurs.DEFAUT):
        taille = taille / 2
        self.canvas.oval(pos.getX() -taille, pos.getX() -taille, pos.getX() +taille, pos.getX() +taille, color=coul)
        self.canvas.text(pos.getX() -taille, pos.getY() -taille + 10, text="Un text popop", size=int(taille/2))


    def dessineLigne(self, de: Vector2D, vers: Vector2D, txt=None, taille: int= 2, coul: Couleurs = Couleurs.DEFAUT):
        self.canvas.line( de.getX(), de.getY(), vers.getY(), vers.getY(), width=taille, color=coul )


    def quitter(self):
        """ Est appelée quand on ferme la fentre."""
        print("Quitter")
        self.destroy()

# ========================
# Getter & setters

    def setModel(self, graph: Graph):
        self.model = graph
        self.updateCanvas()