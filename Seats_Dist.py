#Calculating the number of seats for each winning party
import csv
prty = []
votes = []
seats = []
states = []
pop = []
p_div = [] # to input the divisory value for each party, needed in part 2
ps_stat = [] # to input the number of seats for each party / state
d = 0
v = 0
n = 601
with open('E:\Courses\DSP\output.csv') as csvfile:  # open the CSV file
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        prty.append(row[0])
        votes.append(int(row[1]))
# Calculate value of v (total number of votes
    for x in range(prty.__len__()):
        v = v + int(votes[x])
# Calculate the divisor
    d = round(int(v/n),1)

# Number of seats claculation according to the value of d
    for x in range(prty.__len__()):
        seats.append(round(int(votes[x]/d),0))
        print(str(prty[x])+ ' ; ' + str(votes[x]) + ' ; ' +str(seats[x]))

print ('##############################################################################################################')
