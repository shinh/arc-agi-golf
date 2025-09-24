p=lambda g:sum(([sum((n*[x]for x in r),[])]*n for n in{len({*sum(g,[])})-1}for r in g),[])#scale grid by number of colors
