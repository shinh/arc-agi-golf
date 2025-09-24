def p(g):
    # expand rare color rectangle outward
    w=len(g[0]);c=min(a:=sum(g,[]),key=a.count)
    p=a.index(c);q=a.index(c,-~p);Y=q//w
    return[[[r[j],c][max(Y-i,i-Y,abs(j-q%w))%(Y-p//w)<1]for j in range(w)]for i,r in enumerate(g)]
