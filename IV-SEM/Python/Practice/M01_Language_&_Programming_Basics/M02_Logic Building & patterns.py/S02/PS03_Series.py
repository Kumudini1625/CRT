
'''
#Fibonnaci series
n=int(input())
a=0
b=1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b


#list of program
fib=[0,1]
for i in range(2,n):
    fib.append(fib[i-1]+fib[i-2])
print(fib)
'''

#power of number series
n=int(input())
for i in range(n):
    print(2**i,end=" ")
