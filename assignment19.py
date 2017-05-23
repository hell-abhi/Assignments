from calendar import monthrange
name = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
def schedule(month):
    n = monthrange(2017,name[month])
    i=1
    st=n[0]
    while i <= n[1]:
        if st==6:
            print("On %d, %s 2017: All cars are allowed"%(i,month))
        elif i%2==0:
            print("On %d, %s 2017: Even cars are allowed"%(i,month))
        else:
            print("On %d, %s 2017: Odd cars are allowed" % (i, month))
        i = i+1
        st = (st+1)%7
schedule('January')
