# The goal of this exercise is to convert a string to a new string where each character in the new string
#  is "(" if that character appears only once in the original string, or ")" if that character appears more than once
#  in the original string. Ignore capitalization when determining if a character is a duplicate.
# Examples

# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("

# Notes

# Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!



def function(mystring):
    mystring = mystring.lower()
    coded_mystring = ""
    def replace_letter(letter, mystring):
        if mystring.count(letter) > 1:
            return ")"
        else:
            return "("
    for letter in mystring:
        coded_mystring += replace_letter(letter, mystring)
    return coded_mystring


print(function("din"))
print(function("recede"))
print(function("Success"))
print(function("(( @"))