import json
import numpy as np

checkFile = 'final.json'
with open(checkFile) as levels:
    dataLevel = json.load(levels)

x = np.array(dataLevel)
unique, counts = np.unique(x, return_counts=True)
print(dict(zip(unique, counts)))
print(x.shape)