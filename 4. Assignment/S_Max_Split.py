st = input()
s = ''
strlist=[]
lcount = 0
rcount = 0
for c in st:
    if lcount!=0 and rcount!=0:
        if lcount==rcount:
            strlist.append(s)
            s=''
            lcount=0
            rcount=0
    if c == 'R':
        rcount += 1
        s+=c
    elif c == 'L':
        lcount += 1
        s+=c
strlist.append(s)

print(len(strlist))
for x in strlist:
    print(x)