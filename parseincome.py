import csv

l = csv.reader(open('ACSST5Y2020.S1901-2022-05-02T021649.csv'))
count = 0
for row in l:
    count += 1
    if (count - 2) % 13 == 0:
        print(row[0], end=",")
    elif (count - 4) % 13 == 0:
        print(row[12].replace(",",""))