rep = ["Joe", "K", "Mike", "Joi", "Luv", "Deckard", "Wallace", "Rachel"]

for name in rep:
    if len(name) == 4 or len(name)>=7:
        print(f"{name} is a NOT replicant")
    else: 
        print(f"{name} is a replicant")