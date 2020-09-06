import torch
from torch.autograd import Variable

import numpy
import models.dcgan as dcgan
import numpy as np
import random

import queue
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--zdims', default=None, help='Number of types of tiles')
option = parser.parse_args()

modelToLoad = 'Final Generator PTH/RMSPropNZ8_45.pth' #Generator model to load to generate levels
sizeLatent = 8 #Size of latent vector
batchSize = 1

imageSize = 32
ngf = 64
ngpu = 1
n_extra_layers = 0
z_dims = int(option.zdims)

generator = dcgan.DCGAN_G(imageSize, sizeLatent, z_dims, ngf, ngpu, n_extra_layers)
generator.load_state_dict(torch.load(modelToLoad, map_location=lambda storage, loc: storage))


for i in range(1000):
    randomLatent = []
    for _ in range(sizeLatent):
        randomLatent.append(random.uniform(-1,1)) 

    latent_vector = torch.FloatTensor(randomLatent).view(batchSize, sizeLatent, 1, 1) 
    levels = generator(Variable(latent_vector, volatile=True))
    level = levels.data.cpu().numpy()
    # print('LEVEL BEFORE', level.shape)
    level = level[:,:,:11, :16] #Extracting the level from the padded output
    level = numpy.argmax( level, axis = 1) #Reversing the one hot encoding

    finalLevel = level[0] #The final 11x16 generated level
    # print(finalLevel.shape)
    # print(finalLevel)
    
    unique, counts = np.unique(finalLevel, return_counts=True)
    # print(dict(zip(unique, counts)))

    np.save(f'Lee Algorithm BFS/level_{i}.npy', finalLevel)
    np.save(f'levelImage/level_{i}.npy', finalLevel)
