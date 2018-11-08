# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:30:49 2018

@author: PE_102
"""
from Player import Player


class IA(Player):
    def __init__(self, hand, score, name):
        Player.__init__(self, hand, score, name)

    def play(self,trick):
        playable_cards=Player.playable_cards(self, trick)
        self.get_hand().remove(playable_cards[0])
        return (playable_cards[0])

if __name__ == '__main__':
    pass
    