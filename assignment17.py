ip = [1,2,3,4,5,4,2,1,5,6,7,8,2,4,6]
op = dict()
for i in ip:
    if op.get(i)==None:
        op[i] = 1
    else:
        op[i] = op[i]+1
print(op)
