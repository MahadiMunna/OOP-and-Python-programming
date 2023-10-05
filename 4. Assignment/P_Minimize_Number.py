n=int(input())
arr=list(map(int,input().split()))
flag=False
op=0
for i in arr:
    if i%2==1:
        flag=True
while True:
    if flag==True:
        break
    for i,num in enumerate(arr):
        x=num/2
        if x%2==1:
            flag=True
        arr[i]=x
    op+=1
print(op)