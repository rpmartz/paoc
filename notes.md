## Questions

* 2015.07: Why does `& 0xffff` turn a regular Python `int` into a 16-bit integer?
* Understand `itertools.groupby` better
* 2015.11: does `any` or `all` short circuit if `True` or `False` is found, respectively?

## ToDos

* Implement efficient algorithm for finding permutations 

## Lookups

* `itertools.cominations` vs. `itertools.permutations`. Differences and a basic way to find each

## Learnings

* `O(n!)` grows really fast. Assuming 1 million permutations per second, generating permutations for a set of 10 items can be done in a few seconds. 15 items takes 15 days. 17 items would take 11 years.  