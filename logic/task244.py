def p(g):
    #slice+flip
    k=sum(2>len({*r})for r in g)+1;s=-~len(g)//k
    return[r[:k*s:s][::-1]for r in g[:k*s:s]]
