Höhe = input("Bitte geben Sie eine Zahl für die Höhe an: ")
Breite = input("Bitte geben Sie mir eine Zahl für die Breite an: ")
Zeichen = input("Bitte geben Sie mir ein Zeichen: ")
 
Höhe = int(Höhe)
Breite = int(Breite)
 
print((Zeichen * Breite + "\n") * Höhe)
 
print("Anzahl:", (Breite * Höhe))
