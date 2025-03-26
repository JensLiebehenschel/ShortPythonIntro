# Input and output
(Click [here](https://jensliebehenschel.github.io/ShortPythonIntro/de/input-und-output.html) for the German version of this page)

## Output
Just like with other programming languages, the input and output using a terminal are essential. At least regarding programs in the context of simple scripts.

To print something to the terminal in Python, one can use the function <code>print()</code>.
```py
name = "Joe Generic"
print(name)
# --> "Joe Generic"
```
The <code>print()</code> function can also take multiple parameters. In this case, the provided parameters are concatenated with a whitespace between them.
```py
name1 = "Joe Generic"
name2 = "John Doe"
print(name1, "is friends with", name2)
# --> "Joe Generic is friends with John Doe"
```
After a call to the <code>print()</code> function, a line break is automatically created.
The following lines:
```py
print(1)
print(2)
print(3)
```
result in the following output:
```py
1
2
3
```
instead of
```py
123
```

## Input

How users can provide input to a Python program through the terminal will not be discussed in this introduction.

If one wants to test the function <code>foo(x)</code>, then one can for the time being just hard-code a given value for <code>x</code>.
```py
x = 5
foo(x)

# or just

foo(x)
```

For those, who are interested, here is the <a href="https://docs.python.org/3/library/functions.html" target="_blank">Python Referenz</a>, with information regarding built-in Python functions such as <code>input()</code>.

Alternatively, you can just search for it on the web with a search engine of your choice.
