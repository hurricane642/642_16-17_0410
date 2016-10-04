a=[]
a = list(map(int, input().split()))
s=0
k=1
for i in range(9):
    if (a[i]==2 and a[i+1]>2):
        s=s
    else:
        s=s+a[i]
        k=k+1
s=s+a[9]
print(s//k)