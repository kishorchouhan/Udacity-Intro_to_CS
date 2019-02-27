def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)
    a = p

# To test, uncomment all lines 
# below except those beginning with >>>.
a = [1,2,3]
b = [2,4,6]
union(a,b)
print (a) 
#>>> [1,2,3,4,6]
print (b)
#>>> [2,4,6]
