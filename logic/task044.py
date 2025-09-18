def p(g):# flood fill & match
    g=sum(g,[]);z=[];o={};c=[0]*10
    for i,t in enumerate(g):
        if t<10:
            s=[i];r=[i];g[i]+=10;e=1>t
            while s:
                i=s.pop()
                for n in-11,-10,-9,-1,1,9,10,11:
                    if 0<=(j:=i+n)<100 and-1<=j%10-i%10<=1:
                        v=g[j]
                        if v==t:s+=j,;g[j]+=10;r+=j,
                        elif v%5:e=0
                    else:e=0
            k=tuple(j-r[0]for j in r)
            if t%5:o[k]=o.get(k,[])+[(r,t)];c[t]+=1
            elif e:z+=(r,k),
    for r,k in z:
        for q,t in o.get(k,()):
            if c[t]==1:
                for j in q+r:g[j]=t*(j in r)
                break
    return[[x%10 for x in g[i:i+10]]for i in range(0,100,10)]

