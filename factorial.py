#  factorial using recurtion functions
def recurfact(n):
    if n==1:
        return n
    else:
        return n*recurfact(n-1)

n = int(input("num: "))
if (n<0):
    print("factorial not exist for negative no.")
elif(n==0):
    print("factorial : 1")
else:
    print("factorial:",recurfact(n))