input = ['Hello', 'Python', 'Lovers', 'Welcome']
n = 2
output = [x[:n]+x[n+1:] for x in input]
print(output)
