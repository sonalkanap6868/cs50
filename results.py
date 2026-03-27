results = ["Mario", "Luigi"]

results.append("princess")
results.append("yoshi")
results.append("Koopa Troopa")
results.append("toad")

results.append(["Bowser", "Donkeykong. Jr"])

results.remove(["Bowser", "Donkeykong. Jr"])
results.extend(["Bowser", "Donkeykong. Jr"])

results.remove("Bowser")

results.insert(0, "Bowser")

results.reverse()


print(results)
