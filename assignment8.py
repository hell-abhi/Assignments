input = ['Hello', 'Python', 'Lovers', 'Welcome']
n = 2
output = []
for i in input:
    temp = (i[:n])
    temp += i[n+1:]
    output.append(temp)
print(output)


