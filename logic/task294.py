# rotate flood-fill to erode 5-pixels
p=lambda g:(m:=g,[m:=[[a&b for a,b in zip(r,r[1:]+(0,))]for r in zip(*m[::-1])]for _ in' '*4])and[[c-d*3//5 for c,d in zip(r,m)]for r,m in zip(g,m)]
