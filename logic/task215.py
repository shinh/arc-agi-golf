# copy row per mod-3 group
# p=lambda g:[max(g[i%3::3])for i in range(len(g))]
p=lambda g,i=2:[max(g[(i:=i+1)%3::3])for _ in g]
# p=lambda g,h=[]:g and[max((g+h)[::3])]+p(g[1:],h+g[:1])
# p=lambda g:[max(g[i::3])for i,_ in zip([0,1,2]*9,g)]
# p=lambda g:[*map(max,zip(g,g[3:]*2))]
