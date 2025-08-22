# left if halves equal else top half
p=lambda g:(g[:len(g)//2],l:=[r[:len(r)//2]for r in g])[g==[r*2 for r in l]]
