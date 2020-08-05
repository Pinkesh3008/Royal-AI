
#tuple
'''
=>()
=> ordered
=> unchangable
=> allow duplicate
=>removing individual item is not possible(as immutability) but we can delete entire tuple
=>accessed by index 

'''

#operators

tup1=(1,2,3,4,5,1,4,11)
tup2=(6,7,8,9,10)
print("concatination : =>",tup1+tup2)
print("repeatation := >",tup1*2)


print("slice operator : ",tup1[0:6:2])
print("slice operator : ",tup1[0:6:3])

print("in operator : =>" , 5 in tup1)
print("not in operator : =>" , 5 not in tup1)

#function
print(len(tup1))
print(max(tup1))
print(min(tup1))
print("count :=>",tup1.count(1))
print("count :=>",tup1.count(0))

