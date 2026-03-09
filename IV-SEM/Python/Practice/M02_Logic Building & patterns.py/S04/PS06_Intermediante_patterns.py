
'''
li=[1,2,3,4,5]
#output=[2,4,6,8,10]
res=[]
for i in li:
    res.append(i*2)
print(res)
print([i*2 for i in li])
li=[1,2,3,4,5]
#output=[2,4]
res=[]
for i in li:
    if i%2==0:
        res.append(i*2)
print(res)
print([i*2 for i in li if i%2==0])

li=['a','b','c']
res=" "
for i in li:
    res+=i 
print(res)
print(" ".join(li))
'''

'''Intermediate Patterns
1.Pyramid
n=4
output:
    *
   * *
  * * *
 * * * *

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
'''
'''
2.Inverted Pyramid
n=4
output:
* * * *
 * * * 
  * * 
   *

n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
    
3.diamond
n=4
output:
   *
  * *
 * * *  
* * * *
 * * *
  * *
   *

n=int(input())
for i in range(1,n+1):  
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i) 


#number pyramid
n=4
output:
   1
  1 2
 1 2 3
1 2 3 4

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+" ".join(str(j) for j in range(1,i+1))) 


#Alphabet Pyramid
n=4
output:
A
B C 
D E F 
G H I J 
'''

n=int(input())
count=0
for i in range(1,n+1):
    row=""
    for j in range(i):
        row+=chr(65+count)+" "
        count+=1
    print(row)
    
