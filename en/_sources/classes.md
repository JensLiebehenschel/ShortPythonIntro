# Classes
(Click [here](https://jensliebehenschel.github.io/ShortPythonIntro/de/klassen.html) for the german version of this page)

Python is an object-oriented programming language, and therefore obviously has the concept of classes.

Inheritance and such will not be discussed here.
This introduction only tackles the syntax for class definitions and methods, since it is necessary if one wants to program e.g., binary trees.

To define a class, the keyword <code>class</code> followed by the name of the class. After that one can add empty round brackets and then finish the line with a colon.
```Python
class MyClass:
    <Class definition>
```
and
```Python
class MyClass():
    <Class definition>
```
lead to the same result. The round brackets are used to indicate inheritance.

After the colon, an indented code block follows. There, the actual functionality of the class is defined. A separation is made between class attributes and instance attributes.

## Attributes

Class attributes are shared among all objects of a class and can be accessed independently from a concrete instance.

```Python
class MyClass:
	class_id = 2 # Class attribute

print(MyClass.class_id)
# --> 2
```

Way more interesting are instance attributes. I.e., the attributes, which are individual to each instance of a class. Those are generally defined and initialized in the constructor method of the class, but can be defined in any method.

Attributes, just like regular variables have to initialized.

A declaration without initialization such as 
```C
int i;
```
is not possible in Python.

This is not that big of a deal, since one can just initialize a variable/attribute with a null value. In Python this is done with the keyword <code>None</code>.

A variable with the value <code>None</code> can later be assigned values of any type. Be it integers, strings or class instances. Dynamic typing is the reason for that.

## Methods and constructor
Methods, just like functions, are defined with the <code>def</code> keyword in the class block.
The constructor is just another method, which has to have a predefined method name.
In contrast to other programming languages, where the constructor usually has the same name as the class, the constructor in Python has to be called <code>&#95;&#95;init&#95;&#95;</code>. When an instance is created, the constructor is automatically executed. Of course, the constructor can also take parameters. These can also have default values. The same rules apply as with regular functions.

One important thing applying to the constructor and all other methods, is that every method has to take one mandatory parameter. The very first parameter to a function is the instance itself. This is done automatically when calling a method.

According to convention, this first parameter is referred to as <code>self</code>. One can name it differently if one really wants to. <code>self</code> serves the same function as the keyword <code>this</code> in most other object-oriented languages.
To modify the attributes of the actual instance, the instance has to be addressed with <code>self</code>, or however you decided to name it.
To access attributes or methods of an instance, the dot operator is used.

Example of a class with a constructor:
```Python
class MyClass:
	def __init__(self, a_input, b_input):
		self.a = a_input
		self.b = b_input
		self.c = None  # None is the Python equivalent to null

my_instance = MyClass(1,2)  # Constructor call with parameters
print(my_instance.a)
# --> 1
print(my_instance.b)
# --> 2
print(my_instance.c)
# --> None
```

An example with a constructor, a method and a local variable in said method:
```Python
class MyClass:
	def __init__(self, a_input, b_input):
		self.a = a_input
		self.b = b_input
		self.c = None
		d = 5 	# No "self." in the left side of assignment, therefore this is a local variable and not an attribute. This value only exists in the constructor.

	def calculate_c(self, factor_of_a):
		self.c = self.a * factor_of_a + self.b  # Formula: c = a * factor + b
		self.e = 8  # The attribute e can still be added outside of the constructor.


my_instance = MyClass(1,2)
print(my_instance.a)
# --> 1
print(my_instance.b)
# --> 2
print(my_instance.c)
# --> None

my_instance.calculate_c(3)
print(my_instance.c)
# --> 5

print(my_instance.e)
# --> 8

print(my_instance.d)
# --> AttributeError: 'MyClass' object has no attribute 'd'
# d is not an attribute of the class, instead it is just a local variable in the constructor.
```

Do not forget, that every instance attribute or method has to be prefixed with <code>self.</code> inside of a method, otherwise it will just be a local variable.
