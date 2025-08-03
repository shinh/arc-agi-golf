def p(g):
    # gは二次元配列で、0-9の値が入っています。gは二次元配列で、0-9の値が入っています。
    # 2の図形を8に接続される方向に動かしてください
    a=[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==2];b=[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==8]
    ys,xs=zip(*a);Ys,Xs=zip(*b)
    y1,y2=min(ys),max(ys);x1,x2=min(xs),max(xs);Y1,Y2=min(Ys),max(Ys);X1,X2=min(Xs),max(Xs);dx=dy=0
    if x2<X1:dx=X1-x2-1
    elif x1>X2:dx=X2-x1+1
    elif y2<Y1:dy=Y1-y2-1
    else:dy=Y2-y1+1
    o=[r[:]for r in g]
    for y,x in a:o[y][x]=0
    for y,x in a:o[y+dy][x+dx]=2
    return o
