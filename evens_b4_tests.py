# The purpose of this function is to accept a list of numbers and return True if the list has an even number of even numbers
# Unanswered questions - What should it return if there aren't an even number of even numbers? Or if there are no even numbers?
# The principle of Test-Driven Development is to develop incrementally, writing only enough code to pass each test in order 
# without breaking the preceding test.



# First do the first test, which is expecting the function to return False. The easiest way to make the test pass is to return False

def even_number_of_evens(numbers):
     count = sum([1 for n in numbers if n % 2 == 0])
     if count > 0:
        return count % 2 == 0
     else:
        return False

assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, 3 even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, 4 even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"
assert even_number_of_evens([2, 4, 10]) == False, "3 even"
assert even_number_of_evens([2, 4, 10, 6]) == True, "4 even"

print("all tests passed")