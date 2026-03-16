SHOWS = [
    "Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    "Spongebob Squarepants",
    "Phineas and ferb",
    "Kim Possible",
    "Jimmy Neutron",
    "the proud family"
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        # print(show.capitalize())
        cleaned_shows.append(show.strip().title())
    

    print('.'.join(cleaned_shows))

main()
