#GCamp analysis
#This program accepts a kymograph of chlamydomonas flagella containing drc4-GCamp
#and measures the amount of intra-flagellar calcium

#Packages:
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage, signal
import pandas as pd
import csv
import os

def CalciumConc(loc, name):
    #=============
    #File Location
    #=============

    #loc = "pf2-drc-mcherry-gcamp-18\kymograph_29 filtered_backward.tif"
    #loc = "pf2-drc-mcherry-gcamp-17a\kymograph_26 filtered_backward.tif"
    #loc = "pf2-drc-mcherry-gcamp-14b\kymograph_22 filtered_backward.tif"
    #loc = "pf2-drc-mcherry-gcamp-11b\kymograph_19 filtered_backward.tif"

    #name = "pf2-drc-mcherry-gcamp-18"

    #=====================
    #Microscope Parameters
    #=====================
    px_size = 0.104667 #Length of each pixel (um/px)
    fps = 19.33 #Framerate

    #================
    #Data acquisition
    #================
    im = ndimage.imread(loc, flatten=True)
    cropend = int(0.9 * len(im))

    #Crop off the last 100 frames which contain brightfield image
    im = im[0:cropend,]
    #Display image
    # plt.figure()
    # plt.imshow(im, cmap = 'gray')
    # plt.show()

    #==========================
    #Determine Flagellar Length
    #==========================
    #Assumptions: Flagella starts at the beginning of the image, and ends when the brightness falls below a certain threshold
    #Add all entries in each column
    minvalue = 13 #Set threshold for being counted as a point

    colsums =[]
    for col in range(0, im.shape[1]):
        total = 0
        for row in range(0, im.shape[0]):
            total = total + im[row][col]
        colsums.append(total/im.shape[0])

    #Find point from the end where value exceeds threshold
    flapx = int(len(colsums))-1

    print("Colsums: ", colsums, "\n")
    while(colsums[flapx] < minvalue):
        flapx = flapx - 1

    #i is now the nth pixel where brightness drops off (where the flagella ends)
    flalength = flapx * px_size
    print("Length: ", flalength, "\n")

    # plt.figure()
    # plt.plot(colsums)
    #plt.show()

    #====================================
    #Determine total brightness over time
    #====================================

    #Sum over the length of the flagellum at each timepoint
    #Recall flapx is the end position of the flagellum
    #Reports total intensity / flagella length
    rowsums = []
    for row in range(0, im.shape[0]):
        total = 0
        for col in range(0, flapx):
            total = total + im[row][col]
        rowsums.append(total/flalength)

    print("Rowsums: ", rowsums, "\n")
    plt.figure()
    plt.plot(rowsums)
    plt.show()


    #============
    #Detect peaks
    #============

    #Recall that rowsums is a vector containing intensity at each position
    peaks = list(signal.find_peaks_cwt(rowsums, np.arange(20,30))) #Location of each peak by wavelet method
    peaks = [int(x) for x in peaks] #Convert list of peaks to list of integer indices

    D1 = signal.savgol_filter(rowsums,3,1)
    peakheight = D1[peaks]
    #
    # plt.figure()
    # plt.plot(rowsums)
    # plt.scatter(peaks, peakheight)
    # plt.show()


    #=================
    #Average peak area
    #=================

    #Assumes that baseline is 0
    #Calculates average peak area by adding all points, then dividing by number of peaks
    #Recall rowsum is a vector containing intensity/um
    #First puts in units of just intensity

    totalintensity = 0
    for i in range(0, len(rowsums)):
        totalintensity = totalintensity + rowsums[i]*flalength

    avgPeakArea = totalintensity/len(peaks)
    capertime = totalintensity/len(im) #total calcium divided by time
    print("AvgPeakArea: ", avgPeakArea, "\n")


    #===========
    #Output Data
    #===========

    #Data format: [samplename, flagella length, calcium/time, calcium/pulses]

    Data = [name, flalength, capertime, avgPeakArea]
    print("Data: ", Data, "\n")

    if(not os.path.isfile("Data.csv")):
        with open(r"Data.csv",'a') as f:
            writer = csv.writer(f)
            writer.writerow(["Sample","flalength","CaPerTime","CaPerPulse"])

    with open(r"Data.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(Data)
