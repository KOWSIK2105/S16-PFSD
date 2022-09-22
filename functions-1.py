if __name__ == '__main__':
    def cal_sum_prod(x,y,z):
        s=x+y+z
        p=x*y*z
        return s,p
    a=int(input("Enter a :"))
    b=int(input("Enter b :"))
    c=int(input("Enter c :"))
    s,p=cal_sum_prod(a,b,c)
    print(s,p)