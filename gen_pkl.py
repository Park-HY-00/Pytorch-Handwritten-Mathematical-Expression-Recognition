'''
Python 3.6 
Pytorch 0.4
Written by Hongyu Wang in Beihang university
'''
import os
import sys
import pandas as pd
import pickle as pkl
import numpy
from scipy.misc import imread, imresize, imsave

# image_path='C:\\Users\\msraspeech\\PycharmProjects\\v-honwa\\off_image_test\\off_image_test\\'
image_path='C:\\Users\\parkhy\\ProPEER\\Pytorch-Handwritten-Mathematical-Expression-Recognition\\off_image_train\\off_image_train\\'
# image_path 수정
oupFp_feature=open(outFile,'wb')

features={}

channels=1

sentNum=0

# scpFile=open('C:\\Users\\msraspeech\\PycharmProjects\\v-honwa\\test_caption.txt')
scpFile=open('C:\\Users\\parkhy\\ProPEER\\Pytorch-Handwritten-Mathematical-Expression-Recognition\\train_caption.txt')
# scpFile 경로 수정
while 1:
    line=scpFile.readline().strip() # remove the '\r\n'
    if not line:
        break
    else:
        key = line.split('\t')[0]
        image_file = image_path + key + '_' + str(0) + '.bmp'
        im = imread(image_file)
        mat = numpy.zeros([channels, im.shape[0], im.shape[1]], dtype='uint8')
        for channel in range(channels):
            image_file = image_path + key + '_' + str(channel) + '.bmp'
            im = imread(image_file)
            mat[channel,:,:] = im
        sentNum = sentNum + 1
        features[key] = mat
        if sentNum / 500 == sentNum * 1.0 / 500:
            print('process sentences ', sentNum)

print('load images done. sentence number ',sentNum)

pkl.dump(features,oupFp_feature)
print('save file done')
oupFp_feature.close()
