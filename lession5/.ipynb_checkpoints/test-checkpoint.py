# coding: utf-8
a=[[85,55,34,23],[45,34,55,23],[45,55,88,98]]
a[2][3]
a[1][1]
for row in a:
    for item in row:
        print(item, end=' ')
    print()  
for i,row in enumerate(a):
    for j,item in enumerate(row):
        print(item, end=' ')
    print()    
#total calculate
total=0
items=0
for row in a:
    for item in row:
        total+=item
        items+=1
total/items
for row in a:
    total+=sum(row)
    items+=len(row)
total/items    
