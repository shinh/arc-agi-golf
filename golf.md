Since zlib compression is applied, be aware that removing repetitions can have the opposite effect. Focus on fundamentally improving the logic rather than on small syntax hacks.

```
$ python3 submit.py <task_id> | tail -n 1
```

is the post-compression score (larger is better). I want to know whether this score has increased, so please include the number before and after the change in your report.

Common techniques:

* [:] can often be deleted if don't really need a copy
* enumerate(g) -> can be replaced by g and increment the index manually
* put constant assignments in function definition, doesn't need to be indented there
* inline assignments that are only used once (unless a side effect makes order of evaluation important)
* use := if it can allow the entire thing to become a lambda instead of def
* look for values that are created twice and avoid duplication (e.g. range, range(16), enumerate)
* For tasks that need to check in four directions, instead of writing similar code four times, loop over range(4) and inside do g=[*map(list,zip(*g[::-1]))] to rotate 90 degrees.
* Using max(..., key=) to get the most frequent color can sometimes be replaced with simply 0, g[0][0], or max(g[0]) depending on the task.
* Comments will be automatically removed, so please write them.
* Add anything else here if it seems useful.
