#MAD LIB

outfile = open("madlib.txt", 'w')


player_name = input("What's your name? ")
print("Welcome to Mrs. Leveto's Mad Lib, {0}!".format(player_name))
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")
name = input("Enter a name: ")
verb = input("Enter a verb in present tense: ")
emotion = input("Enter an emotion: ")
school_room = input("Enter a place in a school: ")
verb2 = input("Enter another verb, also in present tense: ")
noun = input("Enter a noun: ")

outfile.write("It was a(n) {0} day at {1} school, when a student named {2} decided to {3}. \
This made the teacher extremely {4}. ".format(adjective, place, name, verb, emotion))
outfile.write("After sending %s to %s, the teacher tried to %s the lesson. \
Unfortunately the rest of the class was too distracted with %s." %(name, school_room, verb2, noun))

outfile.close()
