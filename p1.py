num=int(input("Enter a number:"))
a=0
b=1
c=a+b
print("Fibonacci sequence:")
for i in range (0,num):
  if a%2==0:
   print(a,end=" ")
  a=b
  b=c
  c=a+b


    