# Assignments in Python
(Click [here](https://jensliebehenschel.github.io/ShortPythonIntro/de/zuweisungen.html) for the german version of this page)

## The assignment operator

As we have already seen, Python also uses <code>&equals;</code> as the normal assignment operator, just like most other programming languages. The basic function of said operator need no further introduction.

But in Python it has additional functionality.
Normally the assignment operator has one operand on the left side and one operand on the right side,
i.e.,
```Python
a = b
```

But Python does not have this restriction. Simply put, there just have to be the same amount of operands on both sides. Therefore, is is possibly to perform multiple assignments in one operation. The operands on each side are separated by commas.

Example:
```Python
# a should get the value 5 and b should get the value 10
a,b = 5,10
```
Or expressed more generally:
```Python
variable1, variable2, ... = value_for_variable1, value_for_variable2, ...
```

If both sides do not have equal length, it will not work, just like in this example:
```Python
a,b = 10
a,b = 5,10,15
# --> ValueError: too many values to unpack (expected 2)
```
If one wants to assign the same value to multiple variables, it should be done like this:
```Python
a,b = 10,10
```

# Exercise
Operands on the right side can be literal values or variables.

What do you think would happen if one were to do this:
```Python
a = 5
b = 10

a,b = b,a

# What value will a have?
# What value will b have?
# Is this an illegal operation, 
# which results in an error?
```

:::{admonition} Solution
:class: dropdown

Solution: a will be 10, b will be 5

A swap of the two variables was performed.

One can imagine it as a shortcut for:

```Python
temp = a
a = b
b = temp

# Swapping of three or more variables is also possible.
# But swapping two variables is the more common use case.
```

More generally:
First all operands on the right side are evaluated, and only then are they assigned to the left side.

:::