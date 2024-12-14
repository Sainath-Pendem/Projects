import random
suits={'Hearts','Clubs','Diamonds','Spades'}
ranks={'Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace'}
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.values=values[rank]
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'

    
class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
    
deck=Deck()

class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
        
    def remove(self):
        return self.all_cards.pop()
    
    def add(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
            
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
 
player_one=Player("one")
player_two=Player("two")

deck.shuffle()

for i in range(26):
    player_one.add(deck.deal_one())
    player_two.add(deck.deal_one())
       
import pdb

round=0
game_on = True

while game_on:
    
    round+=1
    print(f'{round} has started')
    
    if len(player_one.all_cards) == 0:
        print('player_two wins')
        game_on=False
        break
    
    if len(player_two.all_cards) == 0:
        print('player_one wins')
        game_on=False
        break
    
    player_one_cards=[]
    player_one_cards.append(player_one.remove())
    
    player_two_cards=[]
    player_two_cards.append(player_two.remove())
    
    at_war=True
    
    while at_war:
        
    
        if player_one_cards[-1].values > player_two_cards[-1].values:
            
            player_one.add(player_one_cards)
            player_one.add(player_two_cards)
            at_war=False
            
        elif player_one_cards[-1].values < player_two_cards[-1].values:
        
            player_two.add(player_one_cards)
            player_two.add(player_two_cards)
            at_war=False
                       
        else :
            print('war')
            
            if len(player_one.all_cards) < 5:
                print('player 2 wins')
                game_on=False
                break
            
            elif len(player_two.all_cards) < 5:
                print('player 1 wins')
                game_on=False
                break
            
            else:
                for i in range(5):
                    player_one_cards.append(player_one.remove())
                    player_two_cards.append(player_two.remove())
                    
