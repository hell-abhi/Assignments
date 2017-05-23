input = ['Hello', 'Python', 'Lovers', 'Welcome']
n = 2
output = []
for i in input:
    str = ''
    length = len(i)
    if length==1 or length==0 or length==2:
        output.append('')
    else:
        temp = (i[:n])
        temp += i[n+1:]
        output.append(temp)
print(output)


