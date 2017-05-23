input = [1, 'a', ['d', 'e', 'f'], 2, -1, (1, 2, 3), 'g']
output = list(filter(lambda x: type(x)==type(1), input))
print(output)
