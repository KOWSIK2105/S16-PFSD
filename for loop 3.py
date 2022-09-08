string='Nagpur-440010'
alphabet=special=digits=0
for i in range(len(string)):
    if(string[i].isalpha()):
        alphabet=alphabet+1
    if(string[i].isdigit()):
        digits=digits+1
    else:
        special=special+1
    print("No of alphabets :",alphabet)
    print("No of digits : ",digits)
    print("No of special characters : ",special)
