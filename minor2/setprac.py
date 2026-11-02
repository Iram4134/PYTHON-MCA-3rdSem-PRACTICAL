set1={1,2,3,4,5}
set2={3,4,5,6,7}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print(set1.difference(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))
print(set1)
print(set2)
print(set1.pop())
print(set1)
print(set1.clear())
print(set1)
print(set2)
print(set2.pop())
print(set2)
print(set2.clear())
print(set2)
print(set1.add(10))
print(set1)
print(set1.update([200,300,400]))
print(set1)


set3={10,10,20,20,30,40,50}
print(set3)

#not working set4={10,20,{30,40,50},60}
# print(set4)

forzen_set={10,20,30,10,50}
print(forzen_set)
print(forzen_set.add(60))
print(forzen_set.remove(20))