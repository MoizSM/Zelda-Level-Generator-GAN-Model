from PIL import Image
import numpy as np
import random

water = Image.open('tiles/water.png')
dark = Image.open('tiles/dark.png') 

for imageNum in range(1000):
    
    fileName = f'level_{imageNum}'
    level = np.load(fileName + '.npy')

    element = random.choice([water, dark])
    floorGreen = Image.open('tiles/green/floor_green.png')
    floorCyan = Image.open('tiles/cyan/floor_cyan.png')
    floor = random.choice([floorCyan, floorGreen])

    if (floor == floorCyan):
        block = Image.open('tiles/cyan/block_cyan.png')
        leftDoor = Image.open('tiles/cyan/leftDoor_cyan.png')
        rightDoor = Image.open('tiles/cyan/rightDoor_cyan.png')
        upDoor = Image.open('tiles/cyan/upDoor_cyan.png')
        downDoor = Image.open('tiles/cyan/downDoor_cyan.png')
        elemBlock = Image.open('tiles/cyan/fireBlock_cyan.png')

    elif (floor == floorGreen):
        block = Image.open('tiles/green/block_green.png')
        leftDoor = Image.open('tiles/green/leftDoor_green.png')
        rightDoor = Image.open('tiles/green/rightDoor_green.png')
        upDoor = Image.open('tiles/green/upDoor_green.png')
        downDoor = Image.open('tiles/green/downDoor_green.png')
        elemBlock = Image.open('tiles/green/fireBlock_green.png')

        

    y1 = 0
    y2 = 100

    x1 = 0
    x2 = 100

    w, h = 1600,1100
    data = np.zeros((h, w, 3), dtype=np.uint8)
    for i in range(11):
        for j in range(16):
            if(level[i][j] == 0):
                data[y1:y2, x1:x2] = floor
            elif(level[i][j] == 1):
                data[y1:y2, x1:x2] = block
            elif(level[i][j] == 2):
                data[y1:y2, x1:x2] = block
            elif(level[i][j] == 3):
                if(j==1):
                    data[y1:y2, x1:x2] = leftDoor
                elif(i==1):
                    data[y1:y2, x1:x2] = upDoor
                elif(j==14):
                    data[y1:y2, x1:x2] = rightDoor
                elif(i==9):
                    data[y1:y2, x1:x2] = downDoor    
            elif(level[i][j] == 4):
                data[y1:y2, x1:x2] = element
            elif(level[i][j] == 5):
                data[y1:y2, x1:x2] = elemBlock 


                            

            x1+=100
            x2+=100
        x1 = 0
        x2 = 100
        y1+=100
        y2+=100

    img = Image.fromarray(data, 'RGB')
    img.save(f'{fileName}.png')

print('DONE')