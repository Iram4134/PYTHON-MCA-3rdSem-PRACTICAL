
list1 = [1, 2, 3, 2, 4, 1, 5, 3]

# Convert list into set to remove duplicates
set1 = set(list1)

print("Original list:", list1)
print("Set after removing duplicates:", set1)


set1.add(6)
print("Set after adding 6:", set1)


set1.remove(3)
print("Set after removing 3:", set1)

# Creating another set
set2 = {3, 4, 5, 6, 7, 8}

print("Second set:", set2)

# 3. Union
print("Union:", set1.union(set2))

# Intersection
print("Intersection:", set1.intersection(set2))

# Difference
print("Difference (set1 - set2):", set1.difference(set2))