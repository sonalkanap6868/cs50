Items = {"Apple": 130,
         "Avacodo": 50, 
         "Sweet Cheerie": 100}


item = input("Which items price would you like to know?")

if item in Items.keys():
    print(f"{Items[item]}")

