# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 19:36:00 2018

@author: yzzhao2
"""

import numpy as np
import os
from PIL import Image
from CNI_CCI_indexes import *

# read a folder, return the complete path
def get_files(path):
    ret = []
    for root, dirs, files in os.walk(path):  
        for filespath in files: 
            ret.append(os.path.join(root,filespath)) 
    return ret

# New indexes accuracy for dataset
def Dset_Acuuracy(base):
    # Define the list saving the accuracy
    CNIlist = []
    CCIlist = []
    CCI_determinelist = []
    CNIratio = 0
    CCIratio = 0
    CCI_determineratio = 0
    
    # Get all images in this folder
    imglist = get_files(base)
    
    # Compute the accuracy
    for i in range(len(imglist)):
        # Full imgpath
        imgpath = imglist[i]
        # Compute the traditional indexes
        CNI = SingleImageCNI(imgpath)
        CCI, CCI_determine = SingleImageCCI(imgpath)
        CNIlist.append(CNI)
        CCIlist.append(CCI)
        CCI_determinelist.append(CCI_determine)
        CNIratio = CNIratio + CNI
        CCIratioratio = CCIratio + CCI
        CCI_determineratio = CCI_determineratio + CCI_determine
        print('The %dth image: CNI: %f, CCI: %f, CCI_determine: %d' % (i, CNI, CCI, CCI_determine))
    CNIratio = CNIratio / len(imglist)
    CCIratioratio = CCIratioratio / len(imglist)
    CCI_determineratio = CCI_determineratio / len(imglist)

    return CNIlist, CCIlist, CCI_determinelist, CNIratio, CCIratioratio, CCI_determineratio
    
if __name__ == "__main__":
    
    # Define imgpath, change it with your own folder path
    base = 'GT'
    
    CNIlist, CCIlist, CCI_determinelist, CNIratio, CCIratioratio, CCI_determineratio = Dset_Acuuracy(base)

    print('The overall results for %s: CNI: %f, CCI: %f, CCI_determine in [16, 20]: %f' % (base, CNIratio, CCIratioratio, CCI_determineratio))
    