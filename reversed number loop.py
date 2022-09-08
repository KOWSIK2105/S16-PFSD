if __name__ == '__main__':
    n=int(input("Enter the number to reverse : "))
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    print('reversed number : ',rev)