def p(g):
    # gは二次元配列で、0-9の値が入っています。gは二次元配列で、0-9の値が入っています。
    # 2の図形を8に接続される方向に動かしてください
    a=[];b=[];[(a,b)[v>2].append((y,x))for y,r in enumerate(g)for x,v in enumerate(r)if v%6==2]
    y1,x1=map(min,zip(*a));y2,x2=map(max,zip(*a));Y1,X1=map(min,zip(*b));Y2,X2=map(max,zip(*b))
    dx=X1-x2-1 if x2<X1 else X2-x1+1 if x1>X2 else 0;dy=(Y1-y2-1 if y2<Y1 else Y2-y1+1)*(not dx)
    for y,x in a:g[y][x]=0
    for y,x in a:g[y+dy][x+dx]=2
    return g
