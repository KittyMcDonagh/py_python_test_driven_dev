{"filter":false,"title":"byotest.py","tooltip":"/byotest.py","undoManager":{"mark":30,"position":30,"stack":[[{"start":{"row":0,"column":0},"end":{"row":34,"column":0},"action":"remove","lines":["","# Testing Functions","","def test_not_equal(a, b):","    assert a != b, \"Did not expect {0}, but got {1}\".format(a, b)","    ","def test_between(actual, lower_limit, upper_limit):","    assert lower_limit <= actual <= upper_limit, \"{0} is less than or equal to {1} or equal to or greater than {2}\".format(actual, lower_limit, upper_limit)","    ","def test_is_in(item, collection):","    assert item in collection, \"{0} does not contain {1}\".format(collection, item)","    ","def test_not_in(item, collection):","    assert item not in collection, \"{0} contains {1}\".format(collection, item)","    ","","# Run test on test functions","","test_not_equal(2, 3)","","test_is_in(5, [1, 2, 3, 4, 5])","","test_not_in(6, [1, 2, 3, 4, 5])","","test_between(6, 4, 9)","","print(\"All tests have passed!\")","","","","","","","",""],"id":406},{"start":{"row":0,"column":0},"end":{"row":73,"column":24},"action":"insert","lines":["\"\"\"","Solution to the third challenge in the `Build Your Own Test Framework` unit ","found in the `Test Driven Development with Python lesson`","NOTE: The solution found in this file is one of the many potential solutions","that can be used to achieve the end result expected by the challenge in the","lesson.","\"\"\"","","","def test_are_equal(actual, expected):","    \"\"\"","    Test that two values are equal. Raises AssertionError if both values are","    not equal.","    `actual` is the actual value produced","    `expected` is the value that was supposed to be produced","    \"\"\"","    assert expected == actual, \"Expected {0}, got {1}\".format(","        expected, actual)","","","def test_not_equal(a, b):","    \"\"\"","    Test that two values are not equal. Raises AssertionError if both values","    are not equal.","    `a` is the actual value produced","    `b` is the value that was supposed to be produced","    \"\"\"","    assert a != b, \"Did not expect {0} but got {1}\".format(a, b)","","","def test_is_in(collection, item):","    \"\"\"","    Check to ensure that a given collection contains a given value. Raises","    AssertionError if `item` is not in `collection`","    `collection` is the collection to be tested","    `item` is the item that is being searched for","    \"\"\"","    assert item in collection, \"{0} does not contain {1}\".format(","        collection, item)","","","def test_not_in(collection, item):","    \"\"\"","    Check to ensure that a given collection does not contain a given value.","    Raises AssertionError if the `item` is found in `collection`","    `collection` is the collection in question","    `item` is the thing that we want to check for","    \"\"\"","    assert item not in collection, \"{0} is not in {1}\".format(","        item, collection)","","","def test_between(upper_limit, lower_limit, actual):","    \"\"\"","    Check to ensure that a number is between two other numbers. Raises","    AssertionError if the number is not between the other two numbers","    \"\"\"","    assert lower_limit <= actual <= upper_limit, \"{0} is not between {1} and {2}\".format(actual, lower_limit, upper_limit)","","","# Test to fail the `test_are_equal` function","# test_are_equal(number_of_evens([1,2,3,4,5]), 2)","","# Test to fail the `test_not_equal` function","# test_not_equal(0, 0)","","# Test to fail the `test_is_in` function","# test_is_in([1], 2)","","# Test to fail the `test_not_in` function","# test_not_in([1], 1)","","# Test to fail the `test_between` function","test_between(10, 1, 200)"]}],[{"start":{"row":0,"column":3},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":407},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]},{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["C"]}],[{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["o"],"id":408},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["p"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["i"]},{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":["e"]},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["d"]}],[{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":[" "],"id":409},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["t"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["h"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["i"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":[" "],"id":410},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["f"]},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["r"]},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["o"]},{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["m"]}],[{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":[" "],"id":411},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["S"]},{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"insert","lines":["o"]}],[{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"insert","lines":["l"],"id":412},{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"insert","lines":["u"]},{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":["t"]},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":["i"]},{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"insert","lines":["o"]},{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"insert","lines":["n"]}],[{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":[" "],"id":413},{"start":{"row":2,"column":26},"end":{"row":2,"column":27},"action":"insert","lines":["C"]},{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"insert","lines":["o"]},{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["d"]},{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":30},"end":{"row":2,"column":31},"action":"insert","lines":[" "],"id":414}],[{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["C"],"id":415},{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"insert","lines":["I"]}],[{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"insert","lines":[" "],"id":416}],[{"start":{"row":2,"column":34},"end":{"row":2,"column":35},"action":"insert","lines":["b"],"id":417},{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"insert","lines":["e"]},{"start":{"row":2,"column":36},"end":{"row":2,"column":37},"action":"insert","lines":["f"]},{"start":{"row":2,"column":37},"end":{"row":2,"column":38},"action":"insert","lines":["o"]},{"start":{"row":2,"column":38},"end":{"row":2,"column":39},"action":"insert","lines":["r"]},{"start":{"row":2,"column":39},"end":{"row":2,"column":40},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":40},"end":{"row":2,"column":41},"action":"insert","lines":[" "],"id":418},{"start":{"row":2,"column":41},"end":{"row":2,"column":42},"action":"insert","lines":["s"]},{"start":{"row":2,"column":42},"end":{"row":2,"column":43},"action":"insert","lines":["t"]},{"start":{"row":2,"column":43},"end":{"row":2,"column":44},"action":"insert","lines":["a"]},{"start":{"row":2,"column":44},"end":{"row":2,"column":45},"action":"insert","lines":["r"]},{"start":{"row":2,"column":45},"end":{"row":2,"column":46},"action":"insert","lines":["t"]},{"start":{"row":2,"column":46},"end":{"row":2,"column":47},"action":"insert","lines":["i"]},{"start":{"row":2,"column":47},"end":{"row":2,"column":48},"action":"insert","lines":["n"]},{"start":{"row":2,"column":48},"end":{"row":2,"column":49},"action":"insert","lines":["g"]}],[{"start":{"row":2,"column":49},"end":{"row":2,"column":50},"action":"insert","lines":[" "],"id":419},{"start":{"row":2,"column":50},"end":{"row":2,"column":51},"action":"insert","lines":["m"]},{"start":{"row":2,"column":51},"end":{"row":2,"column":52},"action":"insert","lines":["i"]},{"start":{"row":2,"column":52},"end":{"row":2,"column":53},"action":"insert","lines":["n"]},{"start":{"row":2,"column":53},"end":{"row":2,"column":54},"action":"insert","lines":["i"]}],[{"start":{"row":2,"column":54},"end":{"row":2,"column":55},"action":"insert","lines":[" "],"id":420},{"start":{"row":2,"column":55},"end":{"row":2,"column":56},"action":"insert","lines":["p"]},{"start":{"row":2,"column":56},"end":{"row":2,"column":57},"action":"insert","lines":["r"]},{"start":{"row":2,"column":57},"end":{"row":2,"column":58},"action":"insert","lines":["o"]},{"start":{"row":2,"column":58},"end":{"row":2,"column":59},"action":"insert","lines":["j"]},{"start":{"row":2,"column":59},"end":{"row":2,"column":60},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":60},"end":{"row":2,"column":61},"action":"insert","lines":["c"],"id":421},{"start":{"row":2,"column":61},"end":{"row":2,"column":62},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":62},"end":{"row":2,"column":63},"action":"insert","lines":[" "],"id":422},{"start":{"row":2,"column":63},"end":{"row":2,"column":64},"action":"insert","lines":["t"]},{"start":{"row":2,"column":64},"end":{"row":2,"column":65},"action":"insert","lines":["o"]}],[{"start":{"row":2,"column":65},"end":{"row":2,"column":66},"action":"insert","lines":[" "],"id":423},{"start":{"row":2,"column":66},"end":{"row":2,"column":67},"action":"insert","lines":["e"]},{"start":{"row":2,"column":67},"end":{"row":2,"column":68},"action":"insert","lines":["n"]},{"start":{"row":2,"column":68},"end":{"row":2,"column":69},"action":"insert","lines":["s"]},{"start":{"row":2,"column":69},"end":{"row":2,"column":70},"action":"insert","lines":["u"]},{"start":{"row":2,"column":70},"end":{"row":2,"column":71},"action":"insert","lines":["r"]},{"start":{"row":2,"column":71},"end":{"row":2,"column":72},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":72},"end":{"row":2,"column":73},"action":"insert","lines":[" "],"id":424},{"start":{"row":2,"column":73},"end":{"row":2,"column":74},"action":"insert","lines":["I"]}],[{"start":{"row":2,"column":74},"end":{"row":2,"column":75},"action":"insert","lines":[" "],"id":425},{"start":{"row":2,"column":75},"end":{"row":2,"column":76},"action":"insert","lines":["h"]},{"start":{"row":2,"column":76},"end":{"row":2,"column":77},"action":"insert","lines":["a"]}],[{"start":{"row":2,"column":76},"end":{"row":2,"column":77},"action":"remove","lines":["a"],"id":426},{"start":{"row":2,"column":75},"end":{"row":2,"column":76},"action":"remove","lines":["h"]}],[{"start":{"row":2,"column":75},"end":{"row":2,"column":76},"action":"insert","lines":["s"],"id":427},{"start":{"row":2,"column":76},"end":{"row":2,"column":77},"action":"insert","lines":["t"]},{"start":{"row":2,"column":77},"end":{"row":2,"column":78},"action":"insert","lines":["a"]},{"start":{"row":2,"column":78},"end":{"row":2,"column":79},"action":"insert","lines":["t"]},{"start":{"row":2,"column":79},"end":{"row":2,"column":80},"action":"insert","lines":["e"]},{"start":{"row":2,"column":80},"end":{"row":2,"column":81},"action":"insert","lines":["d"]}],[{"start":{"row":2,"column":81},"end":{"row":2,"column":82},"action":"insert","lines":[" "],"id":428}],[{"start":{"row":2,"column":81},"end":{"row":2,"column":82},"action":"remove","lines":[" "],"id":429},{"start":{"row":2,"column":80},"end":{"row":2,"column":81},"action":"remove","lines":["d"]},{"start":{"row":2,"column":79},"end":{"row":2,"column":80},"action":"remove","lines":["e"]},{"start":{"row":2,"column":78},"end":{"row":2,"column":79},"action":"remove","lines":["t"]},{"start":{"row":2,"column":77},"end":{"row":2,"column":78},"action":"remove","lines":["a"]}],[{"start":{"row":2,"column":77},"end":{"row":2,"column":78},"action":"insert","lines":["a"],"id":430},{"start":{"row":2,"column":78},"end":{"row":2,"column":79},"action":"insert","lines":["r"]},{"start":{"row":2,"column":79},"end":{"row":2,"column":80},"action":"insert","lines":["t"]},{"start":{"row":2,"column":80},"end":{"row":2,"column":81},"action":"insert","lines":["e"]},{"start":{"row":2,"column":81},"end":{"row":2,"column":82},"action":"insert","lines":["d"]}],[{"start":{"row":2,"column":82},"end":{"row":2,"column":83},"action":"insert","lines":[" "],"id":431},{"start":{"row":2,"column":83},"end":{"row":2,"column":84},"action":"insert","lines":["w"]},{"start":{"row":2,"column":84},"end":{"row":2,"column":85},"action":"insert","lines":["i"]},{"start":{"row":2,"column":85},"end":{"row":2,"column":86},"action":"insert","lines":["t"]},{"start":{"row":2,"column":86},"end":{"row":2,"column":87},"action":"insert","lines":["h"]}],[{"start":{"row":2,"column":87},"end":{"row":2,"column":88},"action":"insert","lines":[" "],"id":432},{"start":{"row":2,"column":88},"end":{"row":2,"column":89},"action":"insert","lines":["n"]},{"start":{"row":2,"column":89},"end":{"row":2,"column":90},"action":"insert","lines":["o"]}],[{"start":{"row":2,"column":90},"end":{"row":2,"column":91},"action":"insert","lines":[" "],"id":433},{"start":{"row":2,"column":91},"end":{"row":2,"column":92},"action":"insert","lines":["b"]},{"start":{"row":2,"column":92},"end":{"row":2,"column":93},"action":"insert","lines":["u"]},{"start":{"row":2,"column":93},"end":{"row":2,"column":94},"action":"insert","lines":["g"]},{"start":{"row":2,"column":94},"end":{"row":2,"column":95},"action":"insert","lines":["s"]}],[{"start":{"row":2,"column":95},"end":{"row":2,"column":96},"action":"insert","lines":["."],"id":434}],[{"start":{"row":2,"column":96},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":435}],[{"start":{"row":0,"column":3},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":436}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":3},"end":{"row":0,"column":3},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1562049338596,"hash":"9a17124ece2355c91da3c9f9a8910594ce172600"}