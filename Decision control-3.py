if __name__ == '__main__':
    x=input("Enter the name of student: ")
    n1=int(input("Enter the marks obtained in subject-1 Out of 100 : "))
    n2=int(input("Enter the marks obtained in subject-2 Out of 100 : "))
    n3=int(input("Enter the marks obtained in subject-3 Out of 100 : "))
    n4=int(input("Enter the marks obtained in subject-4 Out of 100 : "))
    n5=int(input("Enter the marks obtained in subject-5 Out of 100 : "))
    total = n1+n2+n3+n4+n5
    average = total/5
    percentage = (total/500)*100
    print("Total Marks obtained by "+x+" in test :"+str(total))
    print("Average Of Marks obtained by "+x+" in test :"+str(average))
    print("Percentage obtained by "+x+" in test :"+str(percentage))
    if(n1 and n2 and n3 and n4 and n5 >40  and percentage > 90):
        print("Student named as " + x + " Passed he is promoted to next class")
    else:
        print("Student named as " + x + " Failed he is not promoted to next class")