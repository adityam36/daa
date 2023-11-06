sum = 1
def fibo(n):
   if n<=1:
      return n
   else:
      return(fibo(n-1)+fibo(n-2))
input = int(input("Enter the number of items needed:"))
for i in range (input):
   print(i)
a=0
b=1
n=int(input("ENter the number of element you want :"))
sum=1
print(a,b,end=" " )
while (n-2):
   c=a+b
   a=b
   b=c
   sum+=c
   print(c,end=" ")
   n=n-1
print("\n","SUM is :",sum)


# o/p
'''
Enter the number of items needed:5
0
1
2
3
4
Traceback (most recent call last):
'''