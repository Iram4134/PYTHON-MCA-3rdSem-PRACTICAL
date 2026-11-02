n=int(input("Enter a number:"))
sum=0
num=n
while (n>0):
   digit=n%10
   sum=digit**3+sum
   n=n//10
if (num==sum):  
   print(num, "is an Armstrong number")
else:
   print(num, "is not an Armstrong number")