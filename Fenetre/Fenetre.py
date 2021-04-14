from guizero import *

from GraphExplorer import Graph, Node, InstanceNode, ConceptNode
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
        self.updateVue()
        self.display()


    def _initWidgets(self):
        self.title = "Mistec' Hachée"
        self.height = self.HEIGHT
        self.width = self.WIDTH
        self.when_closed = self.quitter
        self.bg = Couleurs.GRIS

        # Les options de la barre de menu
        self.menuBar = MenuBar(self,
                               toplevel=["Options"],  # les onglets ["File", "Edit", "..."]
                               options=[
                                   # onglet Option :
                                   [["Quitter", self.quitter], ["Update", self.updateVue]]
                               ])

        # Les Layouts
        layoutGauche = Box(self, align="left", border=False)
        layoutDroit = Box(self, align="right", height="fill", width="fill", border=False)

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
        self.ajouteBtn = PushButton(layBtnAjoute, command=self.ajouteNoeud, text="Ajouter", align="right")

        # Supprimer
        laySuppr = Box(layoutDroit, align="top", width="fill", border=True)
        Text(laySuppr, "Retirer un noeud dans le graph :", align="top")
        self.supprCombo = Combo(laySuppr, width=30, options=[], align="left")
        self.supprBtn = PushButton(laySuppr, command=self.supprimeNoeud, text="Retirer", align="right")

        # aj attr
        layAttrBtnAjoute = Box(layoutDroit, align="top", width="fill", border=True)
        Text(layAttrBtnAjoute, "Ajouter une relation :", align="top")

        layAttrAjoute = Box(layAttrBtnAjoute, align="left")
        self.attrAjouteTypeCombo =Combo(layAttrAjoute, width=30, options=["ISa", "Ako"], align="top")
        self.attrAjouteComboDe = Combo(layAttrAjoute, width=10, options=[], align="left")
        Text(layAttrAjoute, "-->", align="left")
        self.attrAjouteComboVers = Combo(layAttrAjoute, width=10, options=[], align="left")
        self.attrAjouteBtn = PushButton(layAttrBtnAjoute, command=self.ajouteRelation, text="Ajouter", align="right")

        # suppr attr
        layAttrBtnSuppr = Box(layoutDroit, align="top", width="fill", border=True)
        Text(layAttrBtnSuppr, "Retire une relation :", align="top")

        layAttrSuppr = Box(layAttrBtnSuppr, align="left")
        self.attrSupprComboDe = Combo(layAttrSuppr, width=10, options=[], align="left")
        Text(layAttrSuppr, "<- x ->", align="left")
        self.attrSupprComboVers = Combo(layAttrSuppr, width=10, options=[], align="left")
        self.attrSupprBtn = PushButton(layAttrBtnSuppr, command=self.supprimeRelation, text="Rerirer", align="right")


        # Recherche
        layRech = Box(layoutDroit, align="top", width="fill", border=True)
        Text(layRech, "Recherche :", align="top")
        self.rechTextBox = TextBox(layRech, width=60, align="top")
        self.rechBtn = PushButton(layRech, command=self.recherche, text="Chercher", align="top")


    def updateVue(self):
        print("update")
        self.updateCanvas()
        self.updatesValues()

    def updatesValues(self):
        self.ajouteCombo.clear()
        self.supprCombo.clear()
        self.attrAjouteComboDe.clear()
        self.attrAjouteComboVers.clear()
        self.attrSupprComboDe.clear()
        self.attrSupprComboVers.clear()


        nd = self.model.getNodeSet()

        nbInstances = 0
        nbConcept = 0

        for n in nd:
            if type(n) == InstanceNode:
                nbInstances += 1
                self.attrAjouteComboDe.append(n.name)
                self.attrSupprComboDe.append(n.name)
                self.supprCombo.append(n.name)

            if type(n) == ConceptNode:
                nbConcept += 1
                self.ajouteCombo.append(n.name)
                self.attrAjouteComboVers.append(n.name)
                self.attrSupprComboVers.append(n.name)

        self.labelNbInstances.value = f"il y a {nbInstances} instances"
        self.labelNbConcept.value = f"il y a {nbConcept} Concepts "



    def updateCanvas(self):
        """Met a jour le visuel du canvas"""
        self.noeudsPos = {}
        self.canvas.clear()
        self.canvas.rectangle(0, 0, self.CANVAS_WIDTH, self.CANVAS_HEIGHT, color=Couleurs.BLANC)

        ndDep = self.model.getNodeSet()[0]
        print(ndDep)
        tab = self.model.path_in_width( ndDep )

        nbRang = len(tab)
        for ligne in range(0, nbRang): # rang
            nbNoeud = len(tab[ligne])
            for col in range(0, nbNoeud): # colone
                nd = tab[ligne][col]
                pos = Vector2D( (self.CANVAS_WIDTH / nbNoeud) * col*.85 +40 ,
                               (self.CANVAS_HEIGHT / nbRang) * ligne*.85 +40 )
                self.noeudsPos[nd] = pos

        traite = []
        for n in self.noeudsPos.keys():
            if not n in traite:
                traite += [n]
                de= self.noeudsPos[n]
                for enf in n.getExits():
                    if enf in self.noeudsPos.keys():
                        self.dessineLigne(de, self.noeudsPos[enf], coul=Couleurs.NOIR)

        for n in self.noeudsPos.keys():
            if type(n) == ConceptNode:
                self.dessinePoint( n, self.noeudsPos[n], coul=Couleurs.ROUGE )
            else:
                self.dessinePoint(n, self.noeudsPos[n], coul=Couleurs.BLEU)





    def dessinePoint(self, noeud: Node, pos: Vector2D, taille: int= 50, coul: Couleurs = Couleurs.DEFAUT):
        taille = taille / 2
        self.canvas.oval(pos.getX() -taille, pos.getY() -taille, pos.getX() +taille, pos.getY() +taille, color=coul)
        if noeud != None and noeud.name != None:
            self.canvas.text(pos.getX() -taille, pos.getY() -taille + 10, text=noeud.name, size=int(taille/2))


    def dessineLigne(self, de: Vector2D, vers: Vector2D, txt=None, taille: int= 2, coul: Couleurs = Couleurs.DEFAUT):
        self.canvas.line( de.getX(), de.getY(), vers.getX(), vers.getY(), width=taille, color=coul )


    def quitter(self):
        """ Est appelée quand on ferme la fentre."""
        # print("Quitter")
        self.destroy()

