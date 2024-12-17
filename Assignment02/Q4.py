#4).Write a function find_longest_word() that takes a list of words and returns the 
# length of the longest one.

def find_longest_word(l1):
    max = 0
    for i in range(len(l1)):
        if len(l1[i]) > max:
            max = len(l1[i])
    return max

l1 = []
n = int(input(f"Enter the size of list: "))
i = 0
while(i < n):
    data = input(f"Enter the word at list index {i}: ")
    l1.append(data)
    i = i + 1
print(f"Longest word: {find_longest_word(l1)}")