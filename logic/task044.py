def p(g):
    g=sum(g,[]);z=[];o={};c=[0]*10
    for i in range(100):
        if g[i]>9:continue
        t=g[i]%10;s=[i];r=[];e=t<1
        while s:
            i=s.pop();v=g[i]
            if v>9 or v%10^t:continue
            g[i]=v+10;r+=i,
            for n in(-11,-10,-9,-1,1,9,10,11):
                j=i+n
                if 0<=j<100 and-1<=j%10-i%10<=1:
                    v=g[j]
                    if v%10==t<10:s+=j,
                    elif t<1 and v%10*(v%10-5):e=0
                elif t<1:e=0
        k=tuple(j-r[0]for j in r)
        if t%5:c[t]+=1;o.setdefault(k,[]).append((r,t))
        elif t<1<e+1:z.append((r,k))
    for r,k in z:
        for q,t in o.get(k,[]):
            if c[t]<2:
                for j in q+r:g[j]=t*(j in r)
                o[k].remove((q,t));break
    return[[x%10 for x in g[i:i+10]]for i in range(0,100,10)]

