# def main():
#     spacecraft = {"name": "Voyager 1", "distance": 163}
#     print(create_report(spacecraft))



# def create_report(spacecraft):
#     return f"""
#     ---------- REPORT ----------------
#     NAME: {spacecraft["name"]}
#     DISTANCE: {spacecraft["distance"]} AU
#     ----------------------------------
#     """

# main()


# def main():
#     spacecraft = {"name": "James Webb Space Telescope"}
#     spacecraft["distance"] = 0.01
#     print(create_report(spacecraft))



# def create_report(spacecraft):
#     return f"""
#     ---------- REPORT ----------------
#     NAME: {spacecraft["name"]}
#     DISTANCE: {spacecraft["distance"]} AU
#     ----------------------------------
#     """

# main()


# def main():
#     spacecraft = {"name": "James Webb Space Telescope"}
#     print(create_report(spacecraft))



# def create_report(spacecraft):
#     return f"""
#     ---------- REPORT ----------------
#     NAME: {spacecraft.get("name", "Unknown")}
#     DISTANCE: {spacecraft.get("distance", "Unknown")} AU
#     ----------------------------------
#     """

# main()


# def main():
#     spacecraft = {"name": "James Webb Space Telescope"}
#     spacecraft.update({"distance": "0.01", "orbit": "SUN"})
#     print(create_report(spacecraft))


# def create_report(spacecraft):
#     return f"""
#     ---------- REPORT ----------------
#     NAME: {spacecraft.get("name", "Unknown")}
#     DISTANCE: {spacecraft.get("distance", "Unknown")} AU
#     ORBIT: {spacecraft.get("orbit", "Unknown")}
#     ----------------------------------
#     """

# main()



# distances = {
#     "Voyager 1": 163,
#     "Voyager 2": 136,
#     "Pioneer 10": 80,
#     "New Horizons": 58,
#     "Pioneer 11": 44
# }

# def main():
#     for name in distances.keys():
#         print(f"{name} is {distances[name]} AU from Earth")
        

# main()


distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)}m")

def convert(AU):
    return AU * 149597870700
        

main()
