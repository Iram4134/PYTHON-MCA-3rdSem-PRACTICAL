n=int(input("Enter a number:"))
for i in range(1,n+1):
  if i%2==0:
    print(i,end=" "+" even")
    print("")
  else:
    print(i,end=" "+" odd")
    print("")