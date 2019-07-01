
# Testing Functions

def test_not_equal(a, b):
    assert a != b, "Did not expect {0}, but got {1}".format(a, b)
    
def test_between(actual, lower_limit, upper_limit):
    assert lower_limit <= actual <= upper_limit, "{0} is less than or equal to {1} or equal to or greater than {2}".format(actual, lower_limit, upper_limit)
    
def test_is_in(item, collection):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_not_in(item, collection):
    assert item not in collection, "{0} contains {1}".format(collection, item)
    

# Run test on test functions

test_not_equal(2, 3)

test_is_in(5, [1, 2, 3, 4, 5])

test_not_in(6, [1, 2, 3, 4, 5])

test_between(6, 4, 9)

print("All tests have passed!")







