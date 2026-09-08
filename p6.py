my_list=['iram',21,0.5,True]
for item in my_list:
  print(item," ", type(item))

print("The length of the list is:", len(my_list))

print ("The first item in the list is:", my_list[0])

print ("The last item in the list is:", my_list[-1])

print("The list in reverse order is:", my_list[::-1])

print("The list from index 1 to 3 is:", my_list[1:4])

my_list.append("python")
print("The list after appending an item is:", my_list)

my_list.remove(True)
print("The list after removing an item is:", my_list)

my_list.insert(2,"Great")
print("The list after inserting an item is:", my_list)

my_list.sort(key=str)
print("The list after sorting is:", my_list)

my_list.reverse()
print("The list after reversing is:", my_list)
