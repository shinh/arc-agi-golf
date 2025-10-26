def p(g):
 for _ in'<'*4:x=bytes(map(max,g));f=x.find;a=f(2);b=x.rfind(2)+1;c=f(8);g=[*zip(*(g,g[:a]+g[b:c]+g[a:b]+g[c:])[c>b])][::-1]
 return g
