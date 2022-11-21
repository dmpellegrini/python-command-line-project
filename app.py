from peewee import *
from random import randrange

db = PostgresqlDatabase('flashcards', user='', password='',
                        host='localhost', port=5432)

# Classes
class BaseModel(Model):
    class Meta:
        database = db

class Flashcards(BaseModel):
    question = CharField()
    answer = CharField()

# Deck Mode Functions
def view_deck():
    flashcards_list = Flashcards.select()
    for flashcard in flashcards_list:
        print(f"\n{flashcard.id}: Question: {flashcard.question}, Answer: {flashcard.answer}")

def add_card():
    question = str(input("Enter the flashcard question below \n"))
    answer = str(input("Enter the flashcard answer below \n"))
    new_card = Flashcards(question=question, answer=answer)

    add_confirm = str(input("Would you like to add this flashcard add this flashcard (y/n)"))
    if add_confirm == 'y':
        new_card.save()
        print("Flashcard added! \n")
    else:
        print("Flashcard canceled")
        
    add_another = str(input("Would you like to add another card (y/n)"))
    if add_another == 'y':
        add_card()
    else:
        return

def deck_mode():
    print("\nWelcome to Deck Mode\n")
    print("To view your deck enter (view)")
    print("To add a flashcard enter (add)")
    print("To exit enter (exit)\n")
    add_or_view = str(input("(view/add/exit)\n"))
    if add_or_view == 'add':
        add_card()
        deck_mode()
    elif add_or_view == 'view':
        view_deck()
        deck_mode()
    elif add_or_view == 'exit':
        return 
    else:
        print('invalid input try again')
        deck_mode()

# Game Mode Functions
def play_turn(range):
    random_number = randrange(1,range)
    flashcard = Flashcards.get_by_id(random_number)
    answer = str(input(f"\n{flashcard.question}\n"))
    if answer == flashcard.answer:
        print(f"\n{answer} is correct")
        return True
    elif answer != flashcard.answer and answer != 'exit':
        print(f"\n{answer} is incorrect")
        print(f"The correct answer is {flashcard.answer}")
        return False 
    elif answer == 'exit':
        return 'exit' 

def game_mode():
    flashcards_length = len(Flashcards.select())
    score = 0
    turns = 0

    print("\nWelcome to Game Mode\n")
    print("When prompted, answer the question, to stop the game enter (exit) as your answer\n")
    play_on = str(input("Start game? (y/n)\n"))
    while play_on == 'y' and turns < flashcards_length:
        correct = play_turn(flashcards_length)
        if correct == 'exit':
            break
            # play_on = 'n' 
        elif correct:
            score += 1
        turns += 1
        print(f"You've gotten {score} of {turns} flashcards correct\n")


    print("\nThanks for playing!\n")
    play_on = str(input("Would you like to play again? (y/n)\n"))
    if play_on == 'y':
        game_mode()
    elif play_on == 'n':
        return

def start_app():
    print("\nWelcome To Danny's Vim Flashcards\n")
    print("To view your deck and add cards to it, enter (deck)")
    print("To test your VIM knowledge with flashcards enter (game)")
    print("To exit enter (exit)\n")
    deck_or_game = str(input("(deck/game/exit)?\n"))
    if deck_or_game == "game":
        game_mode()
        start_app()
    elif deck_or_game == "deck":
        deck_mode()
        start_app()
    elif deck_or_game == "exit":
        print("\nThanks for using Danny's Vim Flashcards. Goodbye!\n")
        return
    else:
        print('invalid input try again')
        start_app()

start_app()
