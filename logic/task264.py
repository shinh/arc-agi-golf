from collections import Counter,deque

def p(g):
    h=len(g);w=len(g[0])
    b,l=[x[0]for x in Counter(v for r in g for v in r).most_common(2)]
    s=[[0]*w for _ in g];o=[]
    for i in range(h):
        for j in range(w):
            c=g[i][j]
            if s[i][j] or c in(b,l):continue
            q=deque([(i,j)]);s[i][j]=1;cs=[]
            while q:
                x,y=q.popleft();cs.append((x,y))
                for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                    nx,ny=x+dx,y+dy
                    if 0<=nx<h and 0<=ny<w and not s[nx][ny] and g[nx][ny]==c:
                        s[nx][ny]=1;q.append((nx,ny))
            o.append((c,cs))
    def cl(cs):
        mi=min(i for i,_ in cs);mj=min(j for _,j in cs)
        S={(i-mi,j-mj)for i,j in cs}
        h=max(i for i,_ in S)+1;w=max(j for _,j in S)+1;m=(h//2,w//2)
        def pt(f):return{(i,j)for i in range(h)for j in range(w)if f(i,j)}
        d={'UL':pt(lambda i,j:(i==0 and j<2)or(j==0 and i<2)),
           'UR':pt(lambda i,j:(i==0 and j>=w-2)or(j==w-1 and i<2)),
           'LL':pt(lambda i,j:(i==h-1 and j<2)or(j==0 and i>=h-2)),
           'LR':pt(lambda i,j:(i==h-1 and j>=w-2)or(j==w-1 and i>=h-2)),
           'T': pt(lambda i,j:i==0 or j==m[1]),
           'B': pt(lambda i,j:i==h-1 or j==m[1]),
           'L': pt(lambda i,j:j==0 or i==m[0]),
           'R': pt(lambda i,j:j==w-1 or i==m[0])}
        for k,v in d.items():
            if S==v:return k
    P={'UL':(0,0),'T':(0,1),'UR':(0,2),'L':(1,0),'R':(1,2),'LL':(2,0),'B':(2,1),'LR':(2,2)}
    out=[[l]*9 for _ in range(9)]
    for c,cs in o:
        o8=cl(cs);r,cx=P[o8];rr=r*3;cc=cx*3
        if o8=='UL':out[rr][cc]=out[rr][cc+1]=out[rr+1][cc]=c
        elif o8=='UR':out[rr][cc+1]=out[rr][cc+2]=out[rr+1][cc+2]=c
        elif o8=='LL':out[rr+1][cc]=out[rr+2][cc]=out[rr+2][cc+1]=c
        elif o8=='LR':out[rr+1][cc+2]=out[rr+2][cc+1]=out[rr+2][cc+2]=c
        elif o8=='T':out[rr][cc:cc+3]=[c]*3;out[rr+1][cc+1]=c
        elif o8=='B':out[rr+2][cc:cc+3]=[c]*3;out[rr+1][cc+1]=c
        elif o8=='L':
            for k in range(3):out[rr+k][cc]=c
            out[rr+1][cc+1]=c
        else:
            for k in range(3):out[rr+k][cc+2]=c
            out[rr+1][cc+1]=c
    return out

