p=lambda g:len(o:=[[*s]for r in g if len(s:={*r}-{0,5})])==len(g)and[*zip(*p([*zip(*g)]))]or[r*len(o)for r in o]

