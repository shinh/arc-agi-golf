# fill rectangle enclosed by 8s with 2
p=lambda g:[[(v or((t:=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v>7])and min(i for i,j in t)<=i<=max(i for i,j in t)and min(j for i,j in t)<=j<=max(j for i,j in t))*2)for j,v in enumerate(r)]for i,r in enumerate(g)]

