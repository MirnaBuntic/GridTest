#Definerar en funktion som läser in txt-filen och konverterar den från sting till integar
def read_grid_from_file(filename):
    with open(filename, "r") as f:

        content = f.read()
        rows = content.splitlines() #Delar raderna i varsin string

        row_list = []

        for r in rows:
            numbers = r.split() #Delar talen i varsin string
            new_rows = []

            for n in numbers:
                new_rows.append(int(n))

            row_list.append(new_rows)
        
        return row_list

#Anropar funktionen med filnamnet och sparar resultatet i variabeln grid
grid = read_grid_from_file("riskgrid.txt")


#Hjälpfunktion för find_risk_clusters för att slippa checka medelvärde på varje riktning
#Definerar en funktion som tar emot de fyra riskvärderna, positionera för de fyra värderna, riktningen som klustret hittades i och listan där signifikanta kluster ska sparas
def add_if_significant(values, indices, direction, cluster_list):

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
        cluster_list.append(cluster_info)
  

#Definerar en funktion som checkar om det går att bilda kluster med 4 ammanhängande celler i olika riktningar
def find_risk_clusters(grid):

    cluster_list = []

    for row in range(len(grid)):
        for col in range(len(grid[row])):

            #Variabler för vilka riktiningar från startposition som går utan att hamna utanför gridets gränser
            can_move_right = col + 3 < len(grid[row])
            can_move_down = row + 3 < len(grid)
            can_move_up = row - 3 >= 0

            #Horisontellt åt höger
            if can_move_right:
                right_cluster = [] #Riskvärden
                right_indices = [] #Positioner till riskvärden

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

#Anropar funktionen och sparar alla signifikanta kluster
significant_clusters = find_risk_clusters(grid)


#Hjälpfunktion för sort_clusters
#Definerar en funktion som tar emot ett riskkluster och retunerar värderna
def get_sort_key(risk_cluster):

    #Första index är klustrets första position
    #Andra index är radens/kolomnens första position
    row = risk_cluster["indices"][0][0] 
    col = risk_cluster["indices"][0][1]

    return (risk_cluster["average"], max(risk_cluster["values"]), -row, -col)


#Definerar en funktion som tar emot listan med signifikanta kluster och sorterar den efter reglerna
def sort_clusters(significant_clusters):
    return sorted(significant_clusters, key=get_sort_key, reverse=True)


#Anropar sorteringsfunktionen och sparar den nya listan 
sorted_clusters = sort_clusters(significant_clusters)


#Definerar en funktion som skriver ut alla signifikanta kluster på varsin rad
def print_significant_clusters(clusters):
    for cluster in clusters:
        print(cluster)


#Anropar funktionen som skriver ut resultatet i terminalen
print_significant_clusters(sorted_clusters)