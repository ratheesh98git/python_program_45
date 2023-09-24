#42) Python program to illustrate different set operations




set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}


union_result = set1.union(set2)
print("Union of set1 and set2:", union_result)

intersection_result = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_result)

difference_result = set1.difference(set2)
print("Difference of set1 - set2:", difference_result)

symmetric_difference_result = set1.symmetric_difference(set2)
print("Symmetric Difference of set1 and set2:", symmetric_difference_result)

is_subset = set1.issubset(set2)
print("Is set1 a subset of set2?", is_subset)

is_superset = set1.issuperset(set2)
print("Is set1 a superset of set2?", is_superset)

set1.add(6)
print("After adding 6 to set1:", set1)

set2.remove(7)
print("After removing 7 from set2:", set2)
