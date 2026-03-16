"""
Pseudo Code:
Get The User_input
Remove a e i o u or A E I O U
Print the output

"""
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
user_input = str(input("Type: "))
print(f"{user_input.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '').replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')}")

# if 'a' 'e' 'i' 'o' 'u' 'A' 'E' 'I' 'O' 'U' in user_input:
#     print(f"{user_input.replace('a' 'e' 'i' 'o' 'u' 'A' 'E' 'I' 'O' 'U', '')}")




