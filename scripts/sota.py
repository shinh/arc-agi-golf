def read_sota():
    theirs = []
    # Update this file by
    # https://docs.google.com/spreadsheets/d/e/2PACX-1vQ7RUqwrtwRD2EJbgMRrccAHkwUQZgFe2fsROCR1WV5LA1naxL0pU2grjQpcWC2HU3chdGwIOUpeuoK/pubhtml#gid=1427788625
    for line in open("scripts/sota.txt").readlines()[1:]:
        if not line:
            continue
        toks = line.split()
        assert len(toks) > 2, line
        theirs.append(int(toks[1]))
    assert len(theirs) == 400
    return theirs
