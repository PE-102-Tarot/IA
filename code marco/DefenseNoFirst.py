# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:30:49 2018

@author: PE_102
"""
from player import *
from operator import mod
from trick import *


    
def DefenseNoFirst_play(self,trick, bidder, j,first_player): # fct générale appelée quand une IA en défense doit jouer un pli déjà commencé( j est le nº du pli)
    print('from dnf bidder = ',bidder)
    print('from dnf first_player = ',first_player)
    print('from dnf plie nº = ',j)
    
    print('hello from DefenseNoFirst')
    
    playable_cards=self.playable_cards(trick)
    print('playables_cards= ',playable_cards)
    
    bidder_relatif = mod((bidder - first_player),4)
    print('from dnf bidder_relatif = ',bidder_relatif)
    
    
    presence_excuse=False
    i=0
    for el in playable_cards:
        if el.get_rank()==0: #vérifier que la suite de excuse est bien "excuse"
            presence_excuse=True
            position_excuse=i
            i += 1
    if (j==16 and presence_excuse):   # jouer l'excuse si c'est l'avant dernier plie et quand possède l'excuse          
        return play_DNF(trick,position_excuse,bidder_relatif)
        
    bidder_played= False
    
    if bidder_relatif < len(trick.get_cards()):
        bidder_played = True
        
        
    if bidder_played:  
        return after_bidder(self,trick,bidder_relatif)
    else:
        return before_bidder(self,trick,bidder_relatif)
        
             
    

        
# vérifier pertinence de la fct play        
def play_DNF (self,trick,i,bidder_relatif): #fct en charge de jouer une carte / i correspond à la position de la position de la carte de playable_card à être joué
    playable_cards = self.playable_cards(trick)
    card = playable_cards[i]
    try:
        print(card)
    except:
        print('erreur pour print card à play dnf')
            
    else:
        print('play_DNF va jouer:',card)
    
    
    return card
    
    

def check_if_iam_winner(self,trick,bidder_relatif): 
    print('from check_if_iam_winner' )
    # fct =True si une de mes cartes bat à l'ATT        
    hypo_trick=[] #liste de mes cartes jouables + la carte gagnante de l'att
    hypo_trick.append(trick.get_cards()[0]) #j'ajouter la premiere carte du plie (pour savoir la couleur demandé)
    for el,j in enumerate(trick.get_cards()):
        if j==bidder_relatif:
            hypo_trick.append(el) #j'introduit la carte gagnante de l'att
           
    
    playable_cards=self.playable_cards(trick)
    
    for el in playable_cards:
        hypo_trick.append(el) #j'introduit mes cartes jouables
    print('from check_if_iam_winner hypo_trick =',hypo_trick)   
    position_meilleur_carte= Player.best_card(hypo_trick) - 2 #si la meilleur carte de hypo_trick est mienne, cette variable prend la valeur de la position dans payable_cards de ma meilleur carte
    print('from check_if_iam_winner position_meilleur_carte =',position_meilleur_carte)   
    if Player.best_card(hypo_trick)==1: #cad que je ne peux pas battre la carte de l'attaquant            
        return False , position_meilleur_carte
    else:
        return True , position_meilleur_carte
    
    
    """
    
