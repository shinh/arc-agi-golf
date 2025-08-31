# connect same dots

# def p(g,n=0):
#     for f in[int,abs]:
#         g=[[f([n:=[n,-v*(v in r[x+1:])][0<v!=g[0][2]],v][v!=0])for x,v in enumerate(r)]for r in zip(*g)]
#     return g

p=lambda g,t=1,f=int,n=0:-t*g or p([[f([n:=[n,-v*(v in r[x+1:])][0<v!=g[0][2]],v][v!=0])for x,v in enumerate(r)]for r in zip(*g)],t-1,abs)
