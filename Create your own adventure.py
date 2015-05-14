#Create Your Own Adventure, by: Mrs. Leveto
print("Welcome to Mrs. Leveto's 'Create Your Own Adventure'!")

path=input("The tunnel is dark and you can only see a few feet ahead of you by the light of the torch you are holding. \
You stop suddenly when you see the tunnel splits off to the right and to the left. Which path will you take? (R or L): ")

if path == "R" or path == "r":
    print("As you continue down the dark path, you suddenly smell gas. By the time you see the \
    light of the explosion it's too late and you are blown to bits!")
elif path == "L" or path == "l":
    cliff=input("As you continue down the dark path, you start to hear rattling. \
    You realize it is rattle snakes which makes you break out into a run.\
    You push yourself as fast as you can go and finally break out into the light of day. \
    You have to skid to a stop because you realize you are on the edge of a cliff! What do you do? (jump or cry): ")
    if cliff == "jump":
        print("KERSPLAT! You fell to your death")
    elif cliff == "cry":
        print("A bird picks you up and flies you to safety. You made it!")
else:
    print("That is not an option. Your indecisiveness took too long, and the zombies caught up and ate you.")
