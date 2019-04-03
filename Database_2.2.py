# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:39:21 2019

@author: axel
"""


class Database():
    def __init__(self):
        # Dictionnaire contenant des listes représentant les cartes non jouées
        self.dico = {'S': [i for i in range(1, 15)],
                     'H': [i for i in range(1, 15)],
                     'D': [i for i in range(1, 15)],
                     'C': [i for i in range(1, 15)],
                     'T': [i for i in range(1, 21)]
                     }
        self.excuse = False
        # Coupe à [spades, hearts, diamonds, clovers, trumps]
        # mex_trump: indique que le joueur
        # ne peut pas jouer au dessus d'un certain atout
        # max_trump = 0 -> le joueur n'a plus d'atout
        self.coupes = ({'S': False, 'H':  False, 'D':  False,
                        'C':  False, 'T':  False, 'max_trump': 21},
                       {'S': False, 'H':  False, 'D':  False,
                        'C':  False, 'T':  False, 'max_trump': 21},
                       {'S': False, 'H':  False, 'D':  False,
                        'C':  False, 'T':  False, 'max_trump': 21},
                       {'S': False, 'H':  False, 'D':  False,
                        'C':  False, 'T':  False, 'max_trump': 21},
                      )
        # Le chien a été révelé: on note les rois et les bouts qu'il contenait
        self.chien = []


if __name__ == '__main__':
    a = Database([1, 2, 3, 4])
    print(a.dico['H'])
    a.dico['H'].pop(13)
    print(a.dico['H'][-1])
    a.__init__([1, 2, 3, 4])
    print(a.dico['H'][-1])
# Chemin d'accès type: basic_game.get_data().dico[card.get_suit()][-1]
# Tel joueur a donné des points (cb?) à l'adversaire dans telle couleur
