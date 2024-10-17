"""
    1 2 3 4 5
    16 17 18 19 6
    15 24 25 20 7
    14 23 22 21 8
    13 12 11 10 9
"""
n=int(input("enter a number "))
c=n
r=n
x=0
y=0
t=1
l=[[0 for i in range(n)] for j in range(n)]
pp=[]
while(y<=c and x<=r):
    for i in range(y,c,+1):
        l[y][i]=t
        t+=1
    x+=1

    for i in range(x,r,+1):
        l[i][r-1]=t
        t+=1
    c-=1

    for i in range(c,y,-1):
        l[c][i-1]=t
        t+=1
    r-=1

    for i in range(r,x,-1):
        l[i-1][y]=t
        t+=1
    y+=1

for i in range(n):
    for j in range(n):
        print(l[i][j],end=" ")
        if(l[i][j]%11==0):
            pp.append((i,j))
    print()

print("total power points:"+str(len(pp)+1))
print("(0,0)")
for i in pp:
    print(i)
