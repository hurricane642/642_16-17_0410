a = list(map(int, input().split()))
t=int(input())
for i in range(t):
    a.insert(len(a)-1-a[len(a)-1],a[len(a)-1])
    del a[len(a)-1]
print(' '.join(map(str,a)))