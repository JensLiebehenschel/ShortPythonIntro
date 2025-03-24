# Data Types

## Dynamic typing
(Click [here](https://jensliebehenschel.github.io/ShortPythonIntro/de/datentypen.html) for the german version of this page)

Python has most data types of other known programming languages, be it integers, floating points values or strings.
The difference is, that in Python one does not typically have to concern themselves with the data type.
The reason for that is Python's concept of "dynamic typing".
Here is an explanation:
Simply put, with dynamic typing, the Python interpreter concerns himself with data types. The developer does not have to statically assign data types to variables, functions and so on.

This makes it very easy to work with Python, since the author has to write less code and need not concern themselves whether e.g., a single variable will always be of one consistent data type. For example, whether a variable will always stay an integer or if there were an option, where the result may become a floating points number.
Nevertheless, if one want a variable in a specific data type, then one can perform a type cast and explictly convert a value to a given type. This type can still change after the cast, if a new value is assigned.

```Python
# The function type(x) returns the datatype of the variable x. 

x = 5
print(type(x))
# --> <class 'int'>
# x is an integer

x = str(x)  # Type casting the integer to a string
print(type(x))
# --> <class 'str'>
# x is now a string
```

## Every variable has to be initialized

In programming languages such as C, there is a difference between declaration and initialization of a variable.

A declaration does not assign a value, it just specifies a data type and name for the variable.
```C
int i;
```
One can also perform declaration and initialization at the same time:
```C
int i = 5;
```
In Python it is not possible to declare a variable without also initializing it.
Some thing like
```C
int i;
```
is not possible in Python.
But there are cases, where one wants to declare a varaible without initializing it directly. For this, the variable can be initialized with a null value. In Python this is done with the keyword <code>None</code>.
After that, the variable can later be assigned a value of any type, when one wants to.
```Python
value = None
print(value)
# --> None

value = 5
print(value)
# --> 5

value = "Hello World!"
print(value)
# --> "Hello World!"
```

## Note regarding semicolons

The attentive reader may have noticed, that none of the statements in the Python code end with a semicolon. This is not an error. Semicolons are not needed to end a statment. The only usage of semicolons is to have multiple statements in the same line.
Example:
```Python
x = 5; print(x)
# --> 5
```

## Note regarding strings
In Python, strings can have two different delimiters. Either double quotes or single quotes. They can also be mixed withing the same program, but they are not allowed to be mixed in the same string.

Valid:
```Python
"Text"
'Text'
```

Invalid:
```Python
"Text'
'Text"
```
