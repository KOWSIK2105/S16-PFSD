if __name__ == '__main__':
    n=int(input("Enter the value of quantity :"))
    price=float(input("Enter the price of Item :"))
    if(n>1000):
        discount=10
    else:
        discount=0
    bill=n*price-n*price*discount/100
    print("The total bill is : "+str(bill))
