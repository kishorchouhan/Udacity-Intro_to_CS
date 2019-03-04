# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(list):
    if len(list) == 0:
        return None
    else:
        max = 0
        repeat = 0
        value = 0
        prev = list[0]
        for e in list:
            if e == prev:
                repeat += 1
                prev = e
            else:
                repeat = 1
                prev = e
            if repeat > max:
                max = repeat
                value = e 
        return value

#For example,
print (longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
# 3

print (longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
# b

print (longest_repetition([1,2,3,4,5]))
# 1

print (longest_repetition([]))
# None
