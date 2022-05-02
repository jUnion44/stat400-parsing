import csv

l = csv.reader(open('educational attainment.csv'))
count = 0
for row in l:
    count += 1
    if (count - 2) % 19 == 0:
        print(row[0], end=",")
    elif (count - 7) % 19 == 0:
        print(row[16].replace(",",""))