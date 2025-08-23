# rotate flood-fill to erode 5-pixels
p=lambda g,f=lambda m:[[*map(min,r,r[1:]),0]for r in zip(*m[::-1])]:[[c-d*.6 for c,d in zip(*t)]for t in zip(g,f(f(f(f(g)))))]

