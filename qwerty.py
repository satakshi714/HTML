n=int(input("Enter a number: "))
print("The prime palindrome number is....")
for num in range(0,100000):
    c=0
    rev=0
    tmp=num
    #checking for prime number
    for i in range (1,tmp+1):
        if tmp%i==0:
            c+=1

    #if the number is primt check for palindrime number
    if c==2:
        #reversing the number
        while tmp>0:
            rev=rev*10+(tmp%10)
            tmp//=10
        #checking for prime palindrome number
        if rev==num:
            print(num,end=" ")
                
