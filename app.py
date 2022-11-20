

def play_game():
    print("Welcome to the Vim Flashcards game")
    keep_playing = str(input("Would you like to continue playing? (y/n)"))
    
def add_card():
    question = str(input("Enter the flashcard question below \n"))
    answer = str(input("Enter the flashcard answer below \n"))
    add_another = str(input("Would you like to add another card to the deck (y/n) \n"))

def start_app():
    print("\n Welcome To Danny's Vim Flashcards \n")
    print("You can add flashcards to the deck or test your knowledge and play the game \n")
    add_or_play = str(input("To add cards to the deck enter (a) to play the game enter (p) \n"))
    if add_or_play == "a":
        add_card()
    elif add_or_play == "p":
        play_game()

start_app()
