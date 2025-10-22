list1 = [1,2,3]
list2=list1

# list1 and list2 point to the same object in memory  

list2=[4,5,6]
# Now list2 points to a new object in memory
print("list1:", list1)  # Output: [1, 2, 3]
print("list2:", list2)  # Output: [4, 5, 6]

list1=[7,8,9]   
list2=list1[:]  # Create a shallow copy of list1

# list1 and list2 point to different objects in memory,because of slicing a new copy has been created.