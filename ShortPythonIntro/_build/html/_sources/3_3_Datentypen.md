# Datentypen

## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**


## Dynamic Typing

Python hat alle gängigen Datentypen die man aus anderen Programmiersprachen kennt. Seien es Integer, Gleitkommazahlen oder Strings.
Der Unterschied in Python ist, dass sich der Programmierer in der Regel nicht um Datentypen kümmern muss.
Der Grund dafür liegt in Pythons "Dynamic Typing"
Hier nochmal die Erklärung.
Beim Dynamic Typing, kümmert sich einfach gesagt, der Python Interpreter um Datentypen und der Programmierer muss diese nicht konkret angeben.

Dies macht es sehr einfach mit Python zu arbeiten, da man weniger tippen muss und sich nicht überlegen zu braucht, ob etwa eine bestimmte Variable immer ein Integer bleibt, oder ob es nicht doch ein Szenario gibt, in welchem daraus eine Gleitkommazahl werden könnte.
Wenn man eine Zahl jedoch in einem bestimmten Datentyp haben will, so kann man Typecasting machen und somit den Typen explizit angeben. Dieser kann sich dann aber trotzdem noch ändern, wenn man der Variable einen neuen Wert zuweist.

```Python
# Bei der Funktion type(x) handelt es es sich um eine Funktion, 
# welche angibt von welchem Datentypen das Objekt x ist 

x = 5
print(type(x))
# <class 'int'>
# --> x ist intern ein Integer

x = str(x)  # Typecasting von der Variable x zum Datentyp String
print(type(x))
# <class 'str'>
# --> x ist nun intern ein String
```

## Jede Variable muss initialisiert sein

In Programmiersprachen wie C, unterscheidet man zwischen Deklaration und Initialisation einer Variable.

Bei einer Deklaration wird kein Wert zugewiesen, sondern nur Datentyp und Name angegeben:
```C
int i;
```
Bei einer Initialisation, wird einer bereits deklarierten Variable, ein Wert zugewiesen:
```C
i = 5;
```
Man kann beides auch gleichzeitig machen mit:
```C
int i = 5;
```
In Python kann man keine Variable deklarieren ohne sie auch zu intialisieren.
Der Fall 
```C
int i;
```
ist also in Python nicht möglich.
Es gibt jedoch Fälle, wo man deklarieren aber nicht sofort initialisieren möchte.
Dafür kann ein Nullwert genutzt werden, damit die Variable initialisiert ist. In Python ist dies mit dem Keyword <code>None</code> möglich. 
Anschließend kann man der Variable später einen Wert zuweisen, sobald es soweit ist.
```Python
value = None
print(value)
# None

value = 5
print(value)
# 5

value = "Hello World!"
print(value)
# Hello World!
```

## Hinweis zu Semikola

Wie vom aufmerksamen Leser bereits bemerkt, hat keine dieser Anweisungen ein Semikolon am Ende. Dies ist kein Fehler.
Semikolons werden am Ende einer Zeile nicht benötigt.
Der einzige Nutzen von Semikolons ist das ausführen von mehreren Anweisungen in der selben Zeile.\
Beispiel:

```Python
x = 5; print(x)
```

## Hinweis zu Strings

In Python können Strings entweder mit normalen Anführungszeichen oder mit einfachen Anführungszeichen angegeben werden.
Man kann auch innerhalb eines Programms beides benutzen, jedoch kann man nicht beides innerhalb von einem String benutzen.

Gültig:
```Python
"Text"
'Text'
```

Ungültig:
```Python
"Text'
'Text"
```