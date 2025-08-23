# dedupe+mirror
p=lambda g,T=lambda a:[*zip(*{}.fromkeys(map(tuple,a)))],r=lambda a:a+a[-2::-1]:r([*zip(*r(T(T(g))))])
