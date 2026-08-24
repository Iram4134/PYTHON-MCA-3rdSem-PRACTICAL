num=int(input("Enter a number:"))
a=0
b=1
c=a+b
print("Fibonacci sequence:")
print(a,b,end=" ")
for i in range (0,num):
  print(c,end=" ")
  a=b
  b=c
  c=a+b

    