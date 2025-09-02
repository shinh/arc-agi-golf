# stack unique non-zero colors; rotate if every row has one
p=lambda g:len(o:=[[*s]for r in g if(s:={*r}-{0,5})])^len(g)and[r*len(o)for r in o]or[*zip(*p([*zip(*g)]))]

