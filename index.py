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
        row_list = []

        #Går igenom varje rad i filen
        for r in rows:
            #Delar upp raden i separata strings för varje tal
            numbers = r.split()

            #Skapar en tom lista för den aktuella raden 
            new_rows = []

            #Går igenom varje tal i raden 
            for n in numbers:
                #Konverterar varje string till ett heltal och lägger till det i den aktuella raden
                new_rows.append(int(n))

            #När alla tal i raden är konverterade så lägger vi till den i listan för våran grid
            row_list.append(new_rows)
        
        return row_list

#Anropar funktionen med filnamnet och sparar resultatet i variabeln grid
grid = read_grid_from_file("riskgrid.txt")

#For loop för bättre översikt i terminalen
#for row in grid:
 #   print(row)


def find_risk_clusters(grid):
    cluster_list = []

    for row in range(len(grid)):
        for col in range(len(grid[row])):

            can_move_right = col + 3 < len(grid[row])
            can_move_down = row + 3 < len(grid)
            can_move_up = row - 3 >= 0

            #Horisontellt åt höger
            if can_move_right:
                right_cluster = []

                for i in range(4):
                    right_cluster.append(grid[row][col + i])
                cluster_list.append(right_cluster)

            #Vertikalt nedåt
            if can_move_down:
                down_cluster = []

                for i in range(4):
                    down_cluster.append(grid[row + i][col])
                cluster_list.append(down_cluster)

            #Diagonalt ner åt höger
            if can_move_right and can_move_down:
                down_right_cluster = []

                for i in range(4):
                    down_right_cluster.append(grid[row + i][col + i])
                cluster_list.append(down_right_cluster)

            #Diagonalt upp åt höger
            if can_move_right and can_move_up:
                up_right_cluster = []

                for i in range(4):
                    up_right_cluster.append(grid[row - i][col + i])
                cluster_list.append(up_right_cluster)

    return cluster_list

clusters = find_risk_clusters(grid)


def find_significant_clusters(clusters):
    significant_cluster_list = []

    for cluster in clusters:
        average_value = sum(cluster) / len(cluster)

        if average_value >= 70:
            significant_cluster_list.append(cluster)

    return significant_cluster_list



significant_clusters = find_significant_clusters(clusters)
print(len(significant_clusters))