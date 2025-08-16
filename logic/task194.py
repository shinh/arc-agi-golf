p=lambda g:(t:=[a+[*b]for a,b in zip(g,zip(*g[::-1]))])+[i[::-1]for i in t[::-1]]# rotate and tile
