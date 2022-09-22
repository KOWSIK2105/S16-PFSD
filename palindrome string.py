if __name__ == '__main__':
    string=input("Enter the word : ")
    if(string==string[::-1]):
        print('the word is palindrome = ',str(string))
    else:
        print('the word is not palindrome')