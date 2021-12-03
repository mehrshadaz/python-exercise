b=int(input("enter number:"))
a=int(input("enter another number:"))
max=1
for i in range(max,a*b+1):
    if i%a==0 and i%b==0:
        print(i)
        break