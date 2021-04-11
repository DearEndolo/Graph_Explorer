from guizero import *
from .Vectors import *

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
        self.display()
        self.updateCanvas()


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
        self.canvas.rectangle(0, 0, self.CANVAS_WIDTH, self.CANVAS_HEIGHT, color="white")


    def dessinePoint(self, noeud, pos: Vector2D):
        pass


    def dessineLigne(self, de: Vector2D, vers: Vector2D):
        pass


    def quitter(self):
        """ Est appelée quand on ferme la fentre."""
        print("Quitter")
        self.destroy()