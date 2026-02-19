
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
'''
n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
       