# ========================
# Command btn et event

    def ajouteNoeud(self):
        # print("ajouteNoeud")
        if self.ajouteTextBox.value == "":
            info("err", "il manque une valeur.")
            return

        concpt = self.model.search(self.ajouteCombo.value)
        if concpt == None:
            info("err", "Ce concept n'existe pas.")
            return

        nd = InstanceNode(self.ajouteTextBox.value)

        nd.addExit(concpt, self.model.getRelation("isa"))
        self.model.addNode(nd)

        self.ajouteTextBox.clear()
        self.updateVue()


    def supprimeNoeud(self):
        print("supprimeNoeud")
        self.updateVue()
        pass


    def ajouteRelation(self):
        print("ajouteRelation")
        self.updateVue()
        pass


    def supprimeRelation(self):
        print("supprimeRelation")
        self.updateVue()
        pass


    def recherche(self):
        print("Recherche")
        if self.rechTextBox.value == "":
            info("err", "entrez un valeur à chercher")
            return

        nd = self.model.search( self.rechTextBox.value )

        if nd == None:
            info("Rien trouvé", f"impossiblede trouver un noeud \"{self.rechTextBox.value}\"")
            return


        tp = "Concept"
        if type(nd) == InstanceNode:
            tp = "InstanceNode"
        info(f"{nd.name}", nd.__str__() + "\n du type : " + tp)


# ========================
# Getter & setters

    def setModel(self, graph: Graph):
        self.model = graph
        self.updateCanvas()