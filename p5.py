s=input("Enter a string:")
print("The string is:", s)
punctuation_marks="''!()-[]{};:'/,<>./?@#$%^&*_~ "
result= ""
for ch in s:
  if ch not in punctuation_marks:
    result=result+ch
print("The string without punctuation is:", result)
