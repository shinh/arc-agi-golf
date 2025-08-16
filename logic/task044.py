def p(g):# flood fill & match
    g=sum(g,[]);z=[];o={};c=[0]*10
    for i,t in enumerate(g):
        if t<10:
            s=[i];r=[];e=1>t
            while s:
                i=s.pop();v=g[i]
                if v>9or v%10^t:continue
                g[i]=v+10;r+=[i]
                for n in-11,-10,-9,-1,1,9,10,11:
                    if 0<=(j:=i+n)<100 and-1<=j%10-i%10<=1:
                        v=g[j]
                        if v==t:s+=[j]
                        elif v%5:e=0
                    else:e=0
            k=tuple(j-r[0]for j in r)
            if t%5:c[t]+=1;o.setdefault(k,[]);o[k]+=(r,t),
            elif e:z+=(r,k),
    for r,k in z:
        a=o.get(k,[])
        while a:
            q,t=a.pop()
            if c[t]==1:
                for j in q+r:g[j]=t*(j in r)
                break
    return[[x%10 for x in g[i:i+10]]for i in range(0,100,10)]

