
numberOfTest = 0
score = 0
scoreCount = 0
total = 0
average = 0

numberOfTest = int(input("Please enter the number of tests you want to average "))
while(numberOfTest > scoreCount):
    score1 = int(input("Please enter a score "))
    scoreCount = scoreCount + 1
    total = (score1 + total)
average = total / numberOfTest
print("the average is ", average)
             
