#!/usr/bin/env python
# coding: utf-8

# # Weitere Aufgaben

# ## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**

# # FizzBuzz

# Eine sehr beliebte Aufgabe für Einsteiger einer Programmiersprache, ist das FizzBuzz Problem.
# 
# Das Problem sieht wie folgt aus:
# 
# - Es sollen die Zahlen 1 bis inklusive 100 untereinander ausgegeben werden.
# 
# - Hierbei sollen jedoch Zahlen, welche durch 3 teilbar sind, durch den String <code>"Fizz"</code> ersetzt werden.
# 
# - Zahlen, welche durch 5 teilbar sind, sollen durch den String <code>"Buzz"</code> ersetzt werden.
# 
# - Wenn eine Zahl durch 3 als auch durch 5 teilbar ist, soll die Zahl durch den String <code>"FizzBuzz"</code> ersetzt werden
# 
# 
# Der Output soll so aussehen:

# ```
# Output    Zahl
# 
# 1         1
# 2         2
# Fizz      3
# 4         4
# Buzz      5
# Fizz      6
# 7         7
# 8         8
# Fizz      9
# Buzz      10
# 11        11
# Fizz      12
# 13        13
# 14        14
# FizzBuzz  15
# 16        16
# ...       ...
# 98        98
# Fizz      99
# Buzz      100
# ```
# 
# Die Zahlen rechts sind nur zur Veranschaulichung da. Sie müssen diese nicht ausgeben lassen!

# ## Ihre Antwort

# In[1]:


# Hier können Sie das FizzBuzz Problem lösen


# :::{admonition} Show FizzBuzz solution
# :class: dropdown
# 
# ```Python
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
# ```
# 
# Erklärung der obigen Lösung: 
# 
# <code>range(1, 101)</code>, da es bei <code>1</code> starten soll und bis inklusive <code>100</code> gehen soll. (Inklusive <code>100</code> --> Exklusive <code>101</code> --> <code>range(1, 101)</code>)
# 
# Zahl ist durch <code>n</code> teilbar --> <code>zahl % n == 0</code>.
# 
# Sprich: Es gibt keinen Rest bei der Division <code>zahl / n</code>.
# 
# Es gibt viele Lösungen für diese bekannte Programmieraufgabe. Man könnte etwa mit Strings arbeiten und bei bedarf Fizz und Buzz konkatenieren.
# Alternativ könnte man auch mit Lambdas arbeiten, das ist hier definitiv aber nicht von Relevanz
# 
# :::
