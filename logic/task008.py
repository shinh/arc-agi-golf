import re
# slide the 2-object until it touches the 8-object
p=lambda g,n=39,s=re.search:-n*g or p([*zip(*[[[c//8*8or q&2,c][not s("2, 0[^[(]*8",t:=str(g))or"2, 8"in t]for c,q in zip(R,[0,*R])]for R in g][::-1])],n-1)
