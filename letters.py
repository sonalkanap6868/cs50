# def main():
#     print(write_letter("Mario", "Princess Peach"))
#     print(write_letter("Luigi", "Princess Peach"))
#     print(write_letter("Daisy", "Princess Peach"))
#     print(write_letter("Yoshi", "Princess Peach"))

# def write_letter(receiver, sender):
#     return f"""
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     Dear {receiver},
    
#     You are cordinally invited to a ball at
#     Peach's Castle thisevening, 7.00PM.

#     Sincearly,
#     {sender}
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     """

# main()


# def main():
#     names = ["Mario", "Lungi", "Daisy", "Yoshi"]
#     for i in range(len(names)):
#         print(write_letter(names[i], "Princess Peach"))


# def write_letter(receiver, sender):
#     return f"""
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     Dear {receiver},
    
#     You are cordinally invited to a ball at
#     Peach's Castle thisevening, 7.00PM.

#     Sincearly,
#     {sender}
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     """

# main()



def main():
    names = ["Mario", "Lungi", "Daisy", "Yoshi"]
    for name in names:
        print(write_letter(name, "Princess Peach"))


def write_letter(receiver, sender):
    return f"""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Dear {receiver},
    
    You are cordinally invited to a ball at
    Peach's Castle thisevening, 7.00PM.

    Sincearly,
    {sender}
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

main()