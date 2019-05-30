# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:30:49 2018

@author: PE_102
"""
from player import *
from DefenseNoFirst import *

from trick import *



class IA(Player):
    def __init__(self, score, name):
        Player.__init__(self, score, name)
        #checked
        

        #appel a play dans game.py ligne 257

    def play(self,trick,bidder,j,first_player):               
        
        trick_cards = trick.get_cards()
        print('le trick_cards est:',trick_cards)
        print('le trick est:',trick)
        
        
        if len(trick_cards) == 0: #IA 1º joueur du plie, par l'instant random, A MODIFIER
            print('hello from IA - len(trick) == 0')
            
            playable_cards=Player.playable_cards(self, trick)
            card = playable_cards[0]
            
        
        else : 
            print('hello from IA - len(trick) != 0')
            score = self.get_score()
            name = self.get_name()            
            card = DefenseNoFirst_play(self,trick, bidder, j,first_player)
            print('from IA fin DefenseNoFirst_play la card est:',card)

        

        #on fait le traitement de joueur une carte (var card)
        self.get_hand().remove(card)
        
        loc = self.get_hand().get_placement()
        x,y = self.get_hand().get_position()
        pos = (0,0)
        #On décale globalement de 20 pixels par rapport à l a position de la main
        if loc == "NORTH":
            pos = ((2*x+7*48)/2-48/2,y+89+25)
        elif loc == "EAST":
            pos = (x+7*48+25,y)
        elif loc == "WEST":
            pos = (x-25-48,y)
        card.play(pos)
        '''card.disable()
        x,y = self.get_hand().get_position()
        card.set_position(x,y-40)'''
        #on retire la carte physiquement et réellement de la main et on la met (désactivée) au dessus de la main en attente
        #print("carte ajoutee au trick")
        print(card.get_name())
        trick.add_card(card,pos)
        


        




    