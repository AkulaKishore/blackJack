'''
creating a blackjack game

Dealer: computer
Player: User

Author: SAI KISHORE AKULA
UNIVERSITY OF CINCINNATI

DATE: 01/17/2019

'''

import random;
import os;

class bank():
    def __init__(self,name,total_amount = 0 ):
        self.name = name
        self.total_amount = total_amount
    def deposit(self,deposit_amount):
        self.total_amount = self.total_amount+deposit_amount

    def withdraw(self,withdraw_amount):
        if withdraw_amount > self.total_amount:
            print("Cannot withdraw more than the balance")
        else:
            self.total_amount = self.total_amount - withdraw_amount
            print("{} remaining balance {}".format(self.name, self.total_amount))
            


class Game():
    deck=  {"Ace of clubs": 1,"Ace of diamonds": 1,"Ace of Hearts": 1,"Ace of spades": 1,"two of clubs": 2,"two of diamonds":2,"two of hearts": 2,"two of spades": 2,"three of clubs": 3,"three of diamonds": 3,"three of hearts": 3 ,"three of spades": 3,"four of clubs": 4 ,"four of diamonds": 4,"four of hearts": 4,"four of spades": 4,"five of clubs": 5,"five of diamonds": 5,"five of hearts": 5,"five of spades": 5,"six of clubs": 6 ,"six of diamonds": 6,"six of hearts": 6,"six of spades": 6,"seven of clubs": 7,"seven of diamonds": 7 ,"seven of hearts": 7,"seven of spades": 7,"eight of clubs": 8 ,"eight of diamonds": 8,"eight of hearts": 8,"eight of spades": 8,"nine of clubs": 9,"nine of diamonds": 9,"nine of hearts": 9 ,"nine of spades": 9 ,"ten of clubs": 10 ,"ten of diamonds": 10 ,"ten of hearts": 10,"ten of spades": 10,"jack of clubs": 10,"jack of diamonds": 10 ,"jack of hearts": 10,"jack of spades": 10,"queen of clubs": 10 ,"queen of diamonds": 10,"queen of hearts": 10,"queen of spades": 10,"king of clubs": 10,"king of diamond": 10,"king of hearts": 10,"king of spades": 10,"ace of clubs": 11,"ace of diamonds":11,"ace of hearts": 11,"ace of spades": 11}
    def __init__(self,is_human,name):
        self.is_human = is_human
        self.name = name
        self.total_sum = 0

    def initial_card_distribution(self):
        card_1 = random.choice(list(Game.deck.items()))
        Game.deck.pop(card_1[0])
        card_2 = random.choice(list(Game.deck.items()))
        Game.deck.pop(card_2[0])
        self.total_sum = self.total_sum+card_1[1]+card_2[1]
        print(self.name+ " card_details\n")
        print(card_1)
        print(card_2)
        print()
        print("sum: ",str(self.total_sum))

    def take_card(self):
        card = random.choice(list(Game.deck.items()))
        Game.deck.pop(card[0])
        self.total_sum = self.total_sum+ card[1]
        print(card)
        
    def count_sum(self):
        return self.total_sum
    

class Main():

    def __init__(self):
        pass

    def check_sum(self,player_sum,dealer_sum = 0):
        if player_sum == 21:
            print("winner winner chicken dinner")
            return 1
        elif dealer_sum == 21 or player_sum >  21:
            print("busted")
            return 0
        elif dealer_sum > 21:
            print("winner winner chicken dinner")
            return 1
        else: return 2
    
        
        
    def main(self):
        player = input("Enter player Name: ")
        print("{}, Please deposit amount in the bank".format(player))
        deposit_amount = float(input("Amount: "))
        player1_bank = bank(player)
        player1_bank.deposit(deposit_amount)
        dealer_bank = bank("computer")
        dealer_bank.deposit(1000)

        while True:
            print("****************************************")
            print("Player funds: {}".format(player1_bank.total_amount))
            print("Dealer funds:{}".format(dealer_bank.total_amount))
            print("****************************************")
            print("Welcome to Black Jack")
            bet_amount = int(input("enter the bet amount: "))
            player_sum = 0
            dealer_sum = 0
            player1 = Game(1,player)
            player1.initial_card_distribution()
            player_sum = player1.count_sum()
            dealer  = Game(0,"dealer")
            dealer.initial_card_distribution()
            result = start.check_sum(player_sum)
            turn = 0 
            while True and player_sum < 21 and dealer_sum < 21:
            
                if turn == 0:
                    choice = input("Hit or Stand \n")
                else:
                    choice = 'stand'
                if choice.lower() == 'hit':
                    player1.take_card()
                    player_sum = player1.count_sum()
                    print(player_sum)
                    result = start.check_sum(player_sum)
                    continue
                elif choice.lower() == 'stand':
                    dealer_sum = dealer.count_sum()
                    turn = 1
                    print(dealer_sum)
                    result = start.check_sum(player_sum, dealer_sum)
                    if result ==2:
                        dealer.take_card()

            if result == 1:
                dealer_bank.withdraw(bet_amount)
                player1_bank.deposit(bet_amount)
                
            else:
                player1_bank.withdraw(bet_amount)
                dealer_bank.deposit(bet_amount)
            print()
            play_again = input("you wanna play again: ")
            if play_again.lower() == 'y':
                if player1_bank.total_amount == 0 or dealer_bank.total_amount ==0:
                    print("No sufficient funds")
                    break
                if os.name == 'nt':
                    _ = os.system('cls')
                continue
            else:
                break

    
            
                
            
    
    
    
    
    
    
if __name__== '__main__':
    start = Main()
    start.main()
