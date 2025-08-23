# move patterns from one half onto the other
def p(g):
    #print(f"{len(g)=} {len(g[0])=}")
    #show(g,"input")
    f=sum(g,[])
    c=sorted({*f},key=f.count)
    F=c[:-2]
    g,o=[[[r[:len(g[0])//2]for r in g],[r[len(g[0])//2:]for r in g]],[g[:len(g)//2],g[len(g)//2:]]][len(g)>len(g[0])]
    if(b:=c[-1])in g[0]:g,o=o,g
    #show(g,"from")
    #show(o,"to")
    s=[]
    B=[]
    z=[[0]*99]
    for y in range(len(g)):
        for x in range(len(g[0])):
            if(y,x)not in s:
                Y=X=0
                while(g+z)[y+Y+1][x]in F:Y+=1
                while(g[y]+[0])[x+X+1]in F:X+=1
                if Y*X:
                    #print(f'found block {sy=} {sx=} {ey=} {ex=} {ly=} {lx=} {pc=} {bc=}')
                    for dy in range(Y):
                        for dx in range(X):
                            s+=(y+dy,x+dx),
                    B+=(Y+1,X+1,y,x),
    for Y,X,y,x in sorted(B)[::-1]:
        p=[*{g[y+dy][x+dx]for dy in range(Y)for dx in range(X)}-{c[-3]}][0]
        for ty in range(len(g)-Y+1):
            for tx in range(len(g[0])-X+1):
                if all(o[ty+dy][tx+dx]==[b,p][g[y+dy][x+dx]==p] if Y>dy>-1<dx<X else((o+z)[ty+dy]+[0])[tx+dx]!=p for dy in range(-1,Y+1) for dx in range(-1,X+1)):
                    #print(f'found dest! {ty=} {tx=}')
                    for dy in range(Y):
                        for dx in range(X):
                            o[ty+dy][tx+dx]=g[y+dy][x+dx]
                    #show(o,"fill")
    return o

# The original, AI authored code
#
# # move patterns from one half onto the other
# def p(g):
#  h=len(g);w=len(g[0])
#  B,O=[[[r[:w//2]for r in g],[r[(w+1)//2:]for r in g]],[g[:h//2],g[(h+1)//2:]]][h>w]
#  F=sum(B,[]);G=sum(O,[])
#  if len({*F})>len({*G}):B,O,F,G=O,B,G,F
#  d=max(F,key=F.count);e=max(G,key=G.count)
#  H,W=len(B),len(B[0]);P=[p:=[d]*(W+2)]+[[d]+r+[d]for r in B]+[p]
#  if not(G:=[v for v in G if v-e]):return B
#  f=max(G,key=G.count);h,w=len(O),len(O[0])
#  for i in range(h):
#     for j in range(w):
#      if O[i][j]-e:
#       q=[(i,j)];o=[]
#       while q:
#        x,y=q.pop()
#        if 0<=x<h and 0<=y<w and O[x][y]-e:
#         v=O[x][y];O[x][y]=e;o+=[(v,x,y)];q+=(x+1,y),(x-1,y),(x,y+1),(x,y-1)
#       _,X,Y=zip(*o);r=min(X);R=max(X);c=min(Y);C=max(Y);u=R-r+3;V=C-c+3
#       p=[[d]*V for _ in range(u)]
#       for v,x,y in o:
#        if v-f:p[x-r+1][y-c+1]=v
#       S={(I-1,J-1)for I in range(H+3-u)for J in range(W+3-V)if all(P[I+a][J+b]==p[a][b]for a in range(u)for b in range(V))}
#       if S:
#        I,J=next(iter(S));di,dj=I-r+1,J-c+1
#        for v,x,y in o:
#         x+=di;y+=dj
#         if 0<=x<H and 0<=y<W:B[x][y]=v
#  return B

