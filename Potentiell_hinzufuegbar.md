Themen aus Skript/ Python codes, welche in Python Intro nicht vorkommen - kurzversion

# Weitere Aspekte, welche im Skript/ in Python codes vorkommen, man kann diskutieren ob diese behandelt werden sollen oder nicht

### STRING.split()
	kommt vor in:
		- Listing 1.2 (Einführungsbeispiel mit Word Count)


### List comprehension
	kommt vor in:
		- Listing 5.3 (Quicksort Alternative mit List Comprehension),
		- Etwas ähnliches zu List comprehension kommt in kmp.py vor


# Dateien, welche ich für zu komplex für das Python Intro halte (Diese verstehen zu helfen ist ganz sicher nicht die Aufgabe von Python Intro). Die notwendigen Erklärungen für Aspekte, welche sich auf diese Dateien beschränken, werden nicht beachtet.

- markov.py
- Listing 9.7 (Sudoku) bzw. sudo.py



# Aspekte, welche im Skript/ in Python codes vorkommen, ich aber persönlich als irrelevant oder als zu fortgeschritten für das Python Intro einschätze

### Von Dateien lesen (allgemein)
	kommt vor in:
		- Listing 1.2 (Einführungsbeispiel mit Word Count),


### Exceptions (raise Exception("Exception Nachricht"))
	kommt vor in:
		- Listing 6.4 (Min Priority Queue),
		- Listing 7.7 (Dijkstra)


### printf()-artiges Printen z.B.: print("%s%s" %("A","B"))
	kommt vor in:
		- Listing 7.1 (TREE-SEARCH Version 1),
		- Listing 7.7 (Dijkstra)
		- recursion.py
		- redblacktree.py


### Erstellen von 2D Listen mithilfe von List comprehension
	Bsp.: c = [[0 for j in range(n)] for i in range(m)]
	kommt vor in:
		- Listing 8.1 (LCS-LENGTH),
		- Listing 12.1 (Page Rank)


### if \_\_name\_\_ == "\_\_main\_\_":
	kommt vor in:
		- Listing 12.1 (Page Rank)


### Lambdas
	kommt vor in:
		- growth.py
		- lcs.py


### STRING.replace()
	kommt vor in:
		- growth.py
		- lcs.py


### STRING.join(seperator_character)
	kommt vor in:
		- growth.py
		- lcs.py



# Aspekte, welche im Skript/ in Python codes vorkommen und welche ich schonmal in Python Intro hinzugefügt habe. Bei Bedarf kann ich diese auch wieder entfernen, falls sie nicht relevant genug sein sollten.

### Absteigende For-Schleifen 
	--> for i in range(10, 2, -1) 
	alternativ: for i in reversed(range(3, 11))
	kommt vor in:
		- Listing 5.12 (Heapsort)


### Default Werte für Funktionen als auch Konstruktor
	kommt vor in:
		- Listing 7.1 (TREE-SEARCH Version 1)


### LIST.reverse() um eine List umzukehren
	kommt vor in:
		- Listing 7.7 (Dijkstra)


### Shortcut um z.B. eine List bestehend aus 10 nullen zu erstellen
	--> nums = [0] * 10
	kommt vor in:
		- hash.py 


### Konkatenieren von Listen mit dem "+" Operator
	kommt vor in:
		Listing 5.1 (Merge Sort)