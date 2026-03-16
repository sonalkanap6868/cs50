WORDS = {"PAIR": 4,
         "HAIR": 4,
         "CHAIR": 5}

def main():
    print("Welcome to spelling Bee")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left")
        guess = input("GUESS a Word:")

        if guess in WORDS.keys():
            WORDS.pop(guess)
            print(f"Good Job! You scored {WORDS[guess]} points.")
            

    print("That's the game!")