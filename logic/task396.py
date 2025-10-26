def p(a):
 # locate the biggest solid rectangle and recolor it after cropping
 h=len(a)
 m,c,y,x,d,e=max((((D:=next((j for j in range(Y,h)if a[j][X]^f),h))-Y)*((E:=next((i for i in range(X,len(r))if r[i]^f),len(r)))-X),f,Y,X,D,E)for Y,r in enumerate(a)for X,f in enumerate(r)if f)
 g=sum({*sum(a,[])})-c
 return[[[g,v][v!=c]for v in r[x:e]]for r in a[y:d]]
