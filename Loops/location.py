import sys

def main():
    coordinates = (42.376, -71.115)
    print(f"latitude: {coordinates[0]}")
    print(f"longitude: {coordinates[1]}")

    latitude, longitude = coordinates
    print(f"latitude: {latitude}")
    print(f"longitude: {longitude}")

    # coordinates[0] = -42.376   .......As you cannot change the element in tuple we can use it 
    # if and only if we know that the values are unchangable.... 
    # Advantage of tuple is it use less memory compared to the lists

    coordinate_tuple = (42.376, -71.115)
    coordinate_list = [42.376, -71.115]

    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")

main()