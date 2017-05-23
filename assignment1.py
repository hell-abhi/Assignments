r = ["laptop", "apple", "boy", "doggy", "cat"]
ans = []
for i in r:
	len = 0
	for j in i:
		len = len+1
	if len > 3:
		ans.append(i)
ans.sort()
print ans
