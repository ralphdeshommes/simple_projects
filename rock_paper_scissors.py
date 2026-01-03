import random

class player():
    def __init__(self, name):
        self.name = name
        self.score = 0
    def get_name(self):
        return self.name
    def get_move(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def reset_score(self):
        self.score = 0

def check_winner(user_choice, opponent_choice):

    if user_choice == opponent_choice:
        print(f"Both players chose {user_choice}. It's a tie!")
        return 0
    elif user_choice == 'rock' and opponent_choice == 'scissors':
        the_user.score += 1

        print(f"{the_user.name} wins!")
        return 1
    elif user_choice == 'paper' and opponent_choice == 'rock':
        the_user.score += 1
        print(f"{the_user.name} wins!")
        
        return 0
the_opponent = player("Computer") 
the_user = player("User")
def match():
    print("pick a number:\n 1.rock\n 2.paper\n 3.scissors")


def main():
    choices = {
        1: 'rock',
        2: 'paper',
        3: 'scissors'
    }

    print("Welcome to Rock, Paper, Scissors!")
    print("the rules are simple: 1=rock, 2=paper, 3=scissors")
    print("You will be playing against the computer and who ever gets to 7 points wins the game")
    print("Good luck!")
    user_choice = int(input())
    user_choice = choices[user_choice]
    match()