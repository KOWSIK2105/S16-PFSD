import csv
with open("Student.csv","r",newline='') as p:
    stud=csv.reader(p)
    header=next(stud)
    print(header)
    for r in stud:
        print(r)
    p.close()