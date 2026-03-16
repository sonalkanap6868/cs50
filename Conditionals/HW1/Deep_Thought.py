user_input = input("What is the answer to the Great Question of Life, the Universe and Everything?")

match user_input:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    # case "forty two" | "42" | "forty-two" | "forty three":
    #     print("Yes")
    case _:
        print("No")