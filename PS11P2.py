#function
def compscore(name, exam1, exam2, exam3):
    total = exam1 + exam2 + exam3
    avgscore = total / 3
    return total, avgscore

#input
name = input("Please enter the student's last name: ")
exam1 = int(input("Please enter score 1: "))
exam2 = int(input("Please enter score 2: "))
exam3 = int(input("Please enter score 3: "))

#call function
total, avgscore = compscore(name, exam1, exam2, exam3)

#output
print("Last name: ", name)
print("Total points: ", total)
print("Average exam score: ", avgscore)