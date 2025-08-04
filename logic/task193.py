from collections import defaultdict

def p(g):
    h=len(g);w=len(g[0])
    vis=[[0]*w for _ in g];cnt=defaultdict(int);pal=set()
    for i in range(h):
        for j in range(w):
            pal.add(g[i][j])
            if vis[i][j]:
                continue
            c=g[i][j];cnt[c]+=1;stack=[(i,j)];vis[i][j]=1
            while stack:
                y,x=stack.pop()
                for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                    ny=y+dy;nx=x+dx
                    if 0<=ny<h and 0<=nx<w and not vis[ny][nx] and g[ny][nx]==c:
                        vis[ny][nx]=1;stack.append((ny,nx))
    mc=max(cnt,key=cnt.get)
    bg=min([c for c in pal if c!=mc] or [mc])
    out=[[bg]*w for _ in g]
    for i in range(h-1):
        for j in range(w-1):
            if g[i][j]==g[i+1][j]==g[i][j+1]==g[i+1][j+1]==mc:
                out[i][j]=out[i][j+1]=out[i+1][j]=out[i+1][j+1]=mc
    return out
