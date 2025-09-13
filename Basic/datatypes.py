""" 
datatypes are
1.mutable
2.unmutable

mutable
 1. list->[1,2,3,4]
 2.tuple 
 set
 frozenset
 

 nums[last]=nums[-1] in indexing
 indexing 0 se start hota hai from left to right but,
 piche se -1 se start hota hai
 """

names=['hey','hello','krishn','madhav','balram']
for name in names:
    #print(name[1])

    list1=[1,2,3,4,5,6,7,8]
print(list1[::-1])
print(list1[-2:-6:-1])
list1.reverse()
print(list1)