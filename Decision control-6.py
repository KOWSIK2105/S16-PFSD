if __name__ == '__main__':
    x=int(input("Enter x co-ordinate of point : "))
    y=int(input("Enter y-co-ordinate of point : "))
    if(x==0 and y==0):
        print("Point is the origin")
    elif(x!=0 and y==0):
        print("Origin is lies in the x-axis")
    elif(x==0 and y!=0):
        print("Origin lies in the y-axis")
    else:
        if(x>0 and y>0):
            print("Point lies in the first quadrant")
        elif(x<0 and y>0):
            print("Point lies in the second quadrant")
        elif(x<0 and y<0):
            print("Point lies in the third quadrant")
        else:
            print("point lies in the fourth quadrant")