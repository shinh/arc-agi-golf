#connect same dots
#def p(g,n=0):
#    for f in[int,abs]:
#        g=[[f([n:=[n,-v*(v in r[x+1:])][0<v!=g[0][2]],v][v!=0])for x,v in enumerate(r)]for r in zip(*g)]
#    return g

p=lambda g,n=0:[(g:=[[f([n:=[n,-v*(v in r[x+1:])][0<v!=g[0][2]],v][v!=0])for x,v in enumerate(r)]for r in zip(*g)])for f in(int,abs)][-1]
