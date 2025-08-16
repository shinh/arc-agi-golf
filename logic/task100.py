# pick most frequent nonzero
p=lambda g:[[max(range(1,10),key=sum(g,[]).count)]*2]*2#ignore0
