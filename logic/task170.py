def p(g):
    # shrink first region to leftover
    h=len(g);w=len(g[0])
    for n in range(h*w):
     y,x=divmod(n,w)
     if k:=g[y][x]:
      r=[(y,x)];g[y][x]=0
      for i,j in r:
       for a in-1,0,1:
        for b in-1,0,1:
         if a|b and 0<=(p:=i+a)<h and 0<=(q:=j+b)<w and g[p][q]==k:
          g[p][q]=0;r+=(p,q),
      break
    y,x=zip(*r);u=min(y);v=min(x);U=max(y)-u+1;V=max(x)-v+1;r=[(i-u,j-v)for i,j in r]
    y,x=zip(*((i,j)for i in range(h)for j in range(w)if g[i][j]));a=min(y);b=max(y)+1;c=min(x);d=max(x)+1;b-=a;d-=c
    return [[g[i][j]*(((i-a)*U//b,(j-c)*V//d)in r)for j in range(c,c+d)]for i in range(a,a+b)]
