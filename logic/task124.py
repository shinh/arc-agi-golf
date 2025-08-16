def p(g):
    # find shift and repeat
    h,w=len(g),len(g[0])
    fg=[(i,j,g[i][j])for i in range(h)for j in range(w)if g[i][j]]
    dy,dx=max(((m,dy*dx,dy,dx)for dy in range(1,6)for dx in range(-w,w)if(m:=sum(0<=i+dy<h and 0<=j+dx<w and g[i+dy][j+dx]==v for i,j,v in fg))==(sum(0<=i+dy<h and 0<=j+dx<w for i,j,v in fg))>0),default=(0,0,1,0))[2:]
    out=[[0]*w for _ in range(10)]
    for i,j,v in fg:
        for n in range(10):
            if 9>=i+dy*n>=0<=j+dx*n<w:out[i+dy*n][j+dx*n]=v
    return out
