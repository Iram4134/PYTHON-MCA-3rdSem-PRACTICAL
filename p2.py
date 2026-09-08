n=int (input("Enter a number:"))
i=2
print("prime factors are:")
while n>1:
  if n%i==0:
   print(i,end=" ")
   n=n//i
  else:
   i=i+1