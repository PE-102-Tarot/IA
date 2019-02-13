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
        points_garde = 0 # points comptabilisé que pour  garde sans/contre
        petit = False
        hearts = []
        clovers = []
        diamonds = []
        spades = []
        mayor_trump = []
        # A est un dictionnaire permettant de trier les cartes par couleur
        A = {'S': spades, 'H': hearts, 'D': diamonds, 'C': clovers}
        for card in self.get_hand():
            if isinstance(card, Trump):
                trumps += 1  # On compte un atout en plus
                if card.get_rank() > 15:  # 2 pts en + pour les gros Atouts
                    points += 2
                    mayor_trump.append(card.get_rank())  #liste des ranks des mayor trumps
                elif card.get_rank() == 1:  # Présence du petit
                    petit = True
                if card.get_rank() == 21:  # Le 21 vaut 10 pts
                    points += 10
            elif isinstance(card, Excuse):  # L'Excuse vaut 8 pts
                points += 8
            else:
                A[card.get_suit()].append(card)
                
                # on ajoute 1 points pour chaque mayor trump en séquence 
        if len(mayor_trump) > 1:        
            list.sort(mayor_trump)
            seq= False  # Pour savoir si les 2 cartes précédente était déjà en sequence
            for i in range (len(mayor_trump)-1):                
                if (mayor_trump[i] - mayor_trump[i+1]) == -1:
                    if seq:
                        points +=1
                        seq=True
                    else:
                        points +=2
                        seq=True
                else:
                     seq=False                                   
        
        if petit:  # Le petit vaut un nombre != de pts selon le nbre d'atouts
            if trumps == 4:
                points += 5
            elif trumps == 5:
                points += 7
            elif trumps > 5:
                points += 9
        if trumps > 4:  # 2 pts pour chaque atout s'ils sont assez nombreux
            points += 2*trumps
            
        for couleur in ['H', 'S', 'D', 'C']:  # Des pts pour les suites
            liste = A[couleur]
            if len(liste) == 5:
                points += 5
            elif len(liste) == 6:
                points += 7
            elif len(liste) > 6:
                points += 9
            elif len(liste) == 0:
                points_garde += 6
            elif len(liste) == 1:
                points_garde += 3
            if (king in liste and queen in liste): #10 pts pour K et Q de même couleur
                points +=10
                liste.remove("king")
                liste.remove("queen")                
            for card in liste:
                if card.get_rank() == 14:  # 6 pts pour chaque Roi
                    points += 6
                elif card.get_rank() == 13:  # 3 pts pour chaque Dame
                    points += 3
                elif card.get_rank() == 12:  # 2 pts pour chaque Cavalier
                    points += 2
                elif card.get_rank() == 11:  # 1 pt pour chaque Valet
                    points += 1
        """A faire: major trump in a suit (c'est fait), for garde-contre (c'est fait) and K and Q of same suit (c'est fait)"""
        points = points*(0.9+0.2*random())  # On ajoute un peu de hasard
        
        if (points + points_garde) > 80:
            return 'Garde Contre'
        elif (points + points_garde) > 70:
            return 'Garde Sans'
        elif points > 55:
            return 'Garde'
        elif points > 39:
            return 'Prise'
        else:
            return 'Passe'

if __name__ == '__main__':    
    pass

