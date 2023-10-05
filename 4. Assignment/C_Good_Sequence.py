n=int(input())
arr=list(map(int,input().split()))

counter={}
for i in arr:
    if i in counter:
        counter[i]+=1
    else:
        counter[i]=1
rmv=0
for key,val in counter.items():
    if key<val:
        rmv+=val-key
    elif key>val:
        rmv+=val
print(rmv)