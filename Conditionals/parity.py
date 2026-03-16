# def main():
#     x = int(input("What's x?"))

#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")


# def is_even(n):
#     # if n % 2 == 0:
#     #     return True
#     # else:
#     #     return False
#     return n % 2 == 0
    

# main()



#Program 1: To check weather the number is odd or Even without creating a function.
x = int(input("What's x?"))

if x % 2 == 0:
    print("X is Even")

else:
    print("X is Odd")

#Program 2: To check weather the number is odd or Even with creating a function.

def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("X is Even")
    else:
        print("X is Odd")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

def is_even(n):
    return n % 2 == 0


main()


















# x = int(input("What's x?"))

# if x % 2 == 0:
#     print("x is even number")

# else: 
#     print("x is odd number")

