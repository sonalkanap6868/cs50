def main():
    user_text = input("What is the emoticon? ")
    
    # print(convert(user_text))
    convert(user_text)


def convert(text):

    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


# if __name__ == "__main__":
#     main()

main()