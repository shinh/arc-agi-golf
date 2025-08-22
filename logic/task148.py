def p(g):
    # link every 8 to the side wall then duplicate its row
    w=len(g[0]);s=sum(g,[]);p=[divmod(i,w)for i,v in enumerate(s)if v&6==2];e=[divmod(i,w)for i,v in enumerate(s)if v&8]
    l,a=min((x,y)for y,x in p);r,b=max((x,-y)for y,x in p);o=-b-a
    if all((g[y][l]-2)*(x-l)for y,x in e):l=r;o=-o
    for y,x in e:
        a,b=sorted((l,x));g[y][a:b]=[8]*(b-a);g[y][x]=4;y+=o
        if 0<=y<len(g):g[y]=[8]*w
    for y,x in p:g[y][x]=2
    return g
