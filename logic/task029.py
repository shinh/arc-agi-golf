# Just solved.
#
# Test cases are somewhat tough. There are tasks which assume 1px output like
#
# 111
# 121
# 111
#
# and and another task contains both the above pattern and a larger pattern.
# this is 203B after minifiy and zlib
# def p(g):
#     # brute-force scan for the largest framed rectangle
#     return max(([r[sx:ex+1]for r in g[sy:ey+1]]for sy in range(1,len(g)-1)for sx in range(1,len(g[0])-1)for ey in range(sy,len(g)-1)for ex in range(sx,len(g[0])-1)if{*g[sy-1][sx-1:ex+2],*g[ey+1][sx-1:ex+2],g[sy][ex+1],*[r[sx-1]for r in g[sy-1:ey+2]]}<={g[sy][sx-1]}),key=len)

# idea for another approach, that I don't think would be shorter
# return the stuff enclosed in a rectangle if the border is a rectangle (all same color), otherwise empty list.
# def is_rect(a):
#     # rotate the rectangle 4 times and apply logic at top, rather than duplicate logic 4 times.
#     if len(a)<3: return []
#     if len(a[0])<3: return []
#     c=a[0][0]
#     for _ in range(4):
#         if a==[]: return []
#         if set(a[0])==set([c]):
#             a = a[1:]
#             # rotate
#             a = list(map(list, zip(*a)))[::-1]
#         else:
#             return []
#     return a
#
# def p(g):
#     Y=range(len(g))
#     X=range(len(g[0]))
#     a=[]
#     for y1 in Y:
#         for y2 in Y:
#             for x1 in X:
#                 for x2 in X:
#                     b=[r[x1:x2+1] for r in g[y1:y2+1]]
#                     r=is_rect(b)
#                     if len(r)>len(a): a=r
#     print(a)
#     return a

# another idea, possibly use itertools.combinations to avoid double loops for each dimension

# Finally found a good approach. Crop 10 times.
def p(g):
    for c in range(10):
        f=lambda g:[*map(list,zip(*[r for r in g if c in r]))]
        n=[r[1:-1]for r in f(f(g))[1:-1]]
        if c not in sum(n,[])and n:
            return n
