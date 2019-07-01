"""
Solution to the challenge in the `Test After` unit found in the `Test Driven
Development with Python lesson`
NOTE: The solution found in this file is one of the many potential solutions
that can be used to achieve the end result expected by the challenge in the
lesson.
"""


def count_upper_case(message):
    """
    Count the number of upper case characters in a given message
    `message` is the piece of text to be checked
    
    Returns the number of uppercase characters in a message
    """
    return sum([1 for c in message if c.isupper()])

assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("AA") == 2, "Two upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%%^") == 0, "Special characters"

# Added by me as part of the Challenge

assert count_upper_case("Kitty McDonagh") == 3, "Kitty McDonagh, 5: will fail"
assert count_upper_case("HELLO WORLD") == 10, "HELLO WORLD, 10 uppercase: Pass"
assert count_upper_case("Hello World") == 2, "HELLO WORLD, 10 uppercase: Pass"

# An example of a failed test would be -
# assert count_upper_case("A") == 0, "One upper case"

print("All the tests passed")