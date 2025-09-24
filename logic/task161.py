def p(g):# edge
    a,*_,b=zip(*g);d,*_,e=g;c=min({*a,*d}&{*b,*e},key=sum(g,[]).count);return[[c*(r[0]==r[-1]==c or x==y==c)for x,y in zip(d,e)]for r in g]
