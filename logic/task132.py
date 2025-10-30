# 162
def p(g):
 w,b=len(g[0]),sum(g,[])
 for v in{*b}-{0}:
  i=b.index;a=i(v);d=i(v,a+1);y,l=sorted((a%w,d%w))
  for r in g[a//w:d//w+1]:r[y:l+1]=[v]*(l-y+1)
 return g

# def p(g):
#     # for each color
#         # find minx,miny,maxx,maxy
#         # if present, fill

# def p(g):
#     # for each cell and each color, if there is said color before and after it x and y, then make that color
#     return [[max( for c in range(10)) for x in range(len(g[0]))]for y in range(len(g))]