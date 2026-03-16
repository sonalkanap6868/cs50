from helpers import get_words, save_counts

def main():
    
    words = get_words("address.txt")
    lowercase_words = [word.lower() for word in words if len(word) > 4]
    counts = {word: lowercase_words.count(word) for word in lowercase_words}

    for word in lowercase_words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    save_counts(counts)

    print(counts)

main()


# def get_words():
#     words = []
#     while True:
#         word = input("Word: ")
#         if word == "":
#             break
#         words.append(word)
#     return words