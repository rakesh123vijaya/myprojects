n=int(input())
s,c=0,0
k=1
s1,s2=0,1
p=[0]*11
for i in range(n):
    l=input("enter a over")
    a=list(input().split())
    for i in a:
        if i=='w':
            k+=1
            s1=k            
        elif int(i)%2==0:
            p[s1]+=int(i)
        elif int(i)%2!=0:
            p[s2]+=int(i)
    
    for i in a:
        if i!='w':
            s+=int(i)
        else:
            c+=1
    print(s,c)

print("total score: {} for {} wicktes".format(s,c))
        
pn=['virat','rohith','rakesh','vamsi','dhoni','jaddu','hardik','gail','dube','bumra','shami']
d={}
for i in range(11):
    d[pn[i]]=p[i]
print(d)



    
    
