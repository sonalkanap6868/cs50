# def main():
#     x = int(input("Insert Coin"))
#     Amount_Due(x)

# def Amount_Due(value):
#     value = 50 - x
#     print(value)

Price_Of_Coke = 50
Amount_Due = Price_Of_Coke
for i in range(Price_Of_Coke):
    x = int(input("Insert Coin: "))
    Amount_Due = Amount_Due - x
    i = Amount_Due

    if Amount_Due > 0:
        print(Amount_Due)

    else:
        print("Change_Owed = 0")
        break

    
    # if x > Price_Of_Coke:
    #     Change_Owed = x - Price_Of_Coke
    #     print(Change_Owed)



"""Pseudo Code:
Price of One Coke bottle = 50
Amount Due = 

"""