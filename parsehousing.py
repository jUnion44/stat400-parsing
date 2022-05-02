import csv

l = csv.reader(open('home value.csv'))
count = 0
for row in l:
    count += 1
    if (count - 2) % 5 == 0:
        print(row[0], end=",")
    elif (count - 3) % 5 == 0:
        print(row[101].replace(",",""))