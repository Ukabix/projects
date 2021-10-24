"""Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:

add_binary(1, 1) == "10" (1 + 1 = 2 in decimal or 10 in binary)
add_binary(5, 9) == "1110" (5 + 9 = 14 in decimal or 1110 in binary)

def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(add_binary(1,1),"10")
        test.assert_equals(add_binary(0,1),"1")
        test.assert_equals(add_binary(1,0),"1")
        test.assert_equals(add_binary(2,2),"100")
        test.assert_equals(add_binary(51,12),"111111")
"""

def add_binary(a,b):
    result = bin(a+b)
    return result[2:]