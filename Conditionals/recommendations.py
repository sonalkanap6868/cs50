# def main():
#     difficulty = input("Difficult or Casual? ")
#     players = input("Multilpayer or Single-player? ")

#     if difficulty == "Difficult" :
#         if players == "Multiplayer":
#             recommend("Poker")
#         elif players == "Single-player":
#             recommend("Klondike")
#         else:
#             recommend("Enter a valid number of players")

#     elif difficulty == "Casual":
#         if players == "Multiplayer":
#             recommend("Hearts")
#         elif players == "Single-player":
#             recommend("Clock")
#         else:
#             recommend("Enter a valid number of players")

#     else:
#         print("Enter a valid difficulty")


# def recommend(game):
#     print("You might like", game)


# main()





#Code with New Boolean Expression:

def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual" ):
        print("Enter a valid difficulty")
        return

    player = input("Multi-player or Single-player? ")
    if not (player == "Multi-player" or player == "Single-player" ):
        print("Enter a valid player")
        return
    
    if difficulty == "Difficult" and player == "Multi-player":
        recommend("Poker")
    elif difficulty == "Difficult" and player == "Single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and player == "Multi-player":
        recommend("Hearts")
    else:
        recommend("Clock")

def recommend(game):
    print("You might like", game)


main()