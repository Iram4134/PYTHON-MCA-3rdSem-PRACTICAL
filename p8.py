
t = (10, "Python", 3.14, True, 10, "Python")
print("Elements and their data types:")
for i in t:
    print(i, "->", type(i))

print("\nElement at index 0:", t[0])
print("Element at index 2:", t[2])

print("Elements from index 1 to 3:", t[1:4])

print("\nLength of tuple:", len(t))

element = 10
print("Frequency of", element, ":", t.count(element))

element = "Python"
print("Index of", element, ":", t.index(element))