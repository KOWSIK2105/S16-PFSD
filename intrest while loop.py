if __name__ == '__main__':
    i=1
    while i<=3:
        p=int(input(' Enter the value of principle amount : '))
        t=int(input(' Enter the value of time : '))
        r=float(input(' Enter the value of rate of interest : '))
        intrest=p*t*r/100
    print(" The total simple interest is : "+str(intrest))
    i=i+1
