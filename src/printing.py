import csv
with open("test.csv", "r") as f:
    read = csv.reader(f, delimiter = " ")
    for i in read:
        print i                  
