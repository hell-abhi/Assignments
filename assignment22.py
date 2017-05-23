from functools import reduce
input = [[1, 2, 3], [4, 5], [6, 7, 8]]
output = reduce(lambda x,y: x+y, input)
print(output)
