# Arithmetic operators
(Click [here](https://jensliebehenschel.github.io/ShortPythonIntro/de/arithmetische-operatoren.html) for the German version of this page)

Python of course, offers basic arithmetic operators such as <code>+</code>, <code>-</code>, <code>*</code> and <code>/</code>.

```Python
x = 5+5
print(x)
# --> 10

x = 3*5
print(x)
# --> 15
```

A common shortcut in programming languages such as C or Java to increment a value, is the operator <code>++</code>.

```C
i++;
```
is the same as
```C 
i = i + 1;
```
In Python this is **not** possible.

This is not really that tragic, since incrementing a value is not done as often in Python as it is done in other programming languages. This can be seen when discussing loops later.

As an alternative, 
```Python
i += 1 
```
should be used for incrementing a value in Python, which is also equivalent to
```Python
i = i + 1
```

This works the same for subtraction, i.e., writing <code>x -= 1</code> instead of <code>x--</code>

More generally the operators <code>+=, &#045;=, \*=</code> and <code>/=</code> are used like this:

```Python
x OPERATOR= n

# is equivalent to

x = x OPERATOR n
```

Example:
```Python
x += 5

# is equivalent to

x = x + 5
```

There is also the relatively common modulo operator using the percentage sign (<code>%</code>).
Reminder:
The result of <code>a % b</code> (a modulo b i.e., a mod b) is the division remained of the division <code>a/b</code>.
```Python
x = 8 % 3
print(x)
# --> 2
```

Furthermore, there is the operator <code>//</code> for integer division.
This operation calculates the regular quotient <code>c = a/b</code>, but <code>c</code> will be rounded down to the next-lowest integer, if <code>c</code> is not an integer already. The remainder will be omitted.

One can also rewrite
```Python
a // b 
```
to
```Python
math.floor(a/b)
```
where the rounding down is done explicitly.
Example:
```Python
x = 5 // 2
print(x)
# --> 2

import math
x = math.floor(5/2)
print(x)
# --> 2
```

<code>math.floor()</code> is a function of the math library in Python, which takes a value as input and rounds it down the next-lowest integer if it is not an integer already. The usage of library functions will be discussed in a later chapter.

Last but not least, there is the power operator <code>\*\*</code>, which is used to represent exponentiation.

For example, <code>2 \*\* 5</code> would evaluate to 2<sup>5</sup> (2 to the power of 5).
```Python
x = 3 ** 3
print(x)
# --> 27
```

For the last three operators, there are also the operators <code>%=</code>, <code>//=</code> and <code>\*\*=</code>.
```Python
x = 5
x //= 5
```
is equivalent to:
```Python
x = 5
x = x // 5
```

## Mathematical operators in a non-mathematical context
Depending on the context, arithmetic operators can also have a different meaning.
The addition operator for two numbers represents an addition, but what about the addition operator for two strings?

An arithmetic sum of two strings is most often not desired, therefore the addition operator has a different meaning for objects, which are not numbers.

For example, with the two strings, the following functionality can be observed:
```Python
a = "Hello"
b = "World!"

print(a + b)
# --> "HelloWorld!"
```

A concatenation has taken place. The second string was appended to the first string. To format it slightly better, one can add a whitespace between the two strings with the same method:
```Python
a = "Hello"
b = "World!"

print(a + " " + b)
# --> "Hello World!"
```

Outside of numeric calculations, the addition operator often indicates concatenation. But depending on context, it may mean something different. One is advised to read up on the specific functionality for a given context.
