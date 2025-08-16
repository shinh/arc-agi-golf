def p(g):
        i=sum(g,[]).index;w=len(g[0]);C,A=divmod(i(8),w);B,D=divmod(i(2),w)
        # connect 8 to 2 with a 4 path
        while C-B:C+=B>C or-1;g[C][A]=4
        while A-D:g[B][A]=4;A+=D>A or-1
        return g