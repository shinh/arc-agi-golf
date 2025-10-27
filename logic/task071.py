def p(a):r=max(a,key=any);s=r.index(v:=max(r))+15-r[::-1].index(v);return[[v*(r[x]==v or r[s-x:s-x+1]==[v])for x in range(16)]for r in a]
