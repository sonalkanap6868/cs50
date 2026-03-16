user_input = input("Expression:")

x, y, z = user_input.split(" ")

x_float = float(x)
z_float = float(z)

if y == "+" :
    print(x_float + z_float)
elif y == "-" :
    print(x_float - z_float)
elif y == "*" :
    print(x_float * z_float)
elif y == "/" :
    print(x_float / z_float)





# # Perform the calculation based on the operator.
# if y == "+":
#     result = x_float + z_float
# elif y == "-":
#     result = x_float - z_float
# elif y == "*":
#     result = x_float * z_float
# elif y == "/":
#     result = x_float / z_float

# # Print the result formatted to one decimal place.
# print(f"{result:.1f}")
