def p(g):
    # rare edge lines
    a,*_,b=zip(*g);d,*_,e=g;c=min({*a}&{*b}|{*d}&{*e},key=sum(g,[]).count);return[[c*(r[0]==r[-1]==c or x==y==c)for x,y in zip(d,e)]for r in g]
