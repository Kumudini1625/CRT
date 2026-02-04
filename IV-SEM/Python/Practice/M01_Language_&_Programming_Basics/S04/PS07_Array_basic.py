'''import array
arr=array.array('i',[])
print(arr,type(arr))
arr.append(10)
arr.append(20)
print(arr)
arr.insert(1,15)
print(arr)
'''

'''
li=[12,25.4,6+5j,"Hello",12,25.4]
print(li,type(li))
print(li[3])
print(li[3:6:1])
print(li[::-1])
print(len(li))
li.append(100)
print(li)
li.insert(2,"World")
print(li)
'''

'''
#read a number from user and display no.of digits in that number
input:1234
output:4
num=int(input("Enter a number:"))
count=0
while num>0:
    num=num//10
    count=count+1
print("No.of digits:",count)
'''

import numpy as np
arr=np.array([10,20,30,40,50]) 
print("Array elements are:",arr)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.sum(arr))
print(np.zeros(5))
print(np.ones(8))
print("Even numbers are:",np.arange(2,10,2))
print("Odd numbers are:",np.arange(1,10,2))

n=int(input("Enter the size of array:"))
ele=list(map(int,input("Enter the elements:").split()))
print("Array elements are:",np.array(ele))