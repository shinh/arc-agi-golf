# move patterns from one half onto the other
def p(g):
    #print(f"{len(g)=} {len(g[0])=}")
    #show(g,"input")
    f=sum(g,[])
    sc=sorted({*f},key=f.count)
    fg=sc[:-2]
    #print(f'kkk {s=} {fg=} {bg=}')

    g,o=[[[r[:len(g[0])//2]for r in g],[r[len(g[0])//2:]for r in g]],[g[:len(g)//2],g[len(g)//2:]]][len(g)>len(g[0])]

    if(bg:=sc[-1])in g[0]:g,o=o,g

    #show(g,"from")
    #show(o,"to")

    s=[]
    blocks=[]
    for sy in range(len(g)):
        for sx in range(len(g[0])):
            if(sy,sx)not in s:
                ly=lx=0
                while(g+[[0]*99])[sy+ly+1][sx]in fg:ly+=1
                while(g[sy]+[0])[sx+lx+1]in fg:lx+=1

                if ly*lx:
                    #print(f'found block {sy=} {sx=} {ey=} {ex=} {ly=} {lx=} {pc=} {bc=}')
                    for dy in range(ly):
                        for dx in range(lx):
                            s+=(sy+dy,sx+dx),
                    blocks+=(ly+1,lx+1,sy,sx),

    for ly,lx,sy,sx in sorted(blocks)[::-1]:
        pc=[*{g[sy+dy][sx+dx]for dy in range(ly)for dx in range(lx)}-{sc[-3]}][0]

        for ty in range(len(g)-ly+1):
            for tx in range(len(g[0])-lx+1):
                ok=1

                for dy in range(-1,ly+1):
                    for dx in range(-1,lx+1):
                        if o[ty+dy][tx+dx]!=[bg,pc][g[sy+dy][sx+dx]==pc]if ly>dy>-1<dx<lx else((o+[[0]*99])[ty+dy]+[0])[tx+dx]==pc:
                            ok=0

                if ok:
                    #print(f'found dest! {ty=} {tx=}')
                    for dy in range(ly):
                        for dx in range(lx):
                            o[ty+dy][tx+dx]=g[sy+dy][sx+dx]
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

