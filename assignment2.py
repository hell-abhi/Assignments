input = [0, 2, 4, 5, 8, 10, 13, 15, 18, 20, 23, 25, 35, 40, 42, 45]
output = []
for i in input:
	if i%5==0 and i!=0:
		output.append(i)
output.sort()
print output
