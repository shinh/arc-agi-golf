def p(g):# surround unique cell with 2s
    a=sum(g,[]);v=min(a,key=a.count);y,x=divmod(a.index(v),10);r=range(10)
    o=[[2*(2>i-y>-2<j-x<2)for j in r]for i in r]
    o[y][x]=v;return o

