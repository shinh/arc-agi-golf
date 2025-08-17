# rotate flood-fill to erode 5-pixels
p=lambda g:(m:=g,[m:=[[*map(int.__and__,r,r[1:]),0]for r in zip(*m[::-1])]for _ in[0]*4])and[[c-d/5*3 for c,d in zip(*t)]for t in zip(g,m)]

