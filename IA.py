# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:30:49 2018

@author: PE_102
"""
from Player import Player
from random import random
from Trump import Trump
from Excuse import Excuse


class IA(Player):
    def __init__(self, hand, score, name):
        Player.__init__(self, hand, score, name)

    def play(self, trick):
        playable_cards = Player.playable_cards(self, trick)
        self.get_hand().remove(playable_cards[0])
        return (playable_cards[0])

    def bid(self):
        """Pour comprendre cette fonction, se réfèrer au tableau Wikipédia"""
        points = 0  # Nombre de points attribués à la main
        trumps = 0  # Nombre d'atouts dans la main
        petit = False
        hearts = []
        clovers = []
        diamonds = []
        spades = []
        # A est un dictionnaire permettant de trier les cartes par couleur
        A = {'S': spades, 'H': hearts, 'D': diamonds, 'C': clovers}
        for card in self.get_hand():
            if isinstance(card, Trump):
                trumps += 1  # On compte un atout en plus
                if card.get_rank() > 15:  # 2 pts en + pour les gros Atouts
                    points += 2
                elif card.get_rank() == 1:  # Présence du petit
                    petit = True
                if card.get_rank() == 21:  # Le 21 vaut 10 pts
                    points += 10
            elif isinstance(card, Excuse):  # L'Excuse vaut 8 pts
                points += 8
            else:
                A[card.get_suit()].append(card)
        if petit:  # Le petit vaut un nombre != de pts selon le nbre d'atouts
            if trumps == 5:
                points += 5
            elif trumps == 6:
                points += 7
            elif trumps > 6:
                points += 9
        if trumps > 4:  # 2 pts pour chaque atout s'ils sont assez nombreux
            points += 2*trumps
        for couleur in ['H', 'S', 'D', 'C']:  # Des ots pour les suites
            liste = A[couleur]
            if len(liste) == 5:
                points += 5
            elif len(liste) == 6:
                points += 7
            elif len(liste) > 6:
                points += 9
            for card in liste:
                if card.get_rank() == 14:  # 6 pts pour chaque Roi
                    points += 6
                elif card.get_rank() == 13:  # 3 pts pour chaque Dame
                    points += 3
                elif card.get_rank() == 12:  # 2 pts pour chaque Cavalier
                    points += 2
                elif card.get_rank() == 11:  # 1 pt pour chaque Valet
                    points += 1
        """A faire: major trump in a suit, for garde-contre and K and Q of same suit"""
        print(points)
        points = points*(0.9+0.2*random())  # On ajoute un peu de hasard
        print(points)
        if points < 40:
            return 'Passe'
        elif points < 56:
            return 'Petite'
        elif points < 71:
            return 'Garde'
        elif points < 81:
            return 'Garde Sans'
        else:
            return 'Garde Contre'


if __name__ == '__main__':
    pass
