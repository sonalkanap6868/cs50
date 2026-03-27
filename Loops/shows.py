SHOWS = [
    "Avatar: the last airbender",
    "Ben 10",
    "arthur",
    " Spongebob squareants",
    "Phines and ferb" ,
    "Kim possible",
    "Jimmy Neutron",
    "the proud family"
]


def main():
    cleaned_shows = []
    for show in SHOWS:
        print(show.capitalize())
        print(show.title())
        print(show.strip())
        print(show.strip().title())
        cleaned_shows.append(show.strip().title().upper()) 
        print(cleaned_shows) 
        print(' , ' .join(cleaned_shows))


    print(cleaned_shows)


main()