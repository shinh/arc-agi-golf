# copy row per mod-3 group
p=lambda g:[max(g[i%3::3])for i in range(len(g))]

