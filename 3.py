a=[]
a = list(map(int, input().split()))
x=len(a)-1
for i in range(len(a)//2):
    print(a[i],end=' ')
    print(a[x-i],end=' ')
if len(a)%2!=0:
    print(a[i+1])