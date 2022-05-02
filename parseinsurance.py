import csv

l = csv.reader(open('health insurance.csv'))
count = 0
for row in l:
    count += 1
    if (count - 2) % 16 == 0:
        print(row[0], end=",")
    elif (count - 10) % 16 == 0:
        print(row[1].replace(",",""))