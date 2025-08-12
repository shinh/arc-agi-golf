# rotate the grid so that 1 flows in one direction
p=lambda g,n=144:n and p([[a or b==1 for a,b in zip(r,r[1:]+(0,))]for r in zip(*g[::-1])],n-1)or g

