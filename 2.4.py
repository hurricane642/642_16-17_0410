a = list(map(int, input().split()))
b=a[0]
for i in range(len(a)):
    if a.count(a[i])>a.count(b):
        b=a[i]
print(b)