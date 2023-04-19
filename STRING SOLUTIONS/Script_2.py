#script to enter any sentence and print those word which is palindrome and  also print total number of palindrome word in it.
def sentpailndrome(s):
    dic=[]
    count=0
    a=s.split()
    for i in a:
        b=i[::-1]
        if b==i:
            print(b)
            dic.append(b)
            count=count+1
    print(f"There are total {count} palindrome word in entered String :{set(dic)}")
s=input("Enter any Sentence:")
sentpailndrome(s)
