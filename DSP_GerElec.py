import csv

v = 0
totv = 0
prty = []
# get all party names without duplicates and add them to array prty[] , clculate the total number of votes
with open('E:\Courses\DSP\ergebnisse.csv') as csvfile:  # open the CSV file
    reader = csv.reader(csvfile, delimiter=';')
    csvfile.__next__()  # skip the file header
    for row in reader:
        if row[4] != '-' and row[2] in ('Wahlberechtigte', 'WÃ¤hler', 'UngÃ¼ltige', 'GÃ¼ltige'):
            totv = totv + int(row[4])
        if row[2] in prty or row[2] in ('Wahlberechtigte', 'WÃ¤hler', 'UngÃ¼ltige', 'GÃ¼ltige'):
            continue  # skip duplicates
        else:
            prty.append(row[2])
    csvfile.seek(0)

    ## calculate number of votes per party and output the percentage

    ofile = 'E:\Courses\DSP\output.csv'
    csv = open(ofile, 'w')


    for x in range(prty.__len__()):
        csvfile.__next__()
        for r in reader:
            if prty[x] == r[2] and r[4] != '-':
                v = v + int(r[4])
               # if r[4] != '-':
                  #  v = v + int(r[4])
        if v != 0 and v > 1000000:
            print(prty[x], v, "{0:.0f}%".format(v / totv * 100))
            csv.write(str("{0:.0f}%".format(v / totv * 100)) + ';' + str(prty[x]))
            csv.write('\n')
        csvfile.seek(0)
        v = 0
csvfile.close()