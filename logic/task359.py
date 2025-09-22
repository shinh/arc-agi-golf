p=lambda g,e=enumerate:[[max(a:=g[y]+[*[*zip(*g)][x]],key=a.count) for x,v in e(r)] for y,r in e(g)]
