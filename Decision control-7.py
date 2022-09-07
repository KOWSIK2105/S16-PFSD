if __name__ == '__main__':
    n1=int(input("Enter the side 1 : "))
    n2=int(input("Enter the side-2 : "))
    n3=int(input("Enter the side-3 : "))
    if(n1+n2<=3 or n2+n3<=n1 or n3+n1<=n2):
        print("It doesnt form triangle")
    if(n1==n2==n3):
        print("It is equilateral triangle")
    if(n1!=n2!=n3):
        print("It is Scalene triangle")
    if(n1==n2 and n2!=n3):
        print("It is isosceles triangle")
    if(n2==n3 and n3!=n1):
        print("It is isosceles triangle")
    if(n3==n1 and n1!=n2):
        print("It is isosceles triangle")