# Interesting Numbers

Interesting Numbers is a python package for finding 'interesting' numbers, and representations of numbers. Install with 

```bash
pip install -i https://test.pypi.org/simple/ interesting-numbers==0.1.3
```

If you want to find ways to write a number as a word in a different base, use `find_words`:

```python
from interesting_numbers.find_words import find_words
find_words(11618)
```

If you want to find the next 'interesting' number, create a `NumberFinder` object configured with functions from `interests` which it should check for:

```python
from interesting_numbers.number_finder import NumberFinder
from interesting_numbers.interests import is_square, is_cube, is_triangular, is_fibonacci, is_power_of_two, is_repdigit, is_consecutive, is_palindrome
#The first list passed to NumberFinder is the functions which are base-independent. The second list is the functions which are base-dependent.
#This is a selection of some criteria which might be interesting
finder = NumberFinder([is_square, is_cube, is_triangular, is_fibonacci, is_power_of_two], [is_repdigit, is_consecutive, is_palindrome])
finder.findnext(11628)
```
