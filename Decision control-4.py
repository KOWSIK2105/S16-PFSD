if __name__ == '__main__':
    marstat=input("Enter the Marital status : ")
    ag=int(input("Enter the age of driver : "))
    sex=input("Enter the gender : ")
    if(marstat=='m' or marstat=='un'& ag>30 & sex=='male'or marstat=='un' and sex=="female" and ag>25):
        print('the company insures the driver and he is passed any condition on above')
    else:
        print("the company doesnt insure ")