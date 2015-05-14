import random

# Write code for throwing a die (1-6)

dice = random.randint(1,6)

if dice == 1:
    print("one")
elif dice == 2:
    print("two")
elif dice == 3:
    print("three")
elif dice == 4:
    print("four")
elif dice == 5:
    print("five")
else:
    print("six")
    


# Write code for choosing a random classmates name


sixth_period = ["Andrew", "Britni", "Dale", "Kelly", "Maddy"]

print(random.choice(sixth_period))

input()

