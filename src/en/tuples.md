# Tuples

A tuple is Python is a data structure, which can store a sequence of elements.
Therefore, the functionality is almost identical to lists.

## Syntax
The syntax for tuples is very similar to lists. The only difference is, that round brackets are used instead of square brackets. Otherwise, creation is identical
```py
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
```

The only difference is noticable for tuples with exactly one element. Empty tuples are not really a good idea, as you will soon see, but the syntax is just an opening round bracket and a closing round bracket.
```py
empty = ()
```

Tuples with exactly one element are slightly more special, since they require a comma after the element. One can imagine the reason when thinking about calculation. Round brackets around a number should have no effect on the calculation. But if one would interpret a number encased in round brackets as a tuple, then it would lead to problems, since it would now considered a tuple instead of a number.
```py
print( (5) )
# --> Number 5

print( (5,) )
# --> Tuple containing the number 5

print( 1 + (5) )
# --> Number 6
# Should be 6 instead of "1 + tuple containing the number 5"
```

## Lists vs. tuples
There is only one fundamental difference between lists and tuples. Lists are mutable while tuples are immutable. This means, that after creating a list, it can still be modified later. For example, one can add the value <code>4</code> to the end of the list using <code>my_list.append(4)</code>.
```py
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
# --> [1, 2, 3, 4]
```

This is not possible with tuples. As soon as a tuple object was created, it cannot be modified anymore.
```py
my_tuple = (1, 2, 3)
my_tuple.append(4)
print(my_tuple)
# --> AttributeError: 'my_tuple' object has no attribute 'append'

my_tuple[0] = 0
# --> TypeError: 'my_tuple' object does not support item assignment
```

If one wants to modify a tuple, a new tuple object has to be created. This can be done using the <code>+</code> operator for example, which can be used to concatenate two tuples and store the result in a newly created tuple.
```py
my_tuple = (1, 2, 3)

new_tuple = my_tuple + (4,)
print(new_tuple)
# --> (1, 2, 3, 4)
```

if one wants to convert for example a list to a tuple, this can be done using the <code>tuple()</code> function to cast it to a tuple.

```py
my_list = [1, 2, 3]

my_tuple = tuple(my_list)
print(type(my_tuple))
# --> <class 'tuple'>
```

One possible reason for doing this would be for example be to use the tuple as a key of a ditionary. Since tuples are immutable, they can be used as keys for dicitonaries, while listes are not immutable and therefore cannot.

```py
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

{my_list: True}
# --> TypeError: unhashable type: 'list'

{my_tuple: True}
# --> {(1, 2, 3): True}
```

## Where else can you find tuples?
In Python it is possible to have multiple return values for a function. Interesting to know, is that this is implemented by returning a tuple.
```py
def example():
    return 1, True, "Ok"

result = example()
print(type(result))
# --> <class 'tuple'>

my_tuple = (1, True, "Ok")
is_the_same_as_the_tuple = result == my_tuple
print(is_the_same_as_the_tuple)
# --> True
```