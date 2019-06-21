import csv

path = 'testfileread.txt'
with open(path, "r") as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row[0])
        print(row[1])        