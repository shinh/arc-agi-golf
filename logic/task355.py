def p(g):b=min(s:=sum(g,[]),key=s.count);return[[max(d:=[sum({*r}&{*c}) for c in zip(*g) for r,v in zip(g,c)if v==b],key=d.count)-b]]
