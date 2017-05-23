from operator import itemgetter
name = input("Enter your name\n")
db = dict()
flag = True
f = open('output.txt','w+')
for line in f:
	value, key = line.split()
	db[key] = value
while flag:
	number = input("Enter your number\n")
	if not flag:
		f.write(name)
		f.write(' ')
		f.write(number)
		break
	if db.get(number)==None:
		flag = False
		db[number] = name
sorted_x = sorted(db.items(), key=itemgetter(1))
print(sorted_x)
f.close()
