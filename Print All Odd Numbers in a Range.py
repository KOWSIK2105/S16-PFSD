#print odd numbers
#in range

ll=int(input("Enter lower limit "))
ul=int(input("Enter upper limit "))

print("odd numbers in the range are")

# loop

for i in range(ll,ul):
    if i%2!=0:
        print(i,end=" ")