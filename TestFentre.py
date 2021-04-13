"""
Oulalala
je fais des tests avec le fentre po pO poo00 !
"""


from Fenetre import *
from model import creerMistecache

misteca = creerMistecache()
nd = misteca.getNodeSet()
misteca.dijkstra( nd[0] )
nd[0].show()
# fenetre = Fenetre(misteca)