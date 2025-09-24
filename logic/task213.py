# stack colors; rotate if full
p=lambda g:g[(n:=len(o:=[[*s]for r in g if(s:={*r}-{0,5})])):]and[r*n for r in o]or[*zip(*p([*zip(*g)]))]
