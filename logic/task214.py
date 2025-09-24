p=lambda g:[[*r[:4],*u,*t[3::-1]]for r,u,t in zip(g,zip(*g[::-1]),g[::-1])]#rot+mir
