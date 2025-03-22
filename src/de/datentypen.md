# Datentypen

## Dynamic Typing

Python besitzt alle aus anderen Programmiersprachen bekannten Datentypen. Seien es Integer, Gleitkommazahlen oder Strings.
Der Unterschied in Python ist, dass man sich in der Regel nicht um Datentypen kümmern muss.
Der Grund dafür liegt in Pythons "Dynamic Typing".
Hier nochmal die Erklärung:
Beim Dynamic Typing kümmert sich - einfach gesagt - der Python Interpreter um Datentypen, eine Angaben ist nicht notwendig.

Dies macht es sehr einfach, mit Python zu arbeiten, da man weniger tippen muss und sich nicht überlegen zu braucht, ob etwa eine bestimmte Variable immer ein Integer bleibt, oder ob es nicht doch ein Szenario gibt, in welchem daraus eine Gleitkommazahl werden könnte.
Wenn man eine Zahl jedoch in einem bestimmten Datentyp haben möchte, dann kann man Typecasting machen und somit den Typen explizit angeben. Dieser kann sich dann aber trotzdem noch ändern, wenn der Variable ein neuer Wert zugewiesen wird.

```Python
# Bei der Funktion type(x) handelt es es sich um eine Funktion, 
# welche zurückgibt, welchen Datentypen das Objekt x hat. 

x = 5
print(type(x))
# --> <class 'int'>
# x ist intern ein Integer

x = str(x)  # Typecasting von der Variable x zum Datentyp String
print(type(x))
# --> <class 'str'>
# x ist nun ein String
```

## Jede Variable muss initialisiert sein

In Programmiersprachen wie C, unterscheidet man zwischen Deklaration und Initialisierung einer Variable.

Bei einer Deklaration wird kein Wert zugewiesen, sondern nur Datentyp und Name angegeben:
```C
int i;
```
Bei einer Initialisierung wird einer bereits deklarierten Variable ein Wert zugewiesen:
```C
i = 5;
```
Man kann beides auch gleichzeitig machen mit:
```C
int i = 5;
```
In Python kann man keine Variable deklarieren ohne sie auch zu intialisieren.
Ein Fall wie
```C
int i;
```
ist also in Python nicht möglich.
Es gibt jedoch Fälle, in denen man eine Variable deklarieren aber nicht sofort initialisieren möchte.
Dafür kann ein Nullwert genutzt werden, damit die Variable initialisiert ist. In Python ist dies mit dem Keyword <code>None</code> möglich. 
Anschließend kann man der Variable später einen Wert zuweisen, sobald es soweit ist.
```Python
wert = None
print(wert)
# --> None

wert = 5
print(wert)
# --> 5

wert = "Hello World!"
print(wert)
# --> "Hello World!"
```

## Hinweis zu Semikola

Wie von aufmerksamen Lesenden bereits bemerkt, besitzt keine dieser Anweisungen ein Semikolon am Ende. Dies ist kein Fehler.
Semikolons werden am Ende einer Zeile nicht benötigt.
Der einzige Nutzen von Semikolons ist das Schreiben von mehreren Anweisungen in der selben Zeile.

Beispiel:

```Python
x = 5; print(x)
# --> 5
```

## Hinweis zu Strings

In Python können Strings entweder mit einfachen Anführungszeichen oder doppelten Anführungszeichen angegeben werden.
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