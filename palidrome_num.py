n=int(input("enter num"))
i=n
count=0
while i>0:
    count=count+1
    i//=10
i=n
sum=0
digit=0
while i>0:
    digit=digit+i%10
    pro=1
    x=1
    while x<=count:
        pro=pro*digit
        x+=1
    sum=sum+pro
    i//=10
if sum==n:
    print("num is palidrome")
else:
    print("not palidrome")            

        
        