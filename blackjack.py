'''
creating a blackjack game

Dealer: computer
Player: User

Author: SAI KISHORE AKULA
UNIVERSITY OF CINCINNATI

DATE: 01/17/2019

'''

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
            balance = self.total_amount - withdraw_amount
            print("remaining balance {}".format(balance))
        
        





def Main():
    player = input("Enter player Name: ")
    print("{}, Please deposit amount in the bank".format(player))
    deposit_amount = float(input("Amount: "))
    player1_bank = bank(player)
    player1_bank.deposit(deposit_amount)
    dealer_bank = bank("computer")
    dealer_bank.deposit(1000)
    print("****************************************")
    print("Player funds: {}".format(player1_bank.total_amount))

    print("Dealer funds:{}".format(dealer_bank.total_amount))
    print("****************************************")
    print("\n")
    print("Welcome to Black Jack")
    print("\n")
    bet_amount = int(input("enter the bet amount: "))
    player1_bank.withdraw(bet_amount)
    
    
    
    
    
    
    
if __name__== '__main__':
    Main()
