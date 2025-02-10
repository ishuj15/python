nums ={1,2,1,"hello"}
print(nums)
print(len(nums))

# How to create empty set
emptySet=set()
# as set={} will create emmpty dictionary

# sets are mutable but i can't modify the elements that is why i can't pass list or mutable objects in the set

emptySet.add(1)
emptySet.add(2)
# emptySet.remove(5)  will give error as value doesn't exist
# emptySet.add([1,2]) will give error because the hashvalue can be changed for this

emptySet.add((1,2))
emptySet.add((1,2))  #no error but no duplicates
# emptySet.add({"n":"ishu"})  can't mutable object

print(nums.difference(emptySet))
print(nums.union(emptySet))
print(nums.intersection(emptySet))