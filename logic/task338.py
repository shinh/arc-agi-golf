# Based on 029
# fill holes
def p(g):
 def f(x,y):
  try:
   if g[y][x]<2:g[y][x]=4;f(x,y+1);f(x,y-1);f(x+1,y);f(x-1,y)
  except:0
 f(0,0);f(0,-1)
 return[[3*(v<1)for v in r]for r in g]

# idea
# make all blacks green then flood fill black+red (don't add neighbors if red)

# idea
# # test cases are all rectangles so just replace red black* red with green*
# doesn't handle solid lines and multiple per line
# def p(g):
#     return [for r in g:
#         try:
#           a=r.index(2)
#           b=r.index(2,a+1)
#           r[a]=r[b]=0
#           r[a+2:b+1]=[3]*(b-a-1)
#         except:0
#     return g

# idea
# def p(g):
#     c=0
#     return [[3 if (c:=c+v)==2 and not v else 0 for v in r]for r in g]


# idea regex
# import re
# def p(g):
#     return [for r in g]
