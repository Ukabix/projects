"""You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

    Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

test.expect(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), 'should return True');
test.expect(not is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), 'should return False');
test.expect(not is_valid_walk(['w']), 'should return False');
test.expect(not is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False');
"""

walk=(['n','s','n','s','n','s','n','s','n','s'])

def is_valid_walk(walk):
    sum_n = 0
    sum_s = 0
    sum_w = 0
    sum_e = 0
    for step in walk:
        if step == 'n':
            sum_n = sum_n +1
        elif step == 's':
            sum_s = sum_s +1
        elif step == 'w':
            sum_w = sum_w +1
        elif step == 'e':
            sum_e = sum_e +1
        
    if (sum_n>5 or sum_s>5 or sum_w>5 or sum_e>5) or not(sum_n + sum_s + sum_w + sum_e == 10):
        return False
    else:
        if sum_n == sum_s and sum_w == sum_e:
            return True
        else:
            return False

print(is_valid_walk(walk))
