def p(g):
    h=len(g);w=len(g[0])
    for y in range(h):
        for x in range(w):
            if g[y][x]<1:continue
            q=[(y,x)];g[y][x]=-g[y][x];s={(y,x)};cnt={}
            while q:
                i,j=q.pop();d=-g[i][j];cnt[d]=cnt.get(d,0)+1
                for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                    ni,nj=i+dy,j+dx
                    if 0<=ni<h and 0<=nj<w and g[ni][nj]>0:
                        g[ni][nj]=-g[ni][nj];q.append((ni,nj));s.add((ni,nj))
            lc=min(cnt,key=cnt.get);mc=max(cnt,key=cnt.get)
            for ci,cj in s:
                if -g[ci][cj]==lc:break
            for dy,dx in((-1,0),(1,0),(0,-1),(0,1)):
                if (ci+dy,cj+dx)not in s:break
            n=0;i,j=ci-dy,cj-dx
            while(i,j)in s:n+=1;i-=dy;j-=dx
            if dy:
                t=ci-n if dy>0 else 0;B=h-1 if dy>0 else ci+n;l=max(0,cj-n);r=min(w-1,cj+n)
            else:
                t=max(0,ci-n);B=min(h-1,ci+n);l=cj-n if dx>0 else 0;r=w-1 if dx>0 else cj+n
            for i in range(t,B+1):g[i][l:r+1]=[-mc]*(r-l+1)
            i,j=ci,cj
            while 0<=i<h and 0<=j<w:
                if t<=i<=B and l<=j<=r:g[i][j]=-lc
                i+=dy;j+=dx
    return[[abs(c)for c in r]for r in g]

