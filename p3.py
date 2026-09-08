s=input("Enter a string:")
print("The string is:", s)

#reverse the string
r= s[::-1]
#[start:end:step]
print("The reversed string is:", r)

#palindrome check
if s.lower()==r.lower():
  print("The string is a palindrome")
else:
  print("The string is not a palindrome")

#count the length of the string
print("The length of the string is:", len(s))
 
#count vowels
c=0
for ch in s:
  if ch.lower() in "aeiou":
    c=c+1
print("The number of vowels in the string is:", c)

