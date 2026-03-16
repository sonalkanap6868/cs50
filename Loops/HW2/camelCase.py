def main():
    text = str(input("What would you like to enter?"))
    convert(text)
    

def convert(s):
    newstr = ""
    for c in s:
        if c == c.upper():
            newstr += "_" + c

        else:
            newstr += c

    print(newstr.lower())

main()

