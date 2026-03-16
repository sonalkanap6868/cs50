def main():
    user_input = input("What time is it?")

    time = convert(user_input)

    if time >= 7.0 and time <= 8.0:
        print("It's breakfast time")
    elif time >= 12.0 and time <= 13.0:
        print("It's lunch time")
    elif time >= 18.0 and time <= 19.0:
        print("It's dinner time")
        

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)

    updated_time = hours + (minutes/60.0)
    return updated_time


if __name__ == "__main__":
    main()