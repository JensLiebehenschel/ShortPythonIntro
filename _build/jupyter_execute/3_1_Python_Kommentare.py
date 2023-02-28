#!/usr/bin/env python
# coding: utf-8

# # Kommentare in Python

# Kommentare in Python sind relativ simpel. Es gibt nur einen Weg Kommentare zu erstellen.
# Wenn außerhalb eines Strings ein Rautezeichen(#) vorkommt, so wird alles was in dieser Zeile rechts vom Rautezeichen steht, als Kommentar gewertet

# In[1]:


x = 5 # Gib x den Wert 5
#	   ^^^^^^^^^^^^^^^^^
#Code  Kommentar


# Es gibt eigentlich keinen Weg, einen Kommentar über mehrere Zeilen hinweg zu machen
# wie in C/C++/Java mit
# /*
# 	Das ist kommentar
# 	Das hier auch
# 	Das hier ebenfalls
# */
# 
# Somit muss man in Python jede Zeile einzeln auskommentieren.

# In[2]:


#	Das ist ein kommentar
#	Das hier auch
#	Das hier ebenfalls


# Um das Leben einfacher zu machen, ist es jedoch trotzdessen möglich etwas ähnliches zu erzielen indem man den auszukommentierenden Inhalt als einen String ohne Zuweisung speichert. Somit fällt der betroffene Code weg.
# Das Funktioniert indem man jeweils am Anfang und Ende des auszukommentierenden Bereichs sogenannte "triple quotes" einfügt. Damit bezeichnet man drei aufeinanderfolgende Anführungszeichen.

# Jetzt sind Sie an der Reihe!
# Sorgen sie **OHNE** Code zu entfernen oder zu verschieben dafür, dass der Output "Hello World!" geprinted wird.
# Sie dürfen nur zwei triple quotes (""") nutzen

# In[3]:


my_output = "Hello World!"


my_output = 0
for i in range(1, 100+1):
    my_output += i


print(my_output)


# ## Solution

# ```Python
# my_output = "Hello World!"
# 
# # Dieser Code geht über mehrere Zeilen und soll "auskommentiert" werden
# 
# """
# my_output = 0
# for i in range(1, 100+1):
#     sum += i
# """
# 
# print(my_output)
# ```
