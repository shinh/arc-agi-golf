# 2x2 2s -> cross
p=lambda g:(k:=sum(sum(g,[]))>>3,((k>0,0,k>1),(0,k>2,0),(k>3,0,k>4)))[1]
