#bbox
def p(g):
 s=str(sum(g,[]))[1::3];w=len(g[0])
 return[[int(max(s,key=lambda c:(c>'0')*-~((l:=s.rfind(c)-s.find(c))%w)*-~(l//w)))]*2]*2

