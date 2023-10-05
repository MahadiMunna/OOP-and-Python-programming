x=int(input())
n=int(input())
sum=0
for i in range(2,n,2):
    sum=sum+x**i
print(sum)