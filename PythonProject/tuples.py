# Immutable
# you can add mutable objects in tuple but can't do it in sets and dictionary
# You can't modify element inplace
customTuple=(1,2,[1,2])
print(customTuple)
print(customTuple[1])

# if you want to create single tuple
tu=(1,)
print(type(tu))
# if you didn't use , then python will consider it as int and not tuples
tup=(1)
print(type(tup))

# You can do slicing in tuple

# Methods in tuple
# 1) tu.index(elemet)  to find indes and 2) tu.count(element)