import numpy as np
import scipy.ndimage
from scipy.misc import toimage
import cv2
from load_mnist import load_mnist

# print 'Original array:'
# print im
#
# print 'Resampled by a factor of 2 with nearest interpolation:'
# res = cv2.resize(im,(6, 3), interpolation = cv2.INTER_CUBIC)
#
# print res

def get_new_diment(dataset=None):
    if dataset is None:
        return
    lowestR = dataset.shape[2]
    highestR = 0
    lowestC = dataset.shape[1]
    highestC = 0
    new_dimensions = np.zeros((dataset.shape[0],4))
    for x in range(dataset.shape[0]):
        lR = dataset.shape[2] # first zero before value
        hR = 0 # highest zero after value
        for i in range(dataset.shape[1]):
            for j in range(dataset.shape[2]-1):
                if(abs(dataset[x,i,j]) <= 1e-5 and dataset[x,i,j+1] > 1e-5):
                    lR = min(lR,j+1)
                    break
            cR = 0
            for j in range(dataset.shape[2]-1):
                if(abs(dataset[x,i,j]) > 1e-5 and dataset[x,i,j+1] <= 1e-5):
                    cR = j
            hR = max(hR,cR)
        lowestR = min(lowestR,lR)
        highestR = max(highestR,hR)
        lC = dataset.shape[1]
        hC = 0
        for i in range(dataset.shape[2]):
            for j in range(dataset.shape[1]-1):
                if(abs(dataset[x,j,i]) <= 1e-5 and dataset[x,j+1,i] > 1e-5):
                    lC = min(lC,j+1)
                    break
            cC = 0
            for j in range(dataset.shape[2]-1):
                if(abs(dataset[x,j,i]) > 1e-5 and dataset[x,j+1,i] <= 1e-5):
                    cC = j
            hC = max(hC,cC)
        lowestC = min(lowestC,lC)
        highestC = max(highestC,hC)
        new_dimensions[x][0] = lC
        new_dimensions[x][1] = hC
        new_dimensions[x][2] = lR
        new_dimensions[x][3] = hR
    return lowestC,highestC,lowestR,highestR,new_dimensions

def bounding_box_preprocess(dataset=None):
    lowestC,highestC,lowestR,highestR,dimensions = get_new_diment(dataset)
    newWidth = highestC - lowestC + 1
    newHeight = highestR - lowestR + 1
    print(newHeight,newWidth)
    newDataSet = np.zeros((dataset.shape[0],newHeight,newWidth))
    for x in range(dataset.shape[0]):
        arr = dataset[x]
        arr = arr[dimensions[x][2]+1:dimensions[x][3]+1,dimensions[x][0]+1:dimensions[x][1]+1]
        res = cv2.resize(arr,(newWidth, newHeight), interpolation = cv2.INTER_CUBIC)
        for i in range(newHeight-1):
            for j in range(newWidth-1):
                newDataSet[x,i,j] = res[i,j]
    return newDataSet
