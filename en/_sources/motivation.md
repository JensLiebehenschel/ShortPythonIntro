# Motivation
(Click [here](https://jensliebehenschel.github.io/ShortPythonIntro/de/motivation.html) for the german version of this page)

## Why Python?
This should be an introduction into the programming language Python.
Python is a "general-purpose programming language", which due to its properties is quite suitable for the understanding of algorithms and data structures.

## Want more details? Then please continue reading!

## Why exactly Python?
Algorithms and data structures concern themselves with solving problems and organizing data.
The solution should be usable in software development, independent of a given programming language. Therefore "pseudocode" is often used to show the steps towards solving a problem or organization of data while being programming language-agnostic.

This features the disadvantage, that pseudocode cannot just be written and executed, leading to no output.

The advantage on the other hand, is that the translation from pseudocode to other programming languages is usually easier than translation from one programming language to another.
The major advantage is, that specifics of a given programming language are irrelevant for pseudocode.

The readers most likely have at least some understanding of the C programming language.
In C there is a concept of pointers. Though programming languages like Java or Python have no pointers, as they are abstracted away.
Would it be a good idea for a Java developer to concern themselves with the details of pointers just to understand how a sorting algorithm in a given C source code works? The answer for sure is: No.

Another example: Is it for an algorithm relevant whether integer values or floating point values are sorted?
For C code, absolutely. For the understanding of the sorting algorithm not so much.

## Python
Here is where Python comes in.
Python is the bridge between the advantages of pseudocode and the advantages of real source code.

In contrast to languages such as C, Python is a dynamically typed programming language. This means, that data types of variables do not have to be provided.
If one stores the value <code>5</code> in a variable, Python knows that it should be interpreted as an integer. Dividing said variable by half, Python will now interpret it as the floating point value <code>2.5</code>.
A variable in C, which is is declared and initialized with
```C
int x = 5;
```
would now result in this:
```C
printf("%d", x/2==2.5);
// --> 0 (False)
```
In this case, <code>5</code> divided by <code>2</code> would not result in <code>2.5</code>, since the integer data type does not store decimal places. In Python, this would not have been a problem.

Therefore it is very easy to create very complex structures in Python.
How about an array, which at one index contains another array with 5 further nested arrays. Meaning an array inside an array inside an array, and so on. Now the nested arrays could either be strings or integers. In C one would have to clearly define the structure and plan it out carefully, whereas in Python one can just add the values and leave it at that. Python will figure out which type is used. This structure can then even be changed at runtime.

Generally speaking, Python's intention is to sound as natural as possible. Therefore, Python is largely inspired from spoken English. Examples for where this is the case, will be shown in figure chapters.

## Python use cases?
Because of simplifications such as these, and many more as discussed later, Python is often referred to as "executable pseudocode". It is almost as convenient as writing pseudocode but is an entirely executable language. One disadvantage to other programming languages, such as C, is definitely the performance. For many computationally expensive tasks, Python is not quite as suitable. But for algorithms and data structures, the focus is on efficiency of the concepts, rather than creation of a high performance software product.

Python is wonderful to test an algorithm and make sure that it works. Afterwards, one can rewrite it in a faster programming language usch as C. In that case one would only have to concern themselves with translation instead of the actual inner workings of the algorithm. But then one would have to pay attention to programming language specifics again.
Nevertheless, Python is ideal for quickly building prototypes.

Python is a very popular programming language. Depending on the source of the statistic, Python is usually among the top 3 of the most popular programming languages in the world.

Furthermore, Python is the programming language for artificial intelligence and data science. Websites can also be programmed in Python with a web framework such as "Django".

The time invested to learn Python, should not be waste.
