# Ambreen Chaudhri
# HW 4 Sorting Algorithms

######################################
# First Selection Algorithm: QUICKSORT
######################################

# EXPLANATION:
# Quicksort randomly picks a pivot point.  Then goes through a series of comparisons to place
# pivot in its sorted spot.  At that point it divides the list into two sublists: the points
# to the left of the pivot (lower) and the points greater than the pivot (upper).  It then 
# starts with a new pivot in one of the sublists and places this point in its appropriate place
# then repeats this procedure until the list is sorted (This is the recursive step to this
# sorting method.  

# I used this to help write the function: http://www.geekviewpoint.com/python/sorting/quicksort
# Note that the 'pivot' is randomly selected.  For simplicity I use the first element of the
# list I give the function to be my input. 

import random

def quicksort(inputlist): # complexity = O(n^2) at worst; O(n log n) at best
    try:
        if inputlist == []:
            return []
        else:
            pivot = inputlist[0]
            lower = quicksort([i for i in inputlist[1:] if i < pivot]) 
            			# this moves all values less than the pivot to its left
            upper = quicksort([i for i in inputlist[1:] if i >= pivot])
            			# this moves all values greater than the pivot to its right.	
            return lower + [pivot] + upper
            			# since quicksort will sort each number in the list to its appropriate 
            			# position using upper and lower, this will return a fully sorted list. 
    except:
        if type(inputlist) != list:
            return "Please provide a list of elements as your input.  For instance [1,2,3,4]."


######################################
# Second Selection Algorithm: BUBBLESORT
######################################

# EXPLANATION:
# Bubblesort compares the first two elements of an array and sorts them if they are out of 
# order.  It then moves on to the 2nd and 3rd elements in the array and sorts them.  Once
# it reaches the final two elements and sorts them, the largest number will be sorted to the 
# end of the array.  Bubblesort will then restart the sorting procedure on the first two 
# elements of the array and repeat this procedure (the recursive step) until the array is 
# fully sorted.  For instance if there are 5 numbers, bubble sort will repeat the sorting
# procedure 4 times, each subsequent time leaving out the comparison between the final 
# two elements.  

# I used this to help write the function: http://www.geekviewpoint.com/python/sorting/bubblesort
# While the function uses recursion, I couldn't figure out a way to reference 'bubblesort' within
# the function itself. 


# O(n^2) with O(n) when nearly sorted
# I used this to help write the function: http://www.geekviewpoint.com/python/sorting/bubblesort
def bubblesort(inputlist):
    try:
        n = len(inputlist)
        for j in range(n,1,-1):  # this reverse orders the range and drops the last number
																 # So a list with three numbers [2,1,3] would give us 
																 # [3, 2].  This means that for each iteration of sorting
																 # it will compare one less number at the end of the list
																 # since that number was already sorted to its appropriate
																 # place in the first iteration of sorting. 
											 
            for i in range(n-1): # For a list of [2,1,3] this provides a range of [0,1]
                                 # So the first two elements (list[0] and list[1]) will 
                                 # be sorted first, then the second two elements (list [1]
                                 # and list [2]) will be sorted.  
                if inputlist[i] >= inputlist[i+1]:  # this step compares whether the second
                                                    # value is larger than the first
                    inputlist[i],inputlist[i+1] = inputlist[i+1],inputlist[i] # this step sorts the list.
        return inputlist
    except:
        if type(inputlist) != list:
            return "Please provide a list of elements as your input.  For instance [1,2,3,4]."

############################
# These are just some tests.
############################

correct_order = [1,2,3,4,5,6,7,8,9,10]
reverse_order = [10,9,8,7,6,5,4,3,2,1]
not_list = 210
not_sorted = [7,4,5,9,2,3,6,8,10,1]
random_list = random.sample(range(1,11),10)

quicksort(correct_order)
quicksort(reverse_order)
quicksort(not_list)
quicksort(not_sorted)
quicksort(random_list)


bubblesort(correct_order)
bubblesort(reverse_order)
bubblesort(not_list)
bubblesort(not_sorted)
bubblesort(random_list)




