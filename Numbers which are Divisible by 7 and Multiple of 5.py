if __name__ == "__main__":
    n1=int(input('Enter the starting range : '))
    n2=int(input('Enter the ending range : '))
    for i in range(n1,n2+1):
        if(i%7==0 and i%5==0):
            print(i)
