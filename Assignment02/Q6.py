'''6). Concatenate two lists in the following order by using list comprehension
Input:- list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Output:- [’Hello Dear’, ’Hello Sir’, ’take Dear’, ’take Sir’]
'''

l1 = ["Hello ", "take "]
l2 = ["Dear", "Sir"]
l3 = [f"{i}{j}" for i in l1 for j in l2]
print(l3)