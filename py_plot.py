# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt;
import numpy as np

plt.rcdefaults()
import matplotlib.pyplot as plt
import csv

prty = []
votes = []
with open('E:\Courses\DSP\output.csv') as csvfile:  # open the CSV file
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        prty.append(row[1])
        votes.append(int(str(row[0]).partition("%")[0]))


#prty = ('CDU','SPD','GRÜNE','FDP','DIE LINKE', 'AfD','CSU')
#y_pos = range(prty.__len__())
y_pos = np.arange(len(votes))
x_pos = np.arange(len(prty))
#votes = [26, 20, 9, 11, 8, 13, 6]

#for r in range(prty.__len__()):
 #   print(prty[r]+","+ str(votes[r]) )

plt.bar(y_pos, votes, align='center', alpha=0.75)
plt.xticks(y_pos, prty)
#plt.yticks(np.arange(15), votes)


plt.ylabel('Votes')
plt.title('Parties')

plt.show()
