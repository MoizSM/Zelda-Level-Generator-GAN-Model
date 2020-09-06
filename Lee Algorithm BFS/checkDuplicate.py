import json
import numpy as np

checkFile = 'FWBPI45.json'

with open(checkFile) as levels:
    dataLevel = json.load(levels)

dataNP = np.array(dataLevel)

count = 0
for i in range(1000):
    data = np.load(f'level_{i}.npy')
    for x in dataNP:
        check = data == x
        if (check.all() == True):
            count+=1
            break    

print(count)
percentage = int((count/1000) * 100)
print(f'Percentage - {percentage}%')
        

