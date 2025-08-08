
def p(g):
    h=len(g);w=len(g[0]);r=[s for s in g];S=set();D=(-1,0,1)
    for i in range(h):
        for j in range(w):
            if g[i][j]==0 or (i,j) in S:continue
            st=[(i,j)];c=[]
            while st:
                x,y=st.pop()
                if (x,y) in S or g[x][y]==0:continue
                S.add((x,y));c.append((x,y))
                for a in D:
                    for b in D:
                        if a or b:
                            u,v=x+a,y+b
                            if 0<=u<h and 0<=v<w:st.append((u,v))
            cols=[g[x][y] for x,y in c];m=max(cols,key=cols.count)
            maj=[(x,y) for x,y in c if g[x][y]==m]
            mins=[(x,y,g[x][y]) for x,y in c if g[x][y]!=m]
            mi=min(x for x,y in maj);mj=min(y for x,y in maj)
            H=max(x for x,y in maj)-mi+1;W=max(y for x,y in maj)-mj+1
            pat=[(x-mi,y-mj) for x,y in maj]
            for x,y,v in mins:
                di=(x-mi)//H;dj=(y-mj)//W
                pts=[(H-1-p,q) for p,q in pat] if di%2 else pat
                if dj%2:pts=[(p,W-1-q) for p,q in pts]
                oi=mi+di*H;oj=mj+dj*W
                for p,q in pts:
                    if 0<=oi+p<h and 0<=oj+q<w:r[oi+p][oj+q]=v
    return r
