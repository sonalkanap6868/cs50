# def main():
#     text = str(input("What would you like to enter?"))
#     convert(text)
    

# def convert(s):
#     newstr = ""
#     for c in s:
#         if c == c.upper():
#             newstr += "_" + c

#         else:
#             newstr += c

#     print(newstr.lower())

# main()







# def main():
#     # print(input("camelCase: "))
#     camelCase = str(input("camelCase: "))
#     convert(camelCase)

# def convert(s):
#     for c in s:
#         if c == s.isupper():
#             snake_case = s.split('_').lower()
#             print(f"snake_case: {snake_case}")

#         else:
#             pass


# main()


def main():
    # Get input from the user
    camel_case = input("camelCase: ")
    # Convert and print the result
    print(f"snake_case: {convert(camel_case)}")

def convert(s):
    snake_case = ""
    for char in s:
        # If the character is uppercase, add an underscore and the lowercase version
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            # Otherwise, just add the character as it is
            snake_case += char
    return snake_case

if __name__ == "__main__":
    main()

