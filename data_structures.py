from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
'Eric'
queue.popleft()                 # The second to arrive now leaves
'John'
#print(queue)                    # Remaining queue in order of arrival

squares = []
for x in range(10):
    squares.append(x**2)

# print(squares)
# print(x)
del x

squares = [x**2 for x in range(10)]
# print(squares)
# print(x)

combs1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
combs2 = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs2.append((x,y))

# print(combs1)
# print(combs2)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

r=[[row[i] for row in matrix] for i in range(4)]
#print(r)

# print("Matrix".rjust(18), matrix)
# print("List Matrix".rjust(18), list(matrix))
# print("* Matrix".rjust(18), *matrix)
# print("List Zip Matrix".rjust(18), list(zip(matrix)))
# print("List Zip * Matrix".rjust(18), list(zip(*matrix)))
# print("Zip * Matrix".rjust(18), zip(*matrix))

matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12, 13],    #make last row longer
]
#print(list(zip(*matrix2)))

matrix3 = [
    [1, 2, 3, 4, 13],    #make first row longer
    [5, 6, 7, 8,],
    [9, 10, 11, 12],
]
#print(list(zip(*matrix3)))

matrix3 = [
    [1, 2, 3, 4, 13],   #make first row longer
    [5, 6, 7, 8, 14],   #make first two rows longer
    [9, 10, 11, 12],
]
#print(list(zip(*matrix3)))

matrix3 = [
    [1, 2, 3, 4, 13],    #make first row longer
    [5, 6, 7, 8, 14],    #make first two rows longer
    [9, 10, 11, 12, 15], #Make all three rows longer
]
#print(list(zip(*matrix3)))

# A set is an unordered collection with no duplicate elements.
s = {x for x in 'abracadabra' if x not in 'abc'}
#print(s)

# Dictionaries are associative arrays, like perl hashes,
#  except dictionaries remember insertion order

# Three idendtical methods for creating the same dictionary
d = {'sape': 4139, 'guido': 4127, 'jack':4098}
#print(d)
d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
#print(d)
d = dict(sape=4139, guido=4127, jack=4098)
#print(d)
d2 = {x: x**2 for x in (2, 4, 6)}    # dict comprehension
#print(d2)

for n, p in d.items():
    print(n, "is at", p)
