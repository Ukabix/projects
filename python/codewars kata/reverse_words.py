"""Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
Examples

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"

test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
        test.assert_equals(reverse_words('apple'), 'elppa')
        test.assert_equals(reverse_words('a b c d'), 'a b c d')
        test.assert_equals(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')
"""


def reverse_words(text):
    newlist = []
    if text.count(" ") > 0:
        text = text.split(" ")
        for word in text:
            newlist.append(word[::-1])
        return ' '.join(newlist)
    elif text.count("  ") > 0:
        text = text.split("  ")
        for word in text:
            newlist.append(word[::-1])
        return '  '.join(newlist)
    else: # text.count(" ") and text.count("  ") == 0:
        return text[::-1]

print(reverse_words('double  spaces'))