a=[]
k=int(input())
n=int(input())
for i in range(k):
    a.append(1)
for i in range(n+1):
    if i>(k-1):
        a.append(sum(a[i-k:i]))
print(a[len(a)-1])