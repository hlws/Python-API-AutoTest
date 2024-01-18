import csv
rows=[("序号","姓名","年龄"),("10","lst","11"),("11","qyr","15")]
with open("b.csv","w",encoding="utf-8") as b:
    b_csv=csv.writer(b)
    b_csv.writerows(rows)
