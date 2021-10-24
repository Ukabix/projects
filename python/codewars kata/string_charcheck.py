"""Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

test.expect(xo('xo'), 'True expected')
test.expect(xo('xo0'), 'True expected')
test.expect(not xo('xxxoo'), 'False expected')
"""



def xo(s):
    ns = s.lower()
    if ns.count("x") == ns.count("o"):
        return True
    else:
        return False



