def p(g):
 for _ in'1111':
  x=bytes(map(max,g));a=x.find(2);b=x.rfind(2)+1;c=x.find(8)
  g=[*zip(*((g,g[:a]+g[b:c]+g[a:b]+g[c:])[c>b]))][::-1]
 return g