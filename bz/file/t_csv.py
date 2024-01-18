import csv
with open("a.csv") as  a:
    a_csv=csv.reader(a)
    headers=next(a_csv)
    print(headers)
    for row in a_csv:
        print(row)
