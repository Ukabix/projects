# Given: an array containing hashes of names

# Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

# Example:

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart & Lisa'

# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'

# namelist([])
# # returns ''

# Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

# test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge',
# "Must work with many names")
# test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie',
# "Must work with many names")
# test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'}]), 'Bart & Lisa', 
# "Must work with two names")
# test.assert_equals(namelist([{'name': 'Bart'}]), 'Bart', "Wrong output for a single name")
# test.assert_equals(namelist([]), '', "Must work with no names")

def namelist(names):
    mylist = []
    for dictname in names:
        mylist.append(dictname['name'])
    if len(mylist) == 0:
        return f""
    if len(mylist) == 1:
        return f"{mylist[0]}"
    elif len(mylist) == 2:
        return f"{mylist[0]} & {mylist[1]}"
    else:
        names = ""
        for name in mylist[0:-2]:
            names += f"{name}, "
        return f"{names}{mylist[-2]} & {mylist[-1]}"

print(namelist([]))