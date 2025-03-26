# How do we use Python?
(Click [here](https://jensliebehenschel.github.io/ShortPythonIntro/de/wie-nutzen-wir-python.html) for the German version of this page)

## Not very "pythonic"

One description of the python programs in this introduction could be "not very pythonic". This means that these programs are not written in a way, which takes full advantage of Python's strengths. This is necessary to tackle the underlying concepts instead of relying on the luxuries provided by Python.

To make it clear with an example:
In Python the standard library has a function <code>sort()</code>. Said function can automatically sort a provided list. In algorithms and data structures, the functionality and design of many sorting algorithms is shown. Therefore we cannot use the <code>sort()</code> function in this introduction.

Theoretically, we could replace every sorting algorithm with
```py
your_list.sort()
```
and have the same effect. The goal here is to understand more how functions like <code>sort()</code> work. How you can create one yourself, what the underlying concepts are and how a given algorithm can be analyzed (e.g., regarding time complexity).

Sorting is not the only aspect where the standard library already provides better solutions. For instance, "hashing" is provided in Python using so-called "Dictionaries".

## Python developers work differently than what is desired for learning

Since the <code>sort()</code> function in the Python standard library is also written in C++, not Python, it is faster than anything you can regularly program in Python. So, it is not only more convenient, but also more performant. Therefore, one would typically never write your own sorting algorithm in Python and instead rely on functions such as <code>sort()</code>.

The same applies for other areas such as finding the largest element in a list. The python function <code>max()</code> will be faster than anything you could write in Python.

But the goal of using Python for understanding algorithms and data structures is to understand the individual algorithms, not how to develop an efficient Python program.

Therefore: "Not very pythonic"!
