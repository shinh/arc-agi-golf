def p(g):
    h=len(g);w=len(g[0]);f=sum(g,[]);bg=max(f,key=f.count);v=set();o=[]
    for y in range(h):
        for x in range(w):
            if g[y][x]==bg or (y,x)in v:continue
            q=[(y,x)];v.add((y,x));c=[];cnt={}
            while q:
                i,j=q.pop();c.append((i,j));d=g[i][j];cnt[d]=cnt.get(d,0)+1
                for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                    ni,nj=i+dy,j+dx
                    if 0<=ni<h and 0<=nj<w and g[ni][nj]!=bg and (ni,nj)not in v:
                        v.add((ni,nj));q.append((ni,nj))
            o.append((c,cnt))
    for c,cnt in o:
        lc=min(cnt,key=lambda k:(cnt[k],k));mc=max(cnt,key=lambda k:(cnt[k],k))
        mi=h;ma=-1;mj=w;mk=-1
        for i,j in c:
            if g[i][j]==lc:
                if i<mi:mi=i
                if i>ma:ma=i
                if j<mj:mj=j
                if j>mk:mk=j
        ci=(mi+ma)//2;cj=(mj+mk)//2;s=set(c)
        for dy,dx in((-1,0),(1,0),(0,-1),(0,1)):
            if (ci+dy,cj+dx)not in s:break
        n=0;i,j=ci-dy,cj-dx
        while (i,j)in s:n+=1;i-=dy;j-=dx
        if dy:
            t=0 if dy<0 else ci-n;B=ci+n if dy<0 else h-1;l=max(0,cj-n);r=min(w-1,cj+n)
        else:
            t=max(0,ci-n);B=min(h-1,ci+n);l=0 if dx<0 else cj-n;r=cj+n if dx<0 else w-1;l=max(0,l);r=min(w-1,r)
        for i in range(t,B+1):
            row=g[i]
            for j in range(l,r+1):row[j]=mc
        i,j=ci,cj
        while 0<=i<h and 0<=j<w:
            if t<=i<=B and l<=j<=r:g[i][j]=lc
            i+=dy;j+=dx
    return g
