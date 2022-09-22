import csv
p=open('D://S16-PFSD/Student.csv','w', newline="")
stud=csv.writer(p)
header=['sno','Name','marks']
lis=[[1,'Ram',88],[2,'Mohan',95],[3,'Kowsik',98]]
stud.writerow(header)
stud.writerows(lis)
print(header)
print(lis)
p.close()