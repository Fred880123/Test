# Kopfgesteuerte Schleife

def berechneLaufzeit():

    zinsen = 0.0
    # Eingabe
    startkapital = float(input( " Startkapital:"))
    zielkapital = float(input( " Zielkapital:"))
    zinssatz = float(input( "Zinssatz:"))

    # Verarbeitung
    jahr = 0

    # Kopfgesteuerte Schleife
    while startkapital < zielkapital :
        zinsen = startkapital * zinssatz /100
        startkapital = startkapital + zinsen
        jahr = jahr + 1
        print(" Laufzeit in Jahren:",jahr, "erreichtes Kapital:", startkapital)
        
    startkapital = round(startkapital, 2)    

    print(" Laufzeit in Jahren:",jahr, "erreichtes Kapital:", startkapital)



def ausgabe_zahlen():
    i=0
    while (i <=10):
        print (i)
        i=i+1

# Aufruf
berechneLaufzeit()
ausgabe_zahlen()        


