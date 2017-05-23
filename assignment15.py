d = {'team1':'Alpha', 'team2':'Beta', 'team3':'Gamma', 'team4':'Delta'}
k = ['team1', 'teamX', 'team4', 'team5']
output = dict()
for i in k:
    if d.get(i) != None:
        output[i] = d.get(i)
print(output)
