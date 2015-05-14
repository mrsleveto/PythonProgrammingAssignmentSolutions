#Conversation with a computer, by: Mrs. Leveto
doing_well=input("Hello, are you doing well today? (y/n): ")
if doing_well == "y" or doing_well == "Y":
    print("Wonderful! I'm so glad!")

    reason=input("What has you in such a great mood today? (weather/school/friends): ")
    if reason == "weather":
        print("Yes - the sunshine will do that!")
    elif reason == "school":
        print("Learning something new is great fun!")
    elif reason == "friends":
        print("Friends are the best!")
    else:
        print("Something else then. That's ok, you don't have to explain.")

elif doing_well == "n" or doing_well == "N":
    print("I'm very sorry to hear that.")

else:
    print("I can't understand you, you're mumbling")
    
 
