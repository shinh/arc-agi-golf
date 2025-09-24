# repeat diagonal colors
p=lambda g,r=range(10):[[g[_:=max(y,x)%(4+any(g[4]))][_]for x in r]for y in r]
