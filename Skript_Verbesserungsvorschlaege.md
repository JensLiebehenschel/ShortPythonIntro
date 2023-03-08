# Skript Vorschläge

## Skript Seite 19 (PDF Seite 21):
Der aktuelle Link "http://www.codinghorror.com/blog/2007/02/why-cant-programmers-program.html" ist outdated (unerreichbar).
Der korrekte Link ist "https://blog.codinghorror.com/why-cant-programmers-program/".


## Skript Seite 182 (PDF Seite 184):
###	Aktueller Code:
```Python
INF = sys.maxsize  # TODO should do better
```
###	Vorschlag:
```Python
INF = float('inf')  
# Hat das gleiche Ergebnis, ist aber leserlicher und ich nehme an verständlicher.
# Zusätzlich braucht man nicht die sys library zu importieren.
```

## Gleicher Vorschlag wie davor: Skript Seite 202 (PDF Seite 204), auch in "kpriorityqueue.py":

###	Aktueller Code:
```Python
def adjust(a):
# add s_0 and s_n+1, 999999999 representing infinity
return [[0,0]] + a + [[len(a), 999999999]]
```
###	Vorschlag (Ich habe es getestet und das Programm funktioniert weiterhin):
```Python
def adjust(a):
# add s_0 and s_n+1, float('inf') acts as infinity
return [[0,0]] + a + [[len(a), float('inf')]]
```
