# prefer the color most aligned with the rare value
p=lambda g:[[max(d:=[sum({*r}&{*c}) for c in zip(*g) for r,v in zip(g,c)if v==(b:=min(s:=sum(g,[]),key=s.count))],key=d.count)-b]]
