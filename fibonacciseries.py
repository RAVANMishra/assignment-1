num=int(input('enter any number:'))
n1 ,n2 = 0, 1
n3=0
if num<=0:
    print('please enter num greater then 0')
else:
    for i in range (0,num):
        print(n3,end=' - ')
        n1=n2
        n2=n3
        n3=n1+n2
        

