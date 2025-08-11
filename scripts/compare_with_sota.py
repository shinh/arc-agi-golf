#!/usr/bin/env python3

import glob
import os

ours = []
for py in sorted(glob.glob("submissions/*.py")):
    ours.append(os.path.getsize(py))

assert len(ours) == 400, str(len(ours))

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

for i in range(400):
    o = ours[i]
    t = theirs[i]
    prefix = f"Task{i+1:03d}"
    if o < t:
        print(prefix, f"We win! {o} vs {t}")
    elif o == t:
        print(prefix, f"Tie. {o}")
    else:
        print(prefix, f"{o-t} bytes from theirs: {o} vs {t}")
