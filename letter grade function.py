def letter_grade(number_grade):
    #this functions translates number grades into letter grades

    if number_grade >= 90:
        print("A")
    elif number_grade >= 80 and number_grade <= 89:
        print("B")
    elif number_grade >= 70 and number_grade <= 79:
        print("C")
    elif number_grade >= 61 and number_grade <= 69:
        print("D")
    else:
        print("F")


letter_grade(88)

input()
        
