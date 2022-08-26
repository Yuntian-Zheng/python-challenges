# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
opera = input('What calculation would you like to do? (add, sub, mult, div)')

x = input('what is number 1?')

y = input('what is number 2?')


def cal(x, y):
    x = int(x)
    y = int(y)
    if opera == "add":
        return 'your result is '+str(x+y)
    if opera == "div":
        return 'your result is '+str(x/y)
    if opera == "mult":
        return 'your result is '+str(x*y)
    if opera == "sub":
        return 'your result is '+str(x-y)


print(cal(x, y))
