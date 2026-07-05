for i in range(1,6):
    print(i)

l=[1,2,4,5,3,7,4,7]
for j in l:
    print(j)

s="vishesh"
for k in s:
    print(k)   


n= int(input("enter the no "))
for i in range(1,n+1):
    print(" "* (n-i),end="")
    print("*"* (2*i-1),end="")
    print("\n")
