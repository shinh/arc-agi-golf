# dedupe+mirror
p=lambda g,u=lambda a:{}.fromkeys(map(tuple,a)),t=lambda a:[*map(list,zip(*a))],r=lambda a:a+a[-2::-1]:r(t(r(t(u(t(u(g)))))))
