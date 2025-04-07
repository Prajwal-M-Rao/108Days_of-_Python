l1=[10,20,30]
l2=[40,50,60]
print(l1+l2)
#print(l1*l2) #Error
print(l1*3)
#print(l1/l2) #Error
print(10 in l1)
print(30 not in l1)
print(30 not in l2)
#print(l1-l2) #Error


a=[10,20,30,40,[10.1,20.2,['a','b'],30.3],50,60,70,[40.4,50.5,['c','d'],60.6],80,90]
print("len of list ",len(a))
print(a[2])
print(a[4][2])
print(a[4][2][0])
print(a[7])
print(a[8][1])
print(a[8][2][0])