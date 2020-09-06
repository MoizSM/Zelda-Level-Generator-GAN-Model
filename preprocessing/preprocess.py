import numpy as np
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--dungeon', default=None, help='Text Level File')
option = parser.parse_args()

fileName = option.dungeon
print(fileName)

dungeon = []
#Opening the dungeons text representation file and reading the content into a list
with open(fileName + '.txt', 'r') as filehandle:
    for line in filehandle:
        # removing the last character of the string which is a linebreak (\n)
        currentLine = line[:-1]
        # adding the current line to the dungeon list
        dungeon.append(currentLine)


# F = FLOOR - 0
# B = BLOCK - 2
# M = MONSTER
# P = ELEMENT (LAVA, WATER)
# O = ELEMENT + FLOOR (LAVA/BLOCK, WATER/BLOCK)
# I = ELEMENT + BLOCK
# D = DOOR - 3
# S = STAIR
# W = WALL - 1
# - = VOID - 9
for i, sprite in enumerate(dungeon):
    dungeon[i] = dungeon[i].replace('F','0').replace('M', '0').replace('O', '0').replace('S', '0').replace('W','1').replace('B', '2').replace('P', '4').replace('I','5').replace('D', '1').replace('-', '9')

convertedDungeon = []

for sprite in dungeon:
    convertedDungeon.append(list(sprite)) #Splitting the sprites row into seperate tiles

for i, sprite in enumerate(convertedDungeon):
    for j, y in enumerate(sprite):
        convertedDungeon[i][j] = int(convertedDungeon[i][j]) #Converting the charaters into integer representation

convertedDungeon = np.array(convertedDungeon)
print(convertedDungeon.dtype)

rooms = []

a = np.vsplit(convertedDungeon, convertedDungeon.shape[0]/16)
for x in a:
    rooms.append(np.hsplit(x, convertedDungeon.shape[1]/11))
    
allRooms = []
for room in rooms:
    for y in room:
        allRooms.append(y)

voidFilter = np.empty(shape=(16,11), dtype = int)
voidFilter.fill(9)

#Removing any void rooms from the dungeon representation
allRooms = [room for room in allRooms if room not in voidFilter]
allRooms = np.array(allRooms)

#Transforming each room from 16 x 11 into 11 x 16
reshapeDungeon = []
for room in allRooms:
    reshapeDungeon.append(room.T)

reshapeDungeon = np.array(reshapeDungeon)
#Converting the preprocessed levels to json
jsonDungeon = json.dumps(reshapeDungeon.tolist())

#Saving the json file
with open(fileName + '.json', 'w') as outfile:
    json.dump(jsonDungeon, outfile)

#--------------------------------TESTING PURPOUSE ONLY------------------

#Loading the json file to test
with open(fileName + '.json') as json_file:
    data = json.load(json_file)

dataList = json.loads(data)
dataList

#Count Tiles
unique, counts = np.unique(dataList, return_counts=True)
print(dict(zip(unique, counts)))

dataList = np.array(dataList)

print(dataList.shape)
print(dataList[0].T)
print('\n')
print(dataList[dataList.shape[0]-1].T)
#-----------------------------------------------------------------------