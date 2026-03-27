"""
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed

first two letters in a string
total characters = 6 and minimum characters = 2
Numbers used should be at the end int number = end
First number != 0
. or  or punctuation marks are not allowed

"""

# def main():
#     plate = str(input("Plate: "))
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# def is_valid(s):
#     for c in s:
#         if s[0:2].isalpha() and 6 >= len(s) >= 2:
#             if s[-1].isdigit():
#                 for i in range(len(s)):
#                     if s[i] != 0 and s[i].isdigit():
#                         return False
#                     else:
#                         return True
#                         # for j in range(len(s) - i):
#                         #     if s[j].isalpha() == False:
#                         #         return False
#                         #     else:
#                         #         return True
#             else:
#                 return False
            
#         return True

# main()



# def main():
#     plate = str(input("Plate: "))
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# def is_valid(s):

#     if len(s) < 2 or len(s) > 6:
#         return False
#     if not s[0:2].isalpha():
#         return False
#     if not s.isalnum():
#         return False
#     for i in range(len(s)):
#         if s[i].isdigit():
#             if s[i] == '0' or not s[i:].isdigit():
#                 return False
#             break
#     return True
    
# main()



#######################################################################

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")

    else:
        print("Invalid")

def is_valid(s):
    # c = str()
    print("Hi This is Sonal")
    while s[:2].isalpha() and len(s) <= 6 and s[:].isalnum():
            for i, char in enumerate(s):
                if char.isdigit():
                    # Check if everything from this point to the end is digits
                    return s[i:].isdigit()
                    print("RADHA RADHA RADHA RADHA RADHA RADHA")
            return False # No digits found at all

main()



        # if s[2:].isdigit()  :
        #     return s
        # def digits_only_at_end(s):
        #     # Find the index of the first digit




#####################################################################################