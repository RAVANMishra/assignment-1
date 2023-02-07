#series
n=(1,2,3,4,5,6,7,9,10)
even,odd =0,0
for i in n:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)