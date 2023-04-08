def compavg(name, score1, score2, score3, handicap):
    avgscore = (score1 + score2 + score3) / 3
    avgscorehandicap = (score1 + score2 + score3 + handicap) / 3
    return avgscore, avgscorehandicap

#input
name = input("Please enter the bowler's last name: ")
score1 = int(input("Enter game 1 score: "))
score2 = int(input("Enter game 2 score: "))
score3 = int(input("Enter game 3 score: "))
handicap = int(input("Please enter handicap: "))

#call function
avgscore, avgscorehandicap = compavg(name, score1, score2, score3, handicap)

#output
print("Bowler's last name: ", name)
print("Average score: ", avgscore)
print("Average score with handicap: ", avgscorehandicap)