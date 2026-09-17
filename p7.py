list1 = [1, 2, 3, 4, 2]
list2 = [3, 5, 6, 2, 1]
merged_list=list1 + list2
print("The merged list is:", merged_list)
merged_list.sort()
print("The sorted merged list is:", merged_list)
count=0
for i in merged_list:
     print("The count of", i, "in the merged list is:", merged_list.count(i)) 

#without duplicate values
print("\nThe count of each unique element in the merged list is:")
counted = []

for i in merged_list:
    if i not in counted:
        print(i, "occurs", merged_list.count(i), "times")
        counted.append(i)