if __name__ == '__main__':
    n=int(input('Enter the year : '))
    if(n%4==0 and n%100!=0 or n%400==0):
        print('the given year is '+str(n)+" leap year")
    else:
        print('The year '+str(n)+' is not leap year')