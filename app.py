from peewee import *

db = PostgresqlDatabase('flashcards', user='', password='',
                        host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Flashcards(BaseModel):
    question = CharField()
    answer = CharField()

def view_deck():
    flashcards_list = Flashcards.select()
    for flashcard in flashcards_list:
        print(f"\n Question: {flashcard.question}, Answer: {flashcard.answer}")


def game_mode():
    print("Welcome to the Vim Flashcards game")
    keep_playing = str(input("Would you like to continue playing? (y/n)"))
    
def deck_mode():
    question = str(input("Enter the flashcard question below \n"))
    answer = str(input("Enter the flashcard answer below \n"))
    add_another = str(input("Would you like to add another card to the deck (y/n) \n"))

def start_app():
    print("\n Welcome To Danny's Vim Flashcards \n")
    print("You can add flashcards to the deck or test your knowledge and play the game \n")
    add_or_play = str(input("To add cards to the deck enter (a) to play the game enter (p) \n"))
    if add_or_play == "a":
        game_mode()
    elif add_or_play == "p":
        deck_mode()

# start_app()

view_deck()
