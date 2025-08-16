def p(g):
 # dedupe+mirror
 u=lambda a:dict.fromkeys(map(tuple,a));t=lambda g:[*map(list,zip(*g))];r=lambda a:a+a[-2::-1]
 return r(t(r(t(u(t(u(g)))))))
