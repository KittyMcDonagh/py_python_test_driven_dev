def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("") == 0,"Empty string"        
assert count_upper_case("A") == 1, "One uppercase"
assert count_upper_case("a") == 0, "One uppercase"
assert count_upper_case("Hello World") == 2, "Two uppercase"
assert count_upper_case("HELLO WORLD") == 10, "10 uppercase"

print("All tests passed")

