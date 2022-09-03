if __name__ == "__main__":
    n1=int(input('Enter the starting range : '))
    n2=int(input('Enter the ending range : '))
    for i in range(n1,n2):
        if(i%2!=0 and i%3!=0):
            print(i)
