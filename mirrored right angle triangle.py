a=int(input("enter the number of rows: "))
for i in range(a):
    for j in range(a-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()