def f(g):p=();return(p:=r for r in g if r!=p)
p=lambda g:tuple(f(zip(*f(zip(*g)))))#d
