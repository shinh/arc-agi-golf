p=lambda g:(h:=g[:3])==[*map(list,zip(*h))]and p(g[3:])or h # find first non symmetric 3x3
