input = [0,2,4,5,8,10,13,15,18,20,23,25,35,40,42,45]
n = 2
output = [str(x) for x in input if x%5==0 and x!=0]
output.sort()
print(output)
