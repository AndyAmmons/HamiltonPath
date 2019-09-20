import numpy as np
import json as js
import os
from skimage.draw import polygon
import cv2
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import re

imETply = 'c:/Users/RandyCocks/Desktop/R_Projects/cnnDir/balsamRootPolygons&Images/'
imagepath = 'c:/Users/RandyCocks/Desktop/R_Projects/sourceImages/'

testImage = imETply + 'FLIR1749.jpg'
testPoly = imETply + 'FLIR1749_labels.json'
testPoly = open('c:/Users/RandyCocks/Desktop/R_Projects/cnnDir/balsamRootPolygons&Images/FLIR1749__labels.json')



def maskImage(imagefile, polyfile,boxsize = 0):
    '''
        Params:
            imagefile - .jpg image to map the masked matrix to.
            polyfile - .json file of polygons from which the mask
                        will be generated.
            boxsize - dont know yet
        Purpose:
            This function takes an image and a polygon file and gene-
            rates a mask matrix for later identification.
    '''
    image = cv2.imread(imagefile)
    mask = np.zeros((image.shape[0], image.shape[1]))
    
    poly = js.load(polyfile)
    polyfile.close()

    vertices = [vert for label in poly['labels'] for vert in label['vertices']]
    x,y = zip(*[(Z['x'],Z['y']) for Z in vertices])

    r,c = polygon(x,y,shape=image.shape)
    mask[c,r] = 1
    n_instances = len(r)

    if n_instances > 1:
        return image, mask
    return None,None


def normalize_image(im):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        tmp = np.zeros((im.shape))
        mask = np.zeros((im.shape[0], im.shape[1]))
        scaler = StandardScaler() 
        scaler.fit(im[:, :, 0])
        tmp[:, :, 0] = scaler.transform(im[:, :, 0])
        scaler2 = StandardScaler()
        scaler2.fit(im[:, :, 1])
        tmp[:, :, 1] = scaler2.transform(im[:, :, 1])
        scaler3 = StandardScaler()
        scaler3.fit(im[:, :, 2])
        tmp[:, :, 2] = scaler3.transform(im[:, :, 2])
    return tmp 



def generate_labels_and_features(polypath,imagepath, kernel_size):
    leaves = []
    not_leaves = []

    for f in glob.glob(polypath + "*.json"):
        fileNum = re.findall(r'\d+',f)
        jpg = 'source' + fileNum + '.jpg'
        
        image, mask = maskImage(f, jpg, kernel_size)
        bees += features
        neg_features = generate_not_bees(image, mask, len(features), kernel_size)
        not_bees += neg_features

    features = bees + not_bees
    u = features[0].shape
    ret = np.zeros((len(features), u[0], u[1], u[2]))
    for i, e in enumerate(features):
    # print(i, e.shape, ret.shape)
        ret[i, :, :, :] = e
    labels = [1]*len(bees) + [0]*len(not_bees)
    labels = make_one_hot(labels, 2)
    return np.asarray(features), np.asarray(labels)

def make_one_hot(labels, n_classes):

    ret = np.zeros((len(labels), n_classes))
    for i, e in enumerate(labels):
        ret[i, e] = 1
    return ret



