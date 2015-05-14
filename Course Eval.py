#COURSE EVAL

outfile = open("course_eval.txt", "w")

print("Please answer the following questions about the 'Intro to Computer Programming' class you took this semester.")
Q1 = input("What did you like about Code Academy? ")
Q2 = input("What did you dislike about Code Academy? ")
Q3 = input("Did the assignments help you apply what you learned in Code Academy? ")
Q4 = input("What did the teacher do that helped you? What could the teacher have done better? ")
Q5 = input("Would you recommend this class to a friend? Why/why not? ")

outfile.write(Q1)
outfile.write(Q2)
outfile.write(Q3)
outfile.write(Q4)
outfile.write(Q5)

outfile.close()

infile = open("course_eval.txt", "r")

print(infile.read())

