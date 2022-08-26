# You'll need to use a couple of built in functions to alphabetize a string.
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

strg = "hello world"


print("The original string : " + str(strg))


res = ''.join(sorted(strg))


print("String after sorting : " + str(res))
