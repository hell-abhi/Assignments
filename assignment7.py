input = ['Hello', 'Python', 'Lovers', 'Welcome', '', 'a', 'ab']
output = []
for i in input:
    str = ''
    length = len(i)
    if length==1 or length==0 or length==2:
        output.append('')
    else:
        temp = (i[1:-1])
        output.append(temp)
print(output)


