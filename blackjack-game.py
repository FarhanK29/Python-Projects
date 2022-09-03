from operator import truediv
import random

suits = ['Diamonds', 'Clubs','Hearts','Spades']
ranks = ['Ace','Two','Three', 'Four', 'Five', 'Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
values = {'Ace':1,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10, 'Jack':11,'Queen':12,'King':13}

class Card: 
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return f'{self.rank} of {self.suit}'
        


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit,rank)
                self.all_cards.append(new_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces +=1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 11
            self.aces -= 1

class Chip:
    
    def __init__(self,total=100):
        self.total = total
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Place your bet: \n'))
        except:
            print('Please provide an integer!')
        else:
            if chips.bet > chips.total:
                print('Sorry you do not have enough chips. You currently have {} chips'.format(chips.total))
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal_one())

def hit_or_stand(deck, hand):
    global playing
    choice = input('Do you want to hit or stand?: \n').lower()
    if choice == 'hit':
        hit(deck,hand)
    elif choice == 'stand':
        print('Player stands dealers turn.\n')
        playing = False
        

def show_some(player, dealer):
    print('Dealers Hand')
    print('------------')
    print('First card is hidden!')
    print(dealer.cards[1])
    print()
    print("Player's hand")
    print('-------------')
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    print('Dealers Hand')
    print('------------')
    for card in dealer.cards:
        print(card)
    print(f'Value of dealers hand is : {dealer.value}')
    print()
    print("Player's hand")
    print('-------------')
    for card in player.cards:
        print(card)
    print(f'Value of players hand is : {player.value}')

def player_busts(player, dealer, chips):
    print('PLAYER BUSTS!')
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print('PLAYER WINS!')
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print('PLAYER WINS, DEALER BUSTS')
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print('DEALER WINS!')
    chips.lose_bet()
def push(player,dealer):
    print('Player and dealer tie! PUSH')

print('Welcome to Blackjack!')
player_chips = Chip()
dealer_chips = Chip()
while True:    
    playing = True
    print('\n'*50)
    print('Welcome to Blackjack!')
    game_deck = Deck()
    game_deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(game_deck.deal_one())
    player_hand.add_card(game_deck.deal_one())
    dealer_hand.add_card(game_deck.deal_one())
    dealer_hand.add_card(game_deck.deal_one())

    
    take_bet(player_chips)
    print('\n')

    show_some(player_hand, dealer_hand)

    while playing:
        print()
        hit_or_stand(game_deck, player_hand)
        show_some(player_hand, dealer_hand)
        print()
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break


    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(game_deck, dealer_hand)
        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        elif player_hand == dealer_hand:
            push(player_hand, dealer_hand)

    print(f'Player now has {player_chips.total} chips!')

    play_again = input('Would you like to play again? (y or n)').lower()
    if play_again == 'n':
        break
    else:
        print('Thanks for playing!')
        pass


