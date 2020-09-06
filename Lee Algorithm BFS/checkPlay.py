from collections import deque
import numpy as np
import random

count = 0


for levelNumber in range(1000):
    fileName = f'level_{levelNumber}'

    originalLevel = np.load(fileName + '.npy')

    level = originalLevel[1:-1, 1:-1]
    numOfRows = level.shape[0]
    numOfCols = level.shape[1]
    x = [0,level.shape[0]-1]
    y = [0,level.shape[1]-1]
    pick = [x,y]

    for _ in range(2):
        pickRandomList = pick[random.randrange(len(pick))]
        if pickRandomList == [0,level.shape[0]-1]:
            j = int(level.shape[1]/2)
            i = pickRandomList[random.randrange(len(pickRandomList))]
            door1 = [i,j]
            level[i,j] = 3
            pick.pop(pick.index(pickRandomList))

        if pickRandomList == [0,level.shape[1]-1]:
            j = int(level.shape[0]/2)
            i = pickRandomList[random.randrange(len(pickRandomList))]
            door2 = [j,i]
            level[j,i] = 3
            pick.pop(pick.index(pickRandomList))

    nonwalkable = np.where((level != 0))
    walkable = np.where((level == 0) | (level == 3))
    level[nonwalkable] = 0
    level[walkable] = 1

    # Storing the coordinates of the level 
    class Coordinates: 
        def __init__(self,x: int, y: int): 
            self.x = x 
            self.y = y 

    # Content of the Queue ((current coordinates), Total Travelled Distance from start point) 
    class bfsQueue: 
        def __init__(self,pt: Coordinates, dist: int): 
            self.pt = pt  # The cordinates of the cell 
            self.dist = dist  # Total distance from the  start point 

    #Check if the current coordinates of the level (matrix) are valid 
    def isValid(row: int, col: int): 
        return (row >= 0) and (row < numOfRows) and (col >= 0) and (col < numOfCols) 

    rowNum = [-1, 0, 0, 1] #Moving row-wise 
    colNum = [0, -1, 1, 0] #Moving column-wise

    # Function that determines the shortes path to the destination (if exists) and returns the total shortest distance
    def BFS(mat, src: Coordinates, dest: Coordinates): 

        # If the start point and destination coordinates are not 1 then the maze is invalid  
        if mat[src.x][src.y]!=1 or mat[dest.x][dest.y]!=1: 
            return -1

        visited = [[False for i in range(numOfCols)] for j in range(numOfRows)] #Create a matrix of visited point.

        # Mark the start point as visited 
        visited[src.x][src.y] = True

        # Create a queue for BFS  
        q = deque() 

        # Total distance at the start point is 0 
        s = bfsQueue(src,0) 
        q.append(s) #Enqueue the current point and current total distance 

        # While the queue has items (coordinates and total distance)  
        while q: 

            curr = q.popleft() # Dequeue the item 

            # Check if the coordinates of the dequeued item is equal to the coordinates of the destination  
            pt = curr.pt 
            if pt.x == dest.x and pt.y == dest.y: 
                return curr.dist #Return the total current distance

            # Otherwise enqueue its adjacent cells  
            for i in range(4): 
                row = pt.x + rowNum[i] 
                col = pt.y + colNum[i] 

                # Check if the next row and col are acceptable paths and have not been visited yet.  
                if (isValid(row,col) and mat[row][col] == 1 and not visited[row][col]):
                    #Mark those points as visited now 
                    visited[row][col] = True
                    #Add the coordinates to the queue
                    adjacentCell = bfsQueue(Coordinates(row,col),curr.dist+1) 
                    q.append(adjacentCell) 

        # If there is acceptable path to the destination return the total distance as -1  
        return -1


    mat = level
    currPoint = Coordinates(door1[0],door1[1]) 
    destPoint = Coordinates(door2[0], door2[1]) 
    totalDistance = BFS(mat, currPoint, destPoint)

    # print(f'LEVEL_{levelNumber}\n', level, '\n')


    if (totalDistance!=-1):
        pass
        print('The shortest path found between the doors is', totalDistance, 'steps-------------------------------------\n')
    else:
        print('There is no acceptable path between the doors-----------------------------------------\n')
        count+=1

print('The number of unplayable levels are', count)
percentage = int((count/1000) * 100)
print(f'Percentage - {percentage}%')