'''
Armstrong Number: A number is called an Armstrong number if it is equal to the sum of its own digits raised to the power of the number of digits. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
'''
'''
Armstrong number:
input: 153
output: 153 is an armstrong number
 input:24
 output: 24 is not an armstrong number
 '''
'''
n=int(input())
count=len(str(n))
sum=0
for digit in str(n):
    sum+=int(digit)**count
print("Armstrong number" if sum==n else "Not an armstrong number")
'''

'''perfect number:'''
'''
n=int(input())
sum=0
for i in range(1,n//2+1):
    if n%i==0:
        sum+=i
print("Perfect number" if sum==n else "Not a perfect number")
'''


'''Strong number:
input:123
ouput:not a strong number
Explanation : 1! + 2! + 3! = 1 + 2  +  6 =9'''
'''
def factorial(num):
    if num<0:
        return "no factorial for -ve"
    elif num==0 or num==1:
        return 1
    else:
        fact=1
        for i in range(2,num+1):
            fact=fact*i
        return fact
n=int(input())
sum=0   
for digit in str(n):
    sum+=factorial(int(digit))  
print("Strong number" if sum==n else "Not a strong number")
'''