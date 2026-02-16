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

n=int(input())
count=len(str(n))
sum=0
for digit in str(n):
    sum+=int(digit)**count
print("Armstrong number" if sum==n else "Not an armstrong number")