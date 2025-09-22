import csv

with open("iriss.csv", "r") as file:   # note the double 's'
    reader = csv.reader(file)
    
    # read header
    header = next(reader)
    print("Header:", header)
    # read first 5 rows
    for i, row in enumerate(reader):
        print(row)
        if i >= 4:  # stop after 5 rows
            break
