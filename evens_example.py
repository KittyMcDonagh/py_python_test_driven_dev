"""
This is an example of writing the tests before writing the function. 
Think about what you want it to do first, and test for that.
"""

assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, 3 even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, 4 even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("all tests passed")