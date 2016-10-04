n=int(input())
a = list(map(int, input().split()))
b=a[1]
s1=s2=max=0
for i in range(n):
    for m in range(n):
        if a[i]>a[m]:
            s1+=1
        elif a[i]<a[m]:
            s2+=1
    if s1==s2:
        max=i
    s1=s2=0
print(a[max])