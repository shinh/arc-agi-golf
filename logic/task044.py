def p(g):
    g=sum(g,[]);d=(-11,-10,-9,-1,1,9,10,11)
    z=[];o={};c=[0]*10
    def f(i):
        t=g[i]%10;s=[i];r=[];e=not t
        while s:
            i=s.pop();v=g[i]
            if v>9 or v%10!=t:continue
            g[i]=v+10;r.append(i)
            for n in d:
                j=i+n
                if 0<=j<100 and abs(j%10-i%10)<=1:
                    v=g[j]
                    if v<10 and v%10==t:s.append(j)
                    elif not t and v%10 and v%10-5:e=0
                elif not t:e=0
        return r,e
    for i in range(100):
        if g[i]<10:
            r,e=f(i);t=g[i]%10
            if t and t!=5:
                c[t]+=1;Y=r[0];k=tuple(j-Y for j in r)
                o.setdefault(k,[]).append((r,t))
            elif not t and e:z.append(r)
    for r in z:
        Y=r[0];k=tuple(j-Y for j in r);a=o.get(k)
        if a:
            i=next((i for i,(q,t) in enumerate(a) if c[t]==1),-1)
            if i+1:
                q,t=a.pop(i)
                for j in q:g[j]=0
                for j in r:g[j]=t
    return[[x%10 for x in g[i:i+10]]for i in range(0,100,10)]