def check_if_iam_winner_before(trick): # fct =True si une de mes cartes bat les cartes deja joue par la defense 
    hypo_trick=[] #liste de mes cartes jouables + la carte gagnante de l'att
     
    l_trick = len(trick)
    for i in range (l_trick): #je met les cartes joue par la defense
        hypo_trick.append((trick[i])
    
    playable_cards=playable_cards(self, trick)
    l_playable = len(playable_cards)
    
    for e in range(l_playable):
        hypo_trick.append(playable_cards[e]) #j'introduit mes cartes jouables
        
    a = Player.best_card(hypo_trick)
    
    if a < l_trick: #aucune de mes carte gagne la meilleur carte deja joué par un pote defenseur
        play(trick,worst_card(trick)) # reste a optimiser
    else
        
        
      """
   
    
    
def bidder_payable(self,trick,bidder_relatif): # savoir si l'attaquant peut a priori jouer la couleur demandée + savoir la couleur demande
     
    playable_cards=self.playable_cards(trick)
    first_card = trick.get_cards()[0]
    
    if print(first_card) == "Excuse": #si la 1º carte jouée est une excuse
        if len(trick.get_cards()) == 1: #si l'IA est 2º
            first_card = random.choice(playable_cards)
        else: #on prend la couleur du 2º joueur
            first_card = trick.get_cards()[1] 
    else:
        first_card = trick.get_cards()[0]
    
    if isinstance(first_card, Trump): #si first_card est un obj type Trump
        #to do: estimer si il peut gagner le plie
        couleur_demande="T"
        if basic_game.get_data().coupes[bidder_relatif]['max_trump'] != 0:  #si bidder a des atout d'apres database
            return 'oui' , couleur_demande  #la couleur demandé est atout est l'ATT va jouer atout
        else:
            return 'atout_couleur' , couleur_demande #ATT  n'a pas atout et joue une autre couleur (ATT perd le plie)
        
    if isinstance(first_card, Card):
        couleur_demande=trick.get_cards()[0].get_suit()            
        if basic_game.get_data().coupes[bidder_relatif][couleur_demande] == False :#si bidder a couleur_demande d apres database
            return 'oui' , couleur_demande
        else:
            if basic_game.get_data().coupes[bidder_relatif]['max_trump'] != 0: #bidder a des atout d apres database:
                return 'couleur_atout' , couleur_demande #ATT  n'a pas une couleur et joue atout
            else:
                return 'couleur_couleur' , couleur_demande #ATT  n'a pas la couleur et joue une autre couleur (ATT perd le plie)
                
def avoir_couleur_demande(self,trick): #True si j'ai la couleur demandé
    print('from avoir_couleur_demande' )
    a , couleur_demande=bidder_payable(self,trick,bidder_relatif)
    playable_cards=self.playable_cards(trick)
    for el in playable_cards:
        suit=el.get_suit()
        if suit==couleur_demande :
            return True
    return False
    
    
                
def avoir_atout(self,trick): #True si j'ai des atout dans mes cartes jouables
    print('from avoir_atout' )
    playable_cards=self.playable_cards(trick)
    for el in playable_cards:
        if el.get_oulder() == 1: #à vérifier
            return True
    return False

def atout_max(self,trick): #la fct retourne le rang de ton plus grand atout jouable et sa position ds playable_cards
    print('from atout_max' )
    playable_cards=self.playable_cards(trick)
    rank_max=0
    position_atout_max = 10
    i=-1
    for el in playable_cards:
        i += 1
        if el.get_oulder() == 1 :
            if el.get_rank() > rank_max:
                rank_max == el.get_rank()
                position_atout_max = i
                
    return rank_max , position_atout_max

def atout_min(self,trick): #la fct retourne le rang de ton plus petit atout jouable et sa position ds playable_cards
    print('from atout_min' )
    playable_cards=self.playable_cards(trick)
    rank_min=22
    position_atout_min = 0
    i = -1
    for el in playable_cards:
        i += 1
        if el.get_oulder() == 1 :
            if el.get_rank() < rank_max:
                rank_min == el.get_rank()
                position_atout_max = i
    return rank_min , position_atout_min
                    
def jouer_petit(self,trick):
    print('from jouer_petit' )
    playable_cards=self.playable_cards(trick)
    for el in enumerate(playable_cards):
        if el[1].get_oulder() == 1 and el[1].get_rank() == 1: # True si je peux jouer le petit 
            return True , el[0]
    return False , -1
        

       
def jouer_excuse(self,trick): # la fct joue l'excuse si l'ATT gagne le plie par l'instant et qu'on je peux jouer que des atouts/l'excuse
    print('from jouer_excuse' )
     
    playable_cards=self.playable_cards(trick)
    i=-1
    for el in playable_cards:
        i+=1
        if el.get_oulder()!= 1: #True si la carte ≠ de atout/excuse
                return False, 1 #la valeur 1 est arbitraire, elle ne seras pas utilisée
        if el.get_oulder() == 1 and el.get_rank() == 0: #c'est l'excuse
            position_excuse=i
    return True,position_excuse


def proba_apriori(self,trick,couleur_demande,bidder_relatif): #choisir une carte quand l'attaquant n'a pas encore jouer et il peut a priori jouer la couler demandé
    print('from proba_apriori' )
    playable_cards=self.playable_cards(trick)
    if couleur_demande == 'T':
        if avoir_atout(self,trick):
            bidder_atout_max = basic_game.get_data().coupes[bidder_relatif]['max_trump'] #c'est une cote sup de l'atout max du bidder
            mon_atout_max = atout_max(self,trick)[0]
            if mon_atout_max > bidder_atout_max: #je suis sûre de gagner 
                return play_DNF(self,trick,atout_max(self,trick)[1],bidder_relatif)
                 
            else: #je sais pas si je gagne
                return play_DNF(self,trick,worst_card(self,trick),bidder_relatif) #to do: calcul proba de battre l atout que jouras l ATT 
                
    elif couleur_demande in ['S','H','D','C']: 
        if avoir_couleur_demande(self,trick):
            i=-1
            maxi = True
            rank_max = basic_game.get_data().dico[couleur_demande][-1]
            for c in playable_cards:
                i+=1
                if c.get_suit() == couleur_demande:
                    if c.get_rank() == rank_max:
                        return play_DNF(self,trick,i,bidder_relatif)
                        maxi = False
            if maxi:
                return play_DNF(self,trick,worst_card(self,trick),bidder_relatif)
                               
             #to do calcul proba de battre à l ATT
        else:
            if avoir_atout(self,trick):
                return play_DNF(self,trick,atout_min[1],bidder_relatif) 
            else:
                return play_DNF(self,trick,worst_card(self,trick),bidder_relatif) 
        
        
def before_bidder (self,trick,bidder_relatif):   #L'attaquant n'a pas  encore joué dans ce plie
    
    print('hello from before_bidder' )
    a , couleur_demande=bidder_payable(self,trick,bidder_relatif) # savoir si l'attaquant peut a priori jouer la couleur demandée
    if a=="oui":
        return proba_apriori(self,trick,couleur_demande,bidder_relatif) #choisir une carte quand l'attaquant n'a pas encore jouer et il peut a priori jouer la couler demandé
        
    elif a=="atout_couleur": # la défense remporte le plie
        if jouer_petit(self,trick)[0]:
            return play_DNF(self,trick,jouer_petit(self,trick)[1],bidder_relatif)
        else:
             return play_DNF(self,trick,card_max_point(self,trick),bidder_relatif) # à optimiser: remporter des points + garder des cartes qui peuvent remporter d autres plies
                        
    elif a=="couleur_atout":
        if avoir_couleur_demande(self,trick):
            return play_DNF(self,trick,worst_card(self,trick),bidder_relatif)
        else:
            if avoir_atout(self,trick): 
                
                
                bidder_atout_max = basic_game.get_data().coupes[bidder_relatif]['max_trump'] #c'est une cote sup de l'atout max du bidder
                mon_atout_max = atout_max(self,trick)[0]
                if mon_atout_max > bidder_atout_max: #je suis sûre de gagner 
                    return play_DNF(self,trick,atout_max(self,trick)[1],bidder_relatif)
                else: #je sais pas si je gagne
                    return play_DNF(self,trick,worst_card(self,trick),bidder_relatif) #to do: calcul proba de battre l atout que jouras l ATT 
                
            else:
                return play_DNF(self,trick,worst_card(self,trick),bidder_relatif)
    
    elif a=="couleur_couleur": # la défense remporte le plie
        
        if jouer_petit(self,trick)[0]:
            return play_DNF(self,trick,jouer_petit(self,trick)[1],bidder_relatif)
        else:
             return play_DNF(self,trick,card_max_point(self,trick),bidder_relatif) # à optimiser: remporter des points + garder des cartes qui peuvent remporter d autres plies

def worst_card (self,trick): #renvoie la position dans playing_carte de la pire carte (carte couleur nº minimum < atout de nº minimum)
    print('hello from worst_card' )
    rank_min_couleur = 15
    rank_min_atout = 22
    playable_cards=self.playable_cards(trick)
    presence_carte_couleur= False
    i=-1
    for el in playable_cards:
        i+=1
        if el.get_oulder() == 0: #c'est une carte couleur
            presence_carte_couleur= True
            if el.get_rank() < rank_min_couleur:
                rank_min_couleur = el.get_rank()
                position_worst_card = i
            
    if  presence_carte_couleur:
        return position_worst_card
    else:
        i=-1
        for el in playable_cards:
            i+=1
            if el.get_rank() !=0 and el.get_oulder() == 1: # carte atout
                if el.get_rank() < rank_min_atout:
                    rank_min_atout = el.get_rank()
                    position_worst_card = i
    return position_worst_card
    
def card_max_point (self,trick): #le pli est deja gagner, on cherche a mettre la carte couleur avec max point, si absence de carte couleur en playable_cards on joue l'atout de min rank
     print('hello from card_max_point' )
     playable_cards=self.playable_cards(trick)
     point_max = 0
     presence_carte_couleur= False
     rank_min = 21
     i = -1
     for el in playable_cards:
         
         
         i +=1
         if el.get_oulder()== 0: #c'est une carte couleur
             
             presence_carte_couleur= True
             if el.get_point() > point_max:
                 
                 point_max = el.get_point()
                 position_card = i
     if presence_carte_couleur:
         
         return position_card
     else:
         i=-1
         for el in playable_cards:
             i+=1
             if el.get_oulder()== 1 and print(el) != "Excuse": #c'est une carte atout             
                 if el.get_rank()< rank_min:
                     rank_min = el.get_rank()
                     position_card = i
         return position_card
        
    
def after_bidder (self,trick,bidder_relatif):    #L'attaquant à déjà joué dans ce plie
    print('hello from after_bidder' )
    
    if bidder_relatif== Player.best_card(trick.get_cards()):   # True si L'attaquant à joué la meilleur carte par l'instant      
        if check_if_iam_winner(self,trick,bidder_relatif)[0]:  # fct =True si une de mes cartes bat à l'ATT     
            if jouer_petit(self,trick)[0]: #True si je peux jouer le petit
                hypo_trick = []
                hypo_trick.append(trick.get_cards()[0])        #j'introduit la 1º carte
                hypo_trick.append(trick.get_cards()[bidder_relatif]) #j'introduit la carte gagnante de l'att (VERIFIER j)
                playable_cards=self.playable_cards(trick)      
                hypo_trick.append(playable_cards[jouer_petit(self,trick)[1]])  #j'introduit le petit
                if Player.best_card(hypo_trick) == 2: #je joue le petit et je sais que je remporte le plie
                    return play_DNF(self,trick,jouer_petit(self,trick)[1],bidder_relatif)
                else:
                    return play_DNF(self,trick,check_if_iam_winner(self,trick,bidder_relatif)[1],bidder_relatif) #jouer ma meilleur carte
                
            else:
                return play_DNF(self,trick,check_if_iam_winner(self,trick,bidder_relatif)[1],bidder_relatif) #jouer ma meilleur carte
            # reste à optimiser la carte joué
        
                
                    
            
        else:
            if jouer_excuse(self,trick)[0]:
                position_excuse=jouer_excuse(self,trick)[1]
                return play_DNF(self,trick,position_excuse,bidder_relatif)
                                
            else:   #  jouer la carte la plus petite (reste à optimiser la carte joué )
                return play_DNF(self,trick,worst_card(self,trick),bidder_relatif)
                
    else: #la defense remporte le plie
        if jouer_petit(self,trick)[0]:                
            return play_DNF(self,trick,jouer_petit(self,trick)[1],bidder_relatif)
            
        else:
             return play_DNF(self,trick,card_max_point(self,trick),bidder_relatif)
             

            

                        
        
    
    




