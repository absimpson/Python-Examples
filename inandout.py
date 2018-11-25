year = 2016
event = 'Referendum'
#print(f'Results of the {year} {event}')

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
t='{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
#print(t)

# s = 'Hello, world.'
# print(str(s))
# print(repr(s))
# print(str(1/7))
# x = 10 * 3.25
# y = 200 * 200
# s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
# print(s)
# # The repr() of a string adds string quotes and backslashes:
# hello = 'hello, world\n'
# hellos = repr(hello)
# print(hellos)
# #print( The argument to repr() may be any Python object:)
# print(repr((x, y, ('spam', 'eggs'))))

import math
#print(f'The value of pi is approximately {math.pi:.3f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
#    print(f'{name:10} ==> {phone:10d}')
    pass

animals = 'eels'
# print(f'My hovercraft is full of {animals}.')
# print(f'My hovercraft is full of {animals!a}.')
# print(f'My hovercraft is full of {animals!s}.')
# print(f'My hovercraft is full of {animals!r}.')

for x in range(1, 11):
#    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    pass
