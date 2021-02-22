# Makes an M x N grid containing obstacles X with other nodes containing numbers from range max -> min.
import random
import os

def makeCSV(m, n, maxVal, minVal, numObstacles, startX, startY, numGoals):

    pwd = os.path.abspath(os.getcwd())
    grid = []

    # Make a M x N grid full of values - M num rows, N columns
    for i in range (0,m):
        grid.append([])
        for j in range (0,n):
            node_value = random.randint(minVal,maxVal)
            grid[i].append(node_value)

    # Add the obstacles, goals, and start locations
    for i in range (0,numObstacles):
        y_coord = random.randint(0,m-1)
        x_coord = random.randint(0,n-1)

        grid[y_coord][x_coord] = 'X'
    
    for i in range (0,numGoals):
        y_coord = random.randint(0,m-1)
        x_coord = random.randint(0,n-1)

        grid[y_coord][x_coord] = 'G'
    
    grid[startY][startX] = 'S'

    file = open(pwd + "/testfile.txt","w+")

    # Write to file
    for i in range (0,m):
        list_row = grid[i]
        listToStr = ', '.join(map(str, list_row))
        file.write(listToStr + '\n')

    file.close()

    return 

# makeCSV(m, n, maxVal, minVal, numObstacles, startX, startY, numGoals)
makeCSV(1000, 800, 5, 1, 300, 0, 0, 3)