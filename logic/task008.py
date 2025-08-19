import re
p=lambda g,n=39:-n*g or p([*map(list,zip(*[[[[0,8,2,8][(c>7)+(p==2)*2],c][not re.search(r"2, 0[,0 ]+8",s:=str(g))or"2, 8"in s]for c,p in zip(r,[0]+r)]for r in g][::-1]))],n-1)
