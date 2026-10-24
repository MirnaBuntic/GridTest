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

#Hjälpfunktion för find_risk_clusters för att slippa checka medelvärde på varje riktning fyra gånger
#Definerar en funktion som tar emot de fyra riskvärderna, positionera för de fyra värderna, riktningen som klustret hittades i och listan där signifikanta kluster ska sparas
def add_if_significant(values, indices, direction, cluster_list):

    #Beräknar klustrets medelvärde
    average_value = sum(values) / len(values)

    #Om medelvärdet är större eller lika med 70 sparas dess värden i en dictionary
    if average_value >= 70:
        cluster_info = {
            "values": values,
            "indices": indices,
            "direction": direction,
            "average": average_value
        }
        #Lägger till dicten i listan med signifikanta kluster
        #Behöver inte retunera listan eftersom den skickas in som ett argument
        cluster_list.append(cluster_info)
  

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
                right_indices = []

                for i in range(4):
                    right_cluster.append(grid[row][col + i])
                    right_indices.append((row, col + i))

                add_if_significant(right_cluster, right_indices, "right", cluster_list)

            #Vertikalt nedåt
            if can_move_down:
                down_cluster = []
                down_indices = []

                for i in range(4):
                    down_cluster.append(grid[row + i][col])
                    down_indices.append((row + i, col))

                add_if_significant(down_cluster, down_indices, "down", cluster_list)

            #Diagonalt ner åt höger
            if can_move_right and can_move_down:
                down_right_cluster = []
                down_right_indices = []

                for i in range(4):
                    down_right_cluster.append(grid[row + i][col + i])
                    down_right_indices.append((row + i, col + i))

                add_if_significant(down_right_cluster, down_right_indices, "down-right", cluster_list)

            #Diagonalt upp åt höger
            if can_move_right and can_move_up:
                up_right_cluster = []
                up_right_indices = []

                for i in range(4):
                    up_right_cluster.append(grid[row - i][col + i])
                    up_right_indices.append((row - i, col + i))

                add_if_significant(up_right_cluster, up_right_indices, "up-right", cluster_list)

    return cluster_list

significant_clusters = find_risk_clusters(grid)


#print(len(significant_clusters))


def get_sort_key(risk_cluster):
    row = risk_cluster["indices"][0][0]
    col = risk_cluster["indices"][0][1]

    return (risk_cluster["average"], max(risk_cluster["values"]), -row, -col)

def sort_clusters(significant_clusters):
    return sorted(significant_clusters, key=get_sort_key, reverse=True)

sorted_clusters = sort_clusters(significant_clusters)


for cluster in sorted_clusters:
    print(cluster)
