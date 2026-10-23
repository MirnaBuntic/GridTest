#Definerar en funktion som tar emot ett filnamn som parameter
def read_grid_from_file(filename):
    #Öppnar filen i läsläge och stänger filen automatiskt när blocket avslutas
    with open(filename, "r") as f:
        #Variabel som läser in hela filens innehåll som en string
        content = f.read()

        #Delar upp stringen vid varje radbrytning -> lista där varje element är en rad (str)
        rows = content.splitlines()
        #print(rows)

        #Skapar en tom lista som ska innehålla våran grid
        rowList = []

        #Går igenom varje rad i filen
        for r in rows:
            #Delar upp raden i separata strings för varje tal
            numbers = r.split()

            #Skapar en tom lista för den aktuella raden 
            newRows = []

            #Går igenom varje tal i raden 
            for n in numbers:
                #Konverterar varje string till ett heltal och lägger till det i den aktuella raden
                newRows.append(int(n))

            #När alla tal i raden är konverterade så lägger vi till den i listan för våran grid
            rowList.append(newRows)
        
        return rowList

#Anropar funktionen med filnamnet och sparar resultatet i variabeln grid
grid = read_grid_from_file("riskgrid.txt")

#For loop för bättre översikt i terminalen
for row in grid:
    print(row)
