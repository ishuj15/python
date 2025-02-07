import gc
import  sys
list=[1,2,3]

print(id(list))
print(gc.get_threshold())
 
print(gc.get_count())
print(list)