#python script to check string is palindrome or not
def strpalindrome(a):
    b=a[::-1]
    if(a==b):
        print(f"{a} is palindrome word !")
    else:
        print(f"{a} is not palindrome word")
a=input("Enter any string :")
strpalindrome(a)
