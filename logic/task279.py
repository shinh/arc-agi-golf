# flood fill using rotation like task002
# 247
# f=lambda G,n=63:-n*G or f([[a or b&1 for a,b in zip(r,r[1:]+(0,))]for r in zip(*G[::-1])],n-1)
# p=lambda g:(A:=f([[1]*(l:=len(g[0])+2)]+[[1]+[2*(c<9)for c in r]+[1]for r in g]+[[1]*l]),B:=f([[-~c%3 for c in r]for r in A]),[[[9,8-7*(b<1)][a>1]for a,b in zip(r1,r2)][1:-1]for r1,r2 in zip(A,B)][1:-1])[2]

# def fill(g, c, y, x, prev):
#     if g[y][x] == 9: return False
#     if g[y][x] == c: return True
#     g[y][x]=c
#     loop = False
#     for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
#         newy = y+dy
#         newx = x+dx
#         if 0<=newy<len(g) and 0<=newx<len(g[0]) and (newy,newx) != prev:
#             loop |= fill(g,c,newy,newx,(y,x))
#     return loop
#
# def p(g):
#     for y in range(len(g)):
#         for x in range(len(g[0])):
#             if not fill(g,8,y,x,0):
#                 fill(g,1,y,x,0)
#     return g

# rather than check each cardinal direction, check all points and see if manhatten distance == 1 (slow but shorter because looping is same as main fns looping so zlib for the win).
# 210
# def fill(g, c, oy, ox, prev):
#     if g[oy][ox] == 9: return 1
#     if g[oy][ox] == c: return 0
#     g[oy][ox]=c
#     return all(fill(g,c,y,x,(oy,ox)) for y in range(len(g)) for x in range(len(g[0])) if (oy-y)**2+(ox-x)**2==( (y,x) != prev))
#
# def p(g):
#     [fill(g,1,y,x,0) for y in range(len(g)) for x in range(len(g[0])) if fill(g,8,y,x,0)]
#     return g


# red = 9
# input = 1
# cycle = 8

# dye background black
# dye blues that border red (or light blue) light blue
# then dye black red
# 191
# def p(g):
#     for i in range(80):
#         g=[[0 if a==9 and b==0 else a for a,b in zip(r,(0,*r))] for r in zip(*g[::-1])]
#
#
#     for i in range(80):
#         g=[[8 if a==1 and (b==9 or b==8) else a for a,b in zip(r,(0,*r))] for r in zip(*g[::-1])]
#
#     for i in range(80):
#         g=[[9 if a==0 else a for a,b in zip(r,(0,*r))] for r in zip(*g[::-1])]
#     return g

# use magic formulas to not repeat similar logic 3 times

# 141, still improvement possible in magic formulas and possibly recursion method/logic
A=0,8,9
p=lambda g,i=0: g*(i-399) or p([[[c1:=A[-~(j:=i//80)//2],a][a!=9-c1 or b!=A[-j%3]] for a,b in zip(r,(0,*r))] for r in zip(*g[::-1])],i+1)